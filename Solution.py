from typing import List
from collections import Counter

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        counter: Counter = Counter(nums)    # 🧮 Count the frequency of each number in the list
        index: int = 0                      # ✍️ Index to place the next unique number

        # 🔁 Loop through each unique number (keys of the counter)
        for key in list(counter.keys()):
            # 📌 Place the unique number at the current index
            # 👉 Move to the next index
            nums[index], index = key, index+1  

        return len(counter)     # 🔢 Return the number of unique elements (length of the counter keys)