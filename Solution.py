from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)  # Get the length of the input list 'nums'
        is_Traverse_Possible = [False] * n  # Initialize a list to track reachable indices

        # Recursive function to check if we can reach the last index
        def traverse(index: int) -> bool:
            if index == n - 1:  # If we reached the last index, return True
                return True
            
            if is_Traverse_Possible[index]:  # If this index is already known to be reachable, return True
                return True
            
            if nums[index] == 0:  # If current index has a jump of 0, we cannot proceed
                return False

            # Try all possible jumps from the current index
            for steps in range(1, nums[index] + 1):
                # Recursively check if we can reach the end from the next index
                if traverse(index + steps):
                    is_Traverse_Possible[index] = True  # Mark this index as reachable
                    break  # Exit the loop since we found a valid path
            
            else:
                is_Traverse_Possible[index] = False  # Mark this index as not reachable

            return is_Traverse_Possible[index]  # Return the reachability status of this index
        
        return traverse(0)  # Start the traversal from the first index

# Time Complexity: O(n^2) in the worst case, as each index may lead to multiple recursive calls, but with memoization,
# it avoids redundant calculations.
# Space Complexity: O(n) due to the recursive call stack depth and the space used by the is_Traverse_Possible list.