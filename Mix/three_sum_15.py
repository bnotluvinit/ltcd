import unittest


def solution(nums):
    nums.sort()
    n = len(nums)
    triplets = list()

    # Loop for each char in array
    for i in range(0, n):
        # Avoid dupes
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # left and right pointers
        j = i + 1
        k = n - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                triplets.append([nums[i], nums[j], nums[k]])
                j +=1
                while j < k and nums[j] == nums[j - 1]:
                    j +=1
            elif nums[i] + nums[j] + nums[k] < 0:
                j +=1
            else:
                k -= 1
    return triplets


class Test(unittest.TestCase):

    def test_1(self):
        nums = [-1,0,1,2,-1,-4]
        expected_result = [[-1,-1,2],[-1,0,1]]
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)

    def test_2(self):
        nums = [0]
        expected_result = []
        actual_result = solution(nums)
        self.assertEqual(expected_result, actual_result)
