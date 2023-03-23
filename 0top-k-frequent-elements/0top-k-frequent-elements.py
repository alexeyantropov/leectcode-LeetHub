class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # My approach is usigng two HashMaps for scoring frequency of each element
        # and placing elements on a scrore board by their frequence.
        # E.g. one HM has the primary order and second HM has the reversed order.
        scores, freqs, ret = dict(), dict(), list()
        for n in nums:
            if n in freqs:
                scores[freqs[n]].remove(n)
                freqs[n] += 1
            else:
                freqs[n] = 1
            if freqs[n] not in scores:
                scores[freqs[n]] = set()
            scores[freqs[n]].add(n)
        # Now it gets the variables like:
        # nums: [1,1,1,1,1,2,2,2,3,4], freqs: {1: 5, 2: 3, 3: 1, 4: 1}
        # scores: {1: set([3, 4]), 2: set([]), 3: set([2]), 4: set([]), 5: set([1])}
        # What is the fastest way to return the result? I think it could be an extra loop.
        for s in reversed(sorted(scores)):
            ret.extend(scores[s])
            if len(ret) == k:
                return(ret)
        return(-1) # If smth is wrong with the Constraints.