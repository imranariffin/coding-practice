from itertools import product

class Solution(object):
  def islandPerimeter(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    visited = set()
    q = []
    ret = 0

    ls_ij = product(range(len(grid)), range(len(grid[0])))
    for i, j in ls_ij:
      e = grid[i][j]
      if e == 1:
        q.append((i, j))
        print q
        break
    if not q:
      return 0
        
    while q:
      i, j = q.pop(0)
      visited.add((i, j))
      ls_adj = self.adjacents(grid, i, j)

      for i_adj, j_adj in ls_adj:
        if (i_adj, j_adj) not in visited:
          is_margin = (
            i_adj < 0 or i_adj >= len(grid) or
            j_adj < 0 or j_adj >= len(grid[0])
          )
          if is_margin:
            ret += 1
          elif grid[i_adj][j_adj] == 0:
            ret += 1
          else:
            visited.add((i_adj, j_adj))
            q.append((i_adj, j_adj))

          # print "@", i, j, "; adj:", i_adj, j_adj, "ret", ret

    return ret

  def adjacents(self, grid, i, j):
    return [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]

if __name__ == '__main__':
  s = Solution()

  print "TEST 0"
  grid0 = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
  ]
  for row in grid0: print row
  ret0 = s.islandPerimeter(grid0)
  print ret0
  assert ret0 == 16

  print "TEST 1"
  grid1 = [
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
  ]
  for row in grid1: print row
  ret1 = s.islandPerimeter(grid1)
  print ret1
  assert ret1 == 16

  print "TEST 2"
  grid2 = [
    [1,1,1,1],
    [1,0,0,0],
    [1,0,0,1],
    [1,1,1,1]
  ]
  for row in grid2: print row
  ret2 = s.islandPerimeter(grid2)
  print ret2
  assert ret2 == 24