# Exploring Four Approaches to the Jump Game Problem: A Comprehensive Analysis

- ## Solution 1: Recursion (Time Limit Exceeded)

    - ### Intuition
        - The goal is to determine if you can jump from the first index of an array to the last index, using the values in the array as the maximum jump length at each position. 

    - ### Approach
        1. Use a recursive function `traverse` to explore all possible jumps from the current index.
        2. If the current index is the last index, return `True`.
        3. If the current index has a jump of 0, return `False`.
        4. Iterate through all possible jumps from the current index and recursively check if any jump can lead to the last index.
        5. If any jump is valid, return `True`. If none are valid, return `False`.

    - ### Time Complexity
        - <code>O(2<sup>n</sup>)</code> in the worst case due to the exponential number of recursive calls.

    - ### Space Complexity
        - `O(n)` due to the recursive call stack depth (maximum depth of n in the worst case).

    - ### Code
        ```python3 []
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
        ```
    <hr>

- ## Solution 2: Using Memoization (Time Limit Exceeded)
    - ### Intuition
        - The problem is to determine if you can jump from the first index of an array to the last index using the values in the array, which represent the maximum jump lengths at each position.

    - ### Approach
        1. Define a recursive function `traverse` to explore possible jumps from the current index.
        2. If the current index is the last index, return `True`.
        3. Use a list `is_Traverse_Possible` to track which indices can reach the end, avoiding redundant checks.
        4. For each index, check if you can make a jump to any subsequent index and recursively verify if that index can reach the last index.
        5. If a jump leads to the last index, mark the current index as reachable. Otherwise, mark it as not reachable.
    
    - ### Time Complexity
        - `O(n²)` in the worst case, since each index may lead to multiple recursive calls, but memoization reduces redundant calculations.
    
    - ### Space Complexity
        - `O(n)` due to the recursive call stack depth and the additional space used by the `is_Traverse_Possible` list.

    - ### Code
        ```python3 []
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
        ```
    <hr>

- ## Solution 3:- Dynamic Programming
    - ### Intuition
        - The objective is to determine if you can jump from the first index of the array to the last index. Each element in the array indicates the maximum jump length from that position.

    - ### Approach
        1. Create a dynamic programming array `dp`, where each index indicates whether the end can be reached from that position.
        2. Initialize the last index of `dp` to `True`, as you can always reach the last index from itself.
        3. Iterate backward through the array, checking possible jumps from each index.
        4. For each index, check if you can jump to any of the reachable indices. Update `dp[index]` accordingly.
        5. If `dp[index]` becomes `True`, exit the inner loop as no further checks are needed.
    
    - ## Time Complexity
        - `O(n²)` in the worst case, due to the nested loops where each index checks possible jumps.
    
    - ## Space Complexity
        - `O(n)` due to the `dp` array used to store reachability from each index.

    - ### Code
        ```python
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
        ```
    <hr>
    
- ## Solution 4: Greedy
    - ### Intuition
        -The goal is to determine if you can jump from the first index of the array to the last index, using the values in the array as the maximum jump lengths at each position.

    - ### Approach
        1. Initialize a variable `farthest_Distance_Covered` to track the farthest index that can be reached.
        2. Iterate through each index of the array:
            - If the current index is greater than `farthest_Distance_Covered`, return `False` (not reachable).
            - Update `farthest_Distance_Covered` with the maximum of its current value and the distance that can be covered from the current index.
            - If `farthest_Distance_Covered` reaches or exceeds the last index, return `True`.
        3. If the loop completes without reaching the last index, return `False`.

    - ### Time Complexity
        - `O(n)` since we iterate through the `nums` list once.

    - ### Space Complexity
        - `O(1)` as we only use a constant amount of extra space (for `farthest_Distance_Covered`).

    - ### Code
        ```python3 []
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
        # Space Complexity: O(1) as we only use a constant amount of extra space (farthest_Distance_Covered).
        ```