# [↗️ Remove Duplicates From Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

### 📚 Topics: Array, Two Pointers

### 🎯 Goal:

You're given:
- A sorted array `nums` (non-decreasing order)
- You have to **remove duplicates**, in-place (without using extra space)
- Keep only **unique elements**, and keep their **original order**
- Return `k`, the **count of unique elements**
- Also make sure that the **first `k` elements** of the array `nums` contain those unique values

⚠️ Anything after the first `k` elements doesn’t matter! You can ignore them — they won’t be checked.

### 🧪 Examples
- **✅ Example 1:** <br>
**Input:** `nums = [1, 1, 2]` <br>
**Output:** `k = 2`, `nums = [1, 2, _]` <br>
**Explanation:** <br>
    - Remove duplicate 1 
    - First k=2 elements should be: [1, 2]
    - The rest can be anything (e.g. _, garbage)

- **✅ Example 2:** <br>
**Input:** `nums = [0,0,1,1,1,2,2,3,3,4]` <br>
**Output:** `k = 5`, `nums = [0,1,2,3,4,_,_,_,_,_]` <br>
**Explanation:** <br>
    - Remove extra `0`s, `1`s, `2`s, etc.
    - First 5 unique values should stay in order: `[0, 1, 2, 3, 4]`

### ⚙️ How It Will Be Checked:
LeetCode's judge will test your code like this:

```java
int k = removeDuplicates(nums);  // 🧠 Your function is called

assert k == expectedNums.length; // ✅ k must match expected length

for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];  // ✅ All first k elements must match
}
```

### 🚀 Constraints
- Length of `nums`: `1 <= nums.length <= 30,000`
- Values range from `-100` to `100`
- `nums` is already **sorted**

### 🔑 In Short:
- Remove duplicate values from the sorted array **in-place**, return how many unique values (`k`) there are, and make sure the **first `k` values** in the array are those unique values — in the same order as they appeared.