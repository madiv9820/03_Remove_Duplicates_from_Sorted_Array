from typing import List

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        n: int = len(nums)       # Get the length of the array
        current_index: int = 0   # Start from the first element

        # Loop until the second last element
        while current_index + 1 < n:
            # If current and next elements are the same, it's a duplicate
            if nums[current_index] == nums[current_index + 1]:
                # Shift all elements to the left by one from the duplicate onwards
                for index in range(current_index + 1, n): nums[index - 1] = nums[index]
                n -= 1  # Reduce the size of the array since one duplicate is "removed"
                # Don't move the current_index forward yet, 
                # because the new value at this position needs to be checked again
            else: current_index += 1 # If current and next are different, move to the next index

        # Return the new length of the array after removing duplicates
        return n