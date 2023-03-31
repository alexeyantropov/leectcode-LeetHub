class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        queue, ret, visited = list(), 0, set()
        neighoburs_addrs = [[-1,0], [+1,0], [0,-1], [0, +1]]
        for i in range(m):
            for j in range(n):
                #print('* Point: [{},{}], val: {}'.format(i, j, grid[i][j]))
                #print('* Visited: {}'.format(visited))
                if grid[i][j] == '0' or (i,j) in visited:
                    #print('* A point [{},{}] is in visited or empy.'.format(i, j))
                    continue
                visited.add((i,j))
                queue.append([i,j])
                while len(queue) > 0:
                    #print('** Queue In: {}'.format(queue))
                    point = queue.pop(0)
                    #print('** Point: {}'.format(point))
                    for neighobur_addr in neighoburs_addrs:
                        [h,v] = [x+y for x,y in zip(point, neighobur_addr)]
                        #print('*** Possible N: [{},{}]'.format(h, v))
                        if 0 <= h < m and 0 <= v < n and (h,v) not in visited and grid[h][v] == '1':
                            queue.append([h,v])
                            visited.add((h,v))
                            #print('*** Possible N: [{},{}] is added'.format(h, v))
                    #print('** Queue Out: {}'.format(queue))
                ret += 1
                #print('---')
        return(ret)
            
        