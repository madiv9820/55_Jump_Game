from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)  # Get the length of the input list 'nums'
        dp = [False] * n  # Initialize a list to track if we can reach the end from each index
        dp[n-1] = True  # The last index is reachable from itself

        # Iterate backwards from the second-to-last index to the first index
        for index in range(n - 2, -1, -1):
            # Check all possible jumps from the current index
            for step in range(1, nums[index] + 1):  # Corrected range to include the maximum steps
                next_Index = index + step  # Calculate the next index to jump to
                if next_Index < n:  # Ensure the next index is within bounds
                    dp[index] = dp[index] or dp[next_Index]  # Update the dp value for the current index
                if dp[index]:  # If we can reach the end from this index, no need to check further
                    break

        return dp[0]  # Return the reachability status from the first index

# Time Complexity: O(n^2) in the worst case due to the nested loops where each index checks possible jumps.
# Space Complexity: O(n) due to the dp array used to store reachability from each index.