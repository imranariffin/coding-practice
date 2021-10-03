from collections import Counter
from typing import Dict, Optional, SupportsIndex, Iterable, List, Tuple, TypeVar, Union
import unittest

T = TypeVar("T")


class DuplicateValueError(Exception):
    pass


class HashedList(List[T]):
    """
    A List with O(1) time complexity for `.index()` method, instead of O(N).

    A data structure that is pretty much a Python list, except that:
        1. The method `.index(value)` is O(1) (Good)
        2. The data structure uses twice more memory due to indexing
           (Not good but still okay)
        3. Items must be unique. It will raise DuplicateValueError if
           duplicate item is provided

    Main use case:
        You have a huge list of unique items that:
            1. You may update the list (remove, insert, set value etc) from
               time to time
            2. You may get the index of a specific item in the list from
               time to time

        In this case, using just a regular list definitely works but will cost
        you O(N) each time you get the index of a specific item. Or, you can
        maintain along the list a dictionary of item => index ,but that will cost
        you the burden of updating the dictionary everytime the list is updated.

        HashedList will make the work easy for you.
    """

    def __init__(self, iterable: Iterable[T]):
        super().__init__(iterable)
        self._validate(self)
        self._index: Dict[T, int] = {v: i for i, v in enumerate(iterable)}

    def __setitem__(self, key: Union[SupportsIndex, slice], value: Union[T, Iterable[T]]) -> None:
        new_values: Tuple[T] = tuple(value) if isinstance(value, Iterable) else (value,)
        old_values: Tuple[T] = tuple(self[key]) if isinstance(value, Iterable) else (self[key],)
        for new_value in new_values:
            self._validate_value(new_value)
        super().__setitem__(key, value)
        # Remove old indices
        for old_value in old_values:
            del self._index[old_value]
        # Update indices
        if isinstance(key, SupportsIndex):
            new_key_values = [(key, value)]
        else:  # key is a slice
            new_key_values = zip(range(key.start, key.stop), value)
        for new_index, new_value in new_key_values:
            self._index[new_value] = int(new_index)

    def append(self, value: T) -> None:
        self._validate_value(value)
        super().append(value)
        self._index[value] = len(self) - 1

    def extend(self, iterable: Iterable[T]) -> None:
        old_length = len(self)
        super().extend(iterable)
        self._validate(self)
        for i, v in enumerate(iterable):
            self._index[v] = old_length + i

    def insert(self, index: int, value: T) -> None:
        self._validate_value(value)
        super().insert(index, value)
        # Increment indices for the inserted value and all existing values to the right
        self._index[value] = index
        for i in range(index + 1, len(self)):
            self._index[self[i]] += 1

    def remove(self, value: T) -> None:
        super().remove(value)
        index = self._index[value]
        del self._index[value]
        # Decrement indices for all existing values to the right of the removed value
        for i in range(index, len(self)):
            self._index[self[i]] -= 1

    def pop(self, index: Optional[int] = None) -> T:
        value = super().pop(index) if index is not None else super().pop()
        if index is None:
            return value
        # Decrement indices for all existing values to the right of the removed value
        for i in range(index, len(self)):
            self._index[self[i]] -= 1
        return value

    def clear(self) -> None:
        super().clear()
        self._index = {}

    def index(self, value: T, start: Optional[int] = None, end: Optional[int] = None) -> int:
        try:
            index = self._index[value]
        except KeyError as error:
            raise ValueError(f"{value!r} is not in list") from error

        if start is not None and index < start or end is not None and index >= end:
            raise ValueError(f"{value!r} is not in list")

        return index

    def _validate_value(self, value: T) -> None:
        if value in self._index:
            raise DuplicateValueError(f"Duplicate values in HashedList")

    @staticmethod
    def _validate(iterables: Iterable[T]):
        counts = Counter(iterables)
        duplicate_values = {k: v for k, v in counts.items() if v > 1}
        if duplicate_values:
            raise DuplicateValueError(f"Duplicate values in HashedList")


