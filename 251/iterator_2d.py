class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        # self.size = sum([sum([1 for x in row]) for row in vec2d])
        assert(len(vec2d) != 0)

        self.m = vec2d
        self.i = 0
        self.j = 0

    def next(self):
        """
        :rtype: int
        """
        if self.j >= len(self.m[self.i])-1:
            self.j = 0
            self.i += 1
        else:
            self.j += 1
        i = self.i
        j = self.j

        # print (i, j),
        return self.m[i][j]

    def hasNext(self):
        """
        :rtype: bool
        """
        i = self.i
        j = self.j
        # last row, last column
        if i >= len(self.m)-1 and j >= len(self.m[i])-1:
            return False
        if j >= len(self.m[i])-1:
            k = i
            while k < len(self.m):
                if self.m[k] != []:
                    return True
                k += 1
                self.i = k
            return False
        return True

    def flatten(self, m):
        return [x for x in row for row in m]

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

if __name__=="__main__":
    m = [[y*10+x for x in range(10)] for y in range(10)]
    m = [[1, 2, 3], []]
    v = Vector2D(m)
    print v.m
    # print v.size
    while v.hasNext():
        e = v.next()
        print e,