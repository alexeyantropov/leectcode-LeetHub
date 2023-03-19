class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # The first idea. Time O(len(list1) + len(list2) + max(len(list1),len(list2)), space O(list1+list2)
        # The first loop fills words 
        helper = dict()
        ret = list()
        least_sum = len(list1) + len(list2) - 1
        for i in range(len(list1)):
            helper[list1[i]] = -i
        for i in range(len(list2)):
            if list2[i] in helper:
                helper[list2[i]] *= -1
                helper[list2[i]] += i
                least_sum = min(least_sum, helper[list2[i]])
        for k, v in helper.items():
            if v > -1 and v == least_sum:
                ret.append(k)
        return(ret)
        
        