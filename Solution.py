from typing import List

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        actual_index: int = 0   # 📌 actual_index keeps track of where to place the next unique element
        current_index: int = 0  # 🚶 current_index scans through the array to find unique elements
        length: int = len(nums) # 📏 Store the length of the array
        
        # 🔁 Loop until we've checked all elements
        while current_index < length:
            next_index: int = current_index + 1     # 🔍 next_index looks ahead to skip all duplicates
            while (next_index < length and nums[current_index] == nums[next_index]):
                next_index += 1     # 👉 Skip over duplicates

            nums[actual_index] = nums[current_index]    # ✏️ Write the unique element to the correct position
            actual_index, current_index = actual_index+1, next_index    # ➕ Move both pointers forward
            
        return actual_index     # 🎯 Return the number of unique elements