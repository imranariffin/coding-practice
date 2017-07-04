class Solution(object):
  def islandPerimeter(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid:
    	return 0
    
    m = len(grid)
    n = len(grid[0])
    ret = 0

    for i in range(m):
    	for j in range(n):
    		e = grid[i][j]
    		if e == 1:
    			for ii, jj in ((i-1, j),(i+1,j),(i,j-1),(i,j+1)):
    				is_margin = (
    					ii<0 or ii>=m or
    					jj<0 or jj>=n
    				)
    				ret += [0, 1][is_margin or grid[ii][jj]==0]

    return ret

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