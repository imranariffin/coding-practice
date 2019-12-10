import unittest

from Solution2019 import ListNode, SolutionIterative, SolutionRecursive


class TestIterative(unittest.TestCase):
    def setUp(self):
        self.s = SolutionIterative()

    def test(self):
        test_cases = [
                {
                    'input': '1->2->3->4->5->NULL',
                    'output': '5->4->3->2->1->NULL',
                },
                {
                    'input': 'NULL',
                    'output': 'NULL',
                },
                {
                    'input': '1->NULL',
                    'output': '1->NULL'
                }
        ]

        for test_case in test_cases:
            linked_list = deserialize(test_case['input'])
            want = test_case['output']

            got = serialize(self.s.reverseList(linked_list))

            assert got == want, f'"{got} != {want}"'


class TestRecursive(unittest.TestCase):
    def setUp(self):
        self.s = SolutionRecursive()

    def test(self):
        test_cases = [
                {
                    'input': '1->2->3->4->5->NULL',
                    'output': '5->4->3->2->1->NULL',
                },
                {
                    'input': 'NULL',
                    'output': 'NULL',
                },
                {
                    'input': '1->NULL',
                    'output': '1->NULL'
                }
        ]

        for test_case in test_cases:
            linked_list = deserialize(test_case['input'])
            want = test_case['output']

            got = serialize(self.s.reverseList(linked_list))

            assert got == want, f'"{got} != {want}"'


def deserialize(linked_list_str):
    nodes = [
            ListNode(val) if val != 'NULL'
            else None
            for val in linked_list_str.split('->')
    ]
    if not nodes:
        return None
    for i, node in enumerate(nodes):
        if i != len(nodes) - 1:
            node.next = nodes[i+1]
    return nodes[0]


def serialize(linked_list):
    values = []
    node = linked_list
    while node:
        values.append(str(node.val))
        node = node.next
    values.append('NULL')
    return '->'.join(values)

if __name__ == '__main__':
    unittest.main()

