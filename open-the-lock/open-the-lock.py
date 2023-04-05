class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        state, visited, queue, turns = '0000', set(deadends), list(), 0
        queue.append([state, turns])
        # A corner case. When the initial state is '0000'.
        if state in visited:
            return(-1)
        while len(queue) > 0:
            state_ = queue.pop(0)
            state, turns = state_[0], state_[1]
            if state == target:
                return(turns)
            visited.add(state)
            for i in range(len(state)):
                on_wheel = int(state[i])
                for j in [-1, 1]:
                    on_wheel_new = str((on_wheel + j) % 10)
                    state_new = str(state[0:i] + on_wheel_new + state[1+i:len(state)])
                    #print('state: {}, i: {}, j: {}, state_new: {}'.format(state, i, j, state_new))
                    if state_new not in visited:
                        queue.append([state_new, turns + 1]) # (1)
                        visited.add(state_new)
        return(-1)  
        # 1: It saves a number of each steps connected to each possible next combinations
        # to return the shortest way for finding target.