class TestListParity(unittest.TestCase):
    """Assert that HashedArray is in feature parity with builtin list"""

    def test_index(self):
        harray = HashedList(list(range(10)))
        index = harray.index(9)
        self.assertEqual(index, 9)

    def test_index__with_start(self):
        ls: List[str] = ["10", "3", "5"]
        harray: HashedList[str] = HashedList(ls)

        self.assertEqual(harray.index("10", start=0), ls.index("10", 0))
        self.assertEqual(harray.index("3", start=1), ls.index("3", 1))
        self.assertEqual(harray.index("5", start=2), ls.index("5", 2))
        with self.assertRaises(ValueError) as context_harray:
            harray.index("10", start=1)
        with self.assertRaises(ValueError) as context_ls:
            ls.index("10", 1)
        self.assertEqual(context_harray.exception.args, context_ls.exception.args)

    def test_index__with_start_and_end(self):
        ls: List[str] = ["10", "3", "5"]
        harray: HashedList[str] = HashedList(ls)

        self.assertEqual(harray.index("10", start=0, end=3), ls.index("10", 0, 3))
        self.assertEqual(harray.index("3", start=1, end=3), ls.index("3", 1, 3))
        self.assertEqual(harray.index("5", start=2, end=3), ls.index("5", 2, 3))
        with self.assertRaises(ValueError) as context_harray:
            harray.index("5", start=0, end=1)
        with self.assertRaises(ValueError) as context_ls:
            ls.index("5", 0, 1)
        self.assertEqual(context_harray.exception.args, context_ls.exception.args)

    def test_empty(self):
        harray = HashedList([])
        try:
            ls = []
            ls.index(1)
        except Exception as e_list:
            try:
                harray.index(1)
            except Exception as e_harray:
                self.assertEqual(e_list.__class__, e_harray.__class__)
                self.assertEqual(e_list.args, e_harray.args)

    def test_lookup(self):
        ls = [1, 10, 22, -1]
        harray = HashedList(ls)

        self.assertEqual(ls[0], harray[0])
        self.assertEqual(ls[2], harray[2])
        self.assertEqual(ls[-1], harray[-1])
        self.assertEqual(ls[2:3], harray[2:3])

    def test_setitem(self):
        ls = [1, 10, 22, -1]
        harray = HashedList(ls)
        ls[0] = 2
        harray[0] = 2
        self.assertEqual(ls[0], harray[0])

        ls = [1, 10, 22, -1]
        harray = HashedList(ls)
        ls[2] = 99
        harray[2] = 99
        self.assertEqual(ls[2], harray[2])

        ls = [1, 10, 22, -1]
        harray = HashedList(ls)
        ls[-1] = -111
        harray[-1] = -111
        self.assertEqual(ls[-1], harray[-1])

        ls = [1, 10, 22, -1]
        harray = HashedList(ls)
        ls[1:3] = [3, 9]
        harray[1:3] = [3, 9]
        self.assertEqual(ls[1:3], harray[1:3])

    def test_append(self):
        ls = ["a", "b", "c"]
        harray = HashedList(ls)

        ls.append("Z")
        harray.append("Z")

        self.assertEqual(ls, harray)
        self.assertEqual(ls.index("Z"), harray.index("Z"))
        self.assertEqual(ls.index("c"), harray.index("c"))
        self.assertEqual(ls.index("b"), harray.index("b"))
        self.assertEqual(ls.index("a"), harray.index("a"))

    def test_extend(self):
        ls = ["a", "b", "c"]
        harray = HashedList(ls)

        ls.extend(["X", "Y", "Z"])
        harray.extend(["X", "Y", "Z"])

        self.assertEqual(ls, harray)
        self.assertEqual(ls.index("Z"), harray.index("Z"))
        self.assertEqual(ls.index("Y"), harray.index("Y"))
        self.assertEqual(ls.index("X"), harray.index("X"))
        self.assertEqual(ls.index("c"), harray.index("c"))
        self.assertEqual(ls.index("b"), harray.index("b"))
        self.assertEqual(ls.index("a"), harray.index("a"))

    def test_insert(self):
        # Insert at the beginning
        ls = ["a", "b", "c"]
        harray = HashedList(ls)
        ls.insert(0, "Z")
        harray.insert(0, "Z")
        self.assertEqual(ls, harray)
        self.assertEqual(ls.index("Z"), harray.index("Z"))
        self.assertEqual(ls.index("c"), harray.index("c"))
        self.assertEqual(ls.index("b"), harray.index("b"))
        self.assertEqual(ls.index("a"), harray.index("a"))

        # Insert into the middle
        ls = ["a", "b", "c"]
        harray = HashedList(ls)
        ls.insert(1, "Z")
        harray.insert(1, "Z")
        self.assertEqual(ls, harray)
        self.assertEqual(ls.index("Z"), harray.index("Z"))
        self.assertEqual(ls.index("c"), harray.index("c"))
        self.assertEqual(ls.index("b"), harray.index("b"))
        self.assertEqual(ls.index("a"), harray.index("a"))

        # Insert into the end
        ls = ["a", "b", "c"]
        harray = HashedList(ls)
        ls.insert(3, "Z")
        harray.insert(3, "Z")
        self.assertEqual(ls, harray)
        self.assertEqual(ls.index("Z"), harray.index("Z"))
        self.assertEqual(ls.index("c"), harray.index("c"))
        self.assertEqual(ls.index("b"), harray.index("b"))
        self.assertEqual(ls.index("a"), harray.index("a"))

    def test_remove(self):
        # Remove from the beginning
        ls = ["a", "b", "c"]
        harray = HashedList(ls)
        ls.remove("a")
        harray.remove("a")
        self.assertEqual(ls, harray)
        self.assertEqual(ls.index("c"), harray.index("c"))
        self.assertEqual(ls.index("b"), harray.index("b"))

        # Remove from the middle
        ls = ["a", "b", "c"]
        harray = HashedList(ls)
        ls.remove("b")
        harray.remove("b")
        self.assertEqual(ls, harray)
        self.assertEqual(ls.index("c"), harray.index("c"))
        self.assertEqual(ls.index("a"), harray.index("a"))

        # Remove from the end
        ls = ["a", "b", "c"]
        harray = HashedList(ls)
        ls.remove("c")
        harray.remove("c")
        self.assertEqual(ls, harray)
        self.assertEqual(ls.index("b"), harray.index("b"))
        self.assertEqual(ls.index("a"), harray.index("a"))

    def test_pop(self):
        # Pop from the beginning
        ls = ["a", "b", "c"]
        harray = HashedList(ls)
        value_ls = ls.pop(0)
        value_harray = harray.pop(0)
        self.assertEqual(ls, harray)
        self.assertEqual(value_ls, value_harray)
        self.assertEqual(ls.index("c"), harray.index("c"))
        self.assertEqual(ls.index("b"), harray.index("b"))

        # Pop from the middle
        ls = ["a", "b", "c"]
        harray = HashedList(ls)
        value_ls = ls.pop(1)
        value_harray = harray.pop(1)
        self.assertEqual(ls, harray)
        self.assertEqual(value_ls, value_harray)
        self.assertEqual(ls.index("c"), harray.index("c"))
        self.assertEqual(ls.index("a"), harray.index("a"))

        # Pop from the end
        ls = ["a", "b", "c"]
        harray = HashedList(ls)
        value_ls = ls.pop()
        value_harray = harray.pop()
        self.assertEqual(ls, harray)
        self.assertEqual(value_ls, value_harray)
        self.assertEqual(ls.index("b"), harray.index("b"))
        self.assertEqual(ls.index("a"), harray.index("a"))

    def test_clear(self):
        ls = ["a", "b", "c"]
        harray = HashedList(ls)

        ls.clear()
        harray.clear()
        self.assertEqual(ls, harray)
        with self.assertRaises(ValueError) as context_ls:
            ls.index("a")
        with self.assertRaises(ValueError) as context_harray:
            harray.index("a")
        self.assertEqual(context_harray.exception.args, context_ls.exception.args)

    def test_count(self):
        ls = ["c", "b"]
        harray = ["c", "b"]
        self.assertEqual(ls.count("c"), harray.count("c"))
        self.assertEqual(ls.count("b"), harray.count("b"))

    def test_sort(self):
        ls = ["c", "b", "1"]
        harray = ["c", "b", "1"]

        ls.sort()
        harray.sort()

        self.assertEqual(ls, harray)
        self.assertEqual(ls.index("1"), harray.index("1"))
        self.assertEqual(ls.index("b"), harray.index("b"))
        self.assertEqual(ls.index("c"), harray.index("c"))

    def test_reverse(self):
        ls = ["b", "c", "1"]
        harray = ["b", "c", "1"]

        ls.reverse()
        harray.reverse()

        self.assertEqual(ls, harray)
        self.assertEqual(ls.index("1"), harray.index("1"))
        self.assertEqual(ls.index("b"), harray.index("b"))
        self.assertEqual(ls.index("c"), harray.index("c"))


