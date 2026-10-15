



class Solution (object):
        def twoSum(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
           

            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]
                    
nums_input = input("Enter numbers separated by commas (e.g., 1,2,3,4,5): ")
nums = [int(x) for x in nums_input.split(",")]

target = int(input("Enter target value: "))


solution = Solution()
result = solution.twoSum(nums, target)
print(result)
    