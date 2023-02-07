class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        greatest_element_num = 0
        greatest_element_val = arr[greatest_element_num]  
        for i in range(len(arr)-1):
            if greatest_element_num <= i:
                greatest_element_val = arr[i+1]
                for j in range(i+1, len(arr)):
                    if arr[j] >= greatest_element_val:
                        greatest_element_val = arr[j]
                        greatest_element_num = j
            arr[i] = greatest_element_val
            
        arr[-1] = -1
        return(arr)