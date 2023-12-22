class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        distance_value = 0
        for a in arr1:
            invalid = False
            for b in arr2:
                absolute = abs(a-b)
                if absolute <= d:
                    invalid = True
            if invalid:
                distance_value = distance_value - 1
            distance_value += 1    
        return distance_value
