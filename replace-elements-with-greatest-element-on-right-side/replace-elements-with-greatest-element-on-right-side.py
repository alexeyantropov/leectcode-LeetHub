class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # The vars greatest_element_* follow front Hint #2 
        greatest_element_num = 0
        greatest_element_val = arr[greatest_element_num]  
        for i in range(len(arr)-1):
            # Next condition saves time by reducing O(n-i) extra lookups for the maximum value.
            # It really usefull when list like [1,2,3,4,<many values>,9999,1,2,3]. The IF condition will skipp these <many values>.
            if greatest_element_num > i:
                arr[i] = greatest_element_val
                continue
            # If the code have passed through an index of the former maximum value it has to find a new one.
            greatest_element_val = arr[i+1]
            for j in range(i+1, len(arr)):
                if arr[j] >= greatest_element_val:
                    greatest_element_val = arr[j]
                    greatest_element_num = j
            arr[i] = greatest_element_val
            
        arr[-1] = -1
        return(arr)