class TestUnique(unittest.TestCase):
    """Assert that HashedArray supports only unique values"""

    def test_not_unique(self):
        # HashedList only support unique items
        with self.assertRaises(DuplicateValueError) as context:
            HashedList([1, 2, 3, 3])
        self.assertEqual(context.exception.args, ("Duplicate values in HashedList",))

    def test_setitem__duplicate(self):
        ls = [1, 10, 22, -1]
        harray = HashedList(ls)

        with self.assertRaises(DuplicateValueError) as context:
            harray[0] = 10
        self.assertEqual(context.exception.args, ("Duplicate values in HashedList",))

    def test_append__duplicate(self):
        harray = HashedList(["a", "b", "c"])

        with self.assertRaises(DuplicateValueError) as context:
            harray.append("a")
        self.assertEqual(context.exception.args, ("Duplicate values in HashedList",))

    def test_extend__duplicate(self):
        harray = HashedList(["a", "5", "-1"])

        with self.assertRaises(DuplicateValueError) as context:
            harray.extend(["1", "5"])
        self.assertEqual(context.exception.args, ("Duplicate values in HashedList",))

    def test_insert__duplicate(self):
        harray = HashedList([1, 2, 10])
        with self.assertRaises(DuplicateValueError) as context:
            harray.insert(0, 2)
        self.assertEqual(context.exception.args, ("Duplicate values in HashedList",))


if __name__ == "__main__":
    unittest.main()
