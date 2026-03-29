**Adding in multiple steps and loops to make it more understandable**

# Intuition
# Using hashing to bring time complexity to 0(n)
# Approach
# Using hashing
# Complexity
# Time complexity:
# O(n)
# Space complexity:
# O(n)
```
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        myHash = {}
        prefix_sum = [0] * (len(nums))
        prefix_sum[0] = nums[0]
        count = 0
        x = 0
        for i in range(1, len(nums)): # creating prefix sum array seperately
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        for j in range(0, len(prefix_sum)): # looping prefix sum and checking if x= prefix[sum] - k exists
            x = prefix_sum[j] - k
            if prefix_sum[j] == k: # if k found in prefix sum J-th index
                count += 1
            if x in myHash:      #else get the value for key x and add it in count
                count += myHash[x]
            myHash[prefix_sum[j]] = myHash.get(prefix_sum[j], 0) + 1 #  create/update myHash dict with prefix sum
        return count
```
