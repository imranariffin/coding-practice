import heapq
import typing as t

from problem_2.utils import COLUMN_DEFAULTS, COLUMN_FACTORIES, ColumnNames, Row
from problem_2.peekable_file_iterator import PeekableFileIterator
from problem_2.utils import make_chunk_file_name


def get_min_row(heap_rows: t.List[t.Tuple[int, Row]], sort_columns: t.Tuple[ColumnNames, ...]) -> t.Tuple[int, Row]:
    heap = []
    normal_sort = []
    for chunk_id, row in heap_rows:
        sort_key = tuple(
            getattr(row, column_name.value)
            for column_name in sort_columns
        )
        heap.append((sort_key, (chunk_id, row)))
        normal_sort.append((sort_key, (chunk_id, row)))

    heapq.heapify(heap)

    return heapq.heappop(heap)[1]


def merge_chunks(
    base_ifile_name: str,
    chunk_ids: t.List[int],
    ofile_name: str,
    sort_columns: t.Tuple[ColumnNames, ...],
) -> None:
    heap_file_iterators: t.Dict[int, PeekableFileIterator] = {}

    for chunk_id in chunk_ids:
        heap_file_name = make_chunk_file_name(base_file_name=base_ifile_name, chunk_id=chunk_id)
        heap_file = open(heap_file_name, "r")
        heap_file_iterators[chunk_id] = PeekableFileIterator(file=heap_file)

    # Remove header lines from all heap files
    for chunk_id, heap_iter in heap_file_iterators.items():
        heap_iter.pop().rstrip("\n")

    with open(ofile_name, "w") as ofile:

        while any(heap_file_iterators.values()):
            empty_heaps = []
            top_heap_rows = []
            for chunk_id, heap_iter in heap_file_iterators.items():
                line = heap_iter.peek()
            
                if heap_iter.is_empty() or not line:
                    empty_heaps.append(chunk_id)
                    continue

                _row = Row(*line.rstrip("\n").split(","))
                row = Row(
                    *(
                        COLUMN_FACTORIES[column_name](getattr(_row, column_name)) or COLUMN_DEFAULTS[column_name]
                        for column_name in _row._fields
                    )
                )
                top_heap_rows.append((chunk_id, row))

            
            if not top_heap_rows:
                empty_heaps.append(chunk_id)
                for chunk_id in empty_heaps:
                    if chunk_id in heap_file_iterators:
                        del heap_file_iterators[chunk_id]
                continue

            min_chunk_id, min_heap_row = get_min_row(top_heap_rows, sort_columns)
            heap_file_iterators[min_chunk_id].next()
            
            ofile.write(",".join([str(row) for row in min_heap_row]) + "\n")
    

def _test():
    merge_chunks(
        base_ifile_name="./random_data.csv",
        # base_ifile_name="./large_data.csv",
        chunk_ids=[chunk_id for chunk_id in range(20)],
        ofile_name="./output.csv",
        sort_columns=(ColumnNames.DEVICE_ID,ColumnNames.DATE),
    )
