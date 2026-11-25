
class Solution(object):
    def twoSum(self, nums, target):
        """
        Find two numbers whose sum equals target.
        Return their indices.
        """

        # Step 1: Create an empty dictionary.
        # We will store numbers and their indices here.
        num_map = {}

        # Step 2: Loop through every number in the array.
        for i in range(len(nums)):

            # Step 3: Calculate the number we need
            # to reach the target.
            complement = target - nums[i]

            # Step 4: Check if we have already seen
            # the missing number in our dictionary.
            if complement in num_map:

                # If found, return the index of the
                # previous number and the current index.
                return [num_map[complement], i]

            # Step 5: If the missing number is not found,
            # save the current number and its index.
            num_map[nums[i]] = i

        # Step 6: Return an empty list if no solution exists.
        return []
