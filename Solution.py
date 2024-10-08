from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)  # Get the length of the input list 'nums'

        # Recursive function to check if we can reach the last index
        def traverse(index: int) -> bool:
            if index == n - 1:  # If we reached the last index, return True
                return True
            
            if nums[index] == 0:  # If current index has a jump of 0, we cannot proceed
                return False

            # Try all possible jumps from the current index
            for steps in range(1, nums[index] + 1):
                # Recursively check if we can reach the end from the next index
                if traverse(index + steps):
                    return True  # If we can reach the end, return True

            return False  # If no valid jumps lead to the end, return False
        
        return traverse(0)  # Start the traversal from the first index

# Time Complexity: O(2^n) in the worst case due to the exponential number of recursive calls.
# Space Complexity: O(n) due to the recursive call stack depth (maximum depth of n in the worst case).