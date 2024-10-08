from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_Distance_Covered = 0  # Initialize the farthest index that can be reached

        # Iterate through each index in the nums list
        for index in range(len(nums)):
            # Check if the current index is reachable
            if index > farthest_Distance_Covered:
                return False  # If we cannot reach this index, return False
            
            # Update the farthest index we can reach from the current index
            current_Distance_Covered = index + nums[index]
            farthest_Distance_Covered = max(farthest_Distance_Covered, current_Distance_Covered)

            # If the farthest index reaches or exceeds the last index, return True
            if farthest_Distance_Covered >= len(nums) - 1:
                return True

        return False  # If we finish the loop without reaching the last index, return False

# Time Complexity: O(n) since we iterate through the nums list once.
# Space Complexity: O(1) as we only use a constant amount of extra space (farthest_Distance_Covered)