
class Solution(object):
    def plusOne(self, digits):
        
        # Traverse the array from right to left
        for i in range(len(digits) - 1, -1, -1):

            # If the current digit is less than 9
            if digits[i] < 9:

                # Increment the digit by 1
                digits[i] += 1

                # Return the updated array
                return digits

            # If the digit is 9, change it to 0
            # Carry 1 to the previous digit
            digits[i] = 0

        # If all digits were 9, add 1 at the beginning
        return [1] + digits
