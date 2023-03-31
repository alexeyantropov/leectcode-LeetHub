class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # There is a solution based on articles 'Queue and BFS' & 'BFS - Template'.
        # Main idea is inqueing and dequeing suitable elements from the grid into queue.
        # If an element is a land and the element isn't visited before then
        # we coud run a loop (dequeue) and check neighbour elememts (inqueue or skip
        # by the same rule as for the element).
        # Time compexity is O(n*m), the algo should check all elements.
        # space comp. is O(n*m), for the 'visited' list. 
        
        # Initial variables and buffers.
        m, n = len(grid), len(grid[0])
        queue, ret, visited = list(), 0, set()
        # A helper for build neighobur elements list.
        neighoburs_addrs = [[-1,0], [+1,0], [0,-1], [0, +1]]
        for i in range(m):
            for j in range(n):
                # Check a element: land/water and is/isn't visited.
                if grid[i][j] == '0' or (i,j) in visited:
                    continue
                # If the element is not visited before country then start BFS.
                visited.add((i,j))
                queue.append([i,j])
                while len(queue) > 0:
                    point = queue.pop(0) # dequeue an element
                    for neighobur_addr in neighoburs_addrs:
                        [h,v] = [x+y for x,y in zip(point, neighobur_addr)]
                        if 0 <= h < m and 0 <= v < n and (h,v) not in visited and grid[h][v] == '1':
                            queue.append([h,v])
                            visited.add((h,v)) # inqueue new suitable elements
                # All elements have been checked, it can increment a counter.
                ret += 1
        return(ret)
            
        