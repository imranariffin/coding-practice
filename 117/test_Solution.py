import unittest

from Solution import Solution, Node


class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def output(self, node: Node):
        out = []
        while node != None:
            nextNode = node
            while nextNode != None:
                out.append(nextNode.val)
                nextNode = nextNode.next
            out.append('#')
            node = node.left
        return out

    def test_one(self):
        node = Node(
                1,
                Node(
                    2,
                    Node(4),
                    Node(5),
                ),
                Node(
                    3,
                    None,
                    Node(7),
                ),
        )
        want = [1,'#',2,3,'#',4,5,7,'#']

        ret = self.s.connect(node)
        got = self.output(ret)

        assert got == want, f'{got} != {want}'


if __name__ == '__main__':
    unittest.main()

