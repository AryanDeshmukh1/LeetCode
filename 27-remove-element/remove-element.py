class Solution(object):
    def removeElement(self, nums, val):

        k = 0  # Position for the next valid element

        for i in range(len(nums)):  # Check every element

            if nums[i] != val:  # Is this element valid?

                nums[k] = nums[i]  # Copy it to the front

                k += 1  # Move writer to the next position

        return k  # Return the number of valid elements