class Solution(object):
  def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    s_all = set([v for v in range(numCourses)])
    v_to_neighbours = dict([(v, []) for v in range(numCourses)])

    for u, v in prerequisites:
      v_to_neighbours[u].append(v)

    # print v_to_neighbours

    visited = set()
    cur_path = set()
    for u in v_to_neighbours:
      # print u
      if u not in visited:
        if not self.dfs(u, visited, cur_path, v_to_neighbours):
          # print False
          return False
        cur_path.remove(u)

    # print True
    return True

  def dfs(self, u, visited, cur_path, v_to_neighbours):

    cur_path.add(u)
    visited.add(u)

    # print "cur_path:", cur_path

    for v in v_to_neighbours[u]:

      # print "%s.neighbour:"%u, v

      if v in cur_path:
        return False
      ret = self.dfs(v, visited, cur_path, v_to_neighbours)
      if not ret:
        return False
      cur_path.remove(v)

    return True

if __name__ == '__main__':

  s = Solution()
  
  print "TEST 0"
  n0, edges0 = 2, [[1, 0]]
  ret0 = s.canFinish(n0, edges0)
  print ret0
  assert ret0 == True
  print ""

  print "TEST 1"
  n1, edges1 = 2, [[1,0],[0,1]]
  ret1 = s.canFinish(n1, edges1)
  print ret1
  assert ret1 == False
  print ""

  print "TEST 2"
  n2, edges2 = 3, [[1,0],[0,2], [1, 2]]
  ret2 = s.canFinish(n2, edges2)
  print ret2
  assert ret2 == True
  print ""

  print "TEST 3"
  n3, edges3 = 4, [[0,1],[1,2],[2, 3],[3,1]]
  ret3 = s.canFinish(n3, edges3)
  print ret3
  assert ret3 == False
  print ""

  print "TEST 4"
  n4, edges4 = 7, [[1,2],[2,0],[3,5],[5,6],[6,4],[4,5]]
  ret4 = s.canFinish(n4, edges4)
  print ret4
  assert ret4 == False
  print ""

  