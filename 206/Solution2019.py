class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SolutionIterative:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, node, next = None, head, None

        while node is not None:
            next = node.next

            node.next = prev

            prev = node
            node = next

        return prev


class SolutionRecursive:
    def reverseList(self, head: ListNode) -> ListNode:
        return self._reverse(None, head, None)

    def _reverse(self, prev: ListNode, node: ListNode, next: ListNode) -> ListNode:
        if node is None:
            return prev

        next = node.next
        node.next = prev
        prev = node
        node = next

        return self._reverse(prev, node, next)

