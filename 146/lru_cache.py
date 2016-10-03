class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, node):
        """
        push to the end of list
        """
        if self.tail != None:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            return

        self.tail = node
        self.head = node

    def pop(self):
        """
        pop the front of list
        """
        if self.head != None:
            ret = self.head            
            if self.head.next == None:
                self.tail = None
            self.head = self.head.next
            ret.next = None
            ret.prev = None
            return ret

        return None

    def kick(self, node):
        assert(node != None)
        if node.prev == None and node.next == None:
            return
        if node.next == None:
            return

        if node.prev == None:
            assert(node.next != None)
            self.head = node.next
            self.head.prev = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            node.next = None
            return

        # print "node.prev: ", node.prev
        # print "node.next: ", node.next
        # print "tail: ", self.tail
        # print "tail.prev: ", self.tail.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

        # print " ======== "
        # print "node.prev: ", node.prev
        # print "node.next: ", node.next
        # print "tail: ", self.tail
        # print "tail.prev: ", self.tail.prev

    def print_list(self):
        ret = []
        curr = self.head

        while curr != None:
            ret.append(curr.val)
            curr = curr.next

        print ret

class DoublyLinkedNode(object):
    def __init__(self, key, x):
        self.val = x
        self.key = key
        self.prev = None
        self.next = None

    def __str__(self):
        return "<{}>".format(self.val)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.n = capacity
        self.cache = dict()
        self.q = DoublyLinkedList()

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache.keys():
            return -1

        ret = self.cache[key]
        # update the linked list so that referenced node is push to the end
        self.q.kick(ret)
        return ret.val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        assert(self.n >= len(self.cache))

        if len(self.cache) == self.n:
            # evict
            least_recent = self.q.pop()
            # print [(item[0], item[0]) for item in self.cache.items()]
            # print "pop"
            # # self.cache.pop(least_recent.val, None)
            # print "del self.cache[{}]".format(least_recent.key)
            self.print_cache()
            print "======="
            self.q.print_list()
            print "======="
            print "======="

            del self.cache[least_recent.key]
            # print [(item[0], item[0]) for item in self.cache.items()]

        if key in self.cache.keys():
        #     temp = self.cache[key]
            return

        node = DoublyLinkedNode(key, value)
        self.q.push(node)
        self.cache[key] = node

    def print_cache(self):
        for k, v in self.cache.items():
            print "[ {} -->  {} ]".format(k, v)

# if __name__=="__main__":

    # cache = LRUCache(1)
    # 1,[set(2,1),get(2),set(3,2),get(2),get(3)]
    # cache.set(2, 1)
    # cache.get(2)
    # cache.set(3, 2)
    # cache.get(2)
    # cache.get(3)
    # cache.print_cache()
    # print cache.get(1)

    # # for i in range(15):
    # #     cache.set(i, i)

    # cache.print_cache()

    # cache = LRUCache(10)
    # ret = [cache.set(10,13),cache.set(3,17),cache.set(6,11),cache.set(10,5),cache.set(9,10),cache.get(13),cache.set(2,19),
    # cache.get(2),cache.get(3),cache.set(5,25),cache.get(8),cache.set(9,22),cache.set(5,5),cache.set(1,30),cache.get(11),
    # cache.set(9,12),cache.get(7),cache.get(5),cache.get(8),cache.get(9),cache.set(4,30),cache.set(9,3),cache.get(9),cache.get(10),
    # cache.get(10),cache.set(6,14),cache.set(3,1),cache.get(3),cache.set(10,11),cache.get(8),cache.set(2,14),cache.get(1),
    # cache.get(5),cache.get(4),cache.set(11,4),cache.set(12,24),cache.set(5,18),cache.get(13),cache.set(7,23),cache.get(8),
    # cache.get(12),cache.set(3,27),cache.set(2,12),cache.get(5),cache.set(2,9),cache.set(13,4),cache.set(8,18),cache.set(1,7),
    # get(6),set(9,29),set(8,21),get(5),set(6,30),set(1,12),get(10),set(4,15),
    # set(7,22),set(11,26),set(8,17),set(9,29),get(5),set(3,4),set(11,30),
    # get(12),set(4,29),get(3),get(9),get(6),set(3,4),get(1),get(10),
    # set(3,29),set(10,28),set(1,20),set(11,13),get(3),set(3,12),set(3,8),
    # set(10,9),set(3,26),get(8),get(7),get(5),set(13,17),set(2,27),set(11,15),
    # get(12),set(9,19),set(2,15),set(3,16),get(1),set(12,17),set(9,1),
    # set(6,19),get(4),get(5),get(5),set(8,1),set(11,7),set(5,2),set(9,28),
    # get(1),set(2,2),set(7,4),set(4,22),set(7,24),set(9,26),set(13,28),set(11,26)]

#     dll = DoublyLinkedList()
#     dll.


# [ 1 -->  <30> ]
# [ 2 -->  <19> ]
# [ 3 -->  <17> ]
# [ 4 -->  <30> ]
# [ 5 -->  <25> ]
# [ 6 -->  <11> ]x
# [ 9 -->  <10> ]
# [ 10 -->  <13> ]
# [ 11 -->  <4> ]
# [ 12 -->  <24> ]
# =======
# [ 1 -->  <30> ]
# [ 2 -->  <19> ]x
# [ 3 -->  <17> ]
# [ 4 -->  <30> ]
# [ 5 -->  <25> ]
# [ 7 -->  <23> ]
# [ 9 -->  <10> ]
# [ 10 -->  <13> ]
# [ 11 -->  <4> ]
# [ 12 -->  <24> ]
# =======
# [ 1 -->  <30> ]
# [ 3 -->  <17> ]
# [ 4 -->  <30> ]
# [ 5 -->  <25> ]
# [ 7 -->  <23> ]
# [ 9 -->  <10> ]
# [ 10 -->  <13> ]
# [ 11 -->  <4> ]
# [ 12 -->  <24> ]
# [ 13 -->  <4> ]
# =======
# [ 1 -->  <30> ]
# [ 3 -->  <17> ]
# [ 4 -->  <30> ]
# [ 5 -->  <25> ]
# [ 7 -->  <23> ]
# [ 8 -->  <18> ]
# [ 10 -->  <13> ]
# [ 11 -->  <4> ]
# [ 12 -->  <24> ]
# [ 13 -->  <4> ]
# =======