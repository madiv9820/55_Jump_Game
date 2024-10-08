# 55. Jump Game

__Type:__ Medium <br>
__Topics:__ Array, Dynamic Programming, Greedy <br>
__Companies:__ Amazon, Google, Microsoft, Bloomberg, tcs, Apple, Meta, Goldman Sachs, Cisco, TomTom, Verily, Walmart Labs, TikTok, Meesho, Adobe, Yahoo, Oracle, Uber, DoorDash, Salesforce, MakeMyTrip, Infosys, Flipkart, Morgan Stanley <br>
__Leetcode Link:__ [Jump Game](https://leetcode.com/problems/jump-game/description/)
<hr>

You are given an integer array `nums`. You are initially positioned at the array's __first index__, and each element in the array represents your maximum jump length at that position.<br><br>
Return `true` _if you can reach the last index, or_ `false` _otherwise_.
<hr>

### Examples

__Example 1:__

__Input:__ nums = [2,3,1,1,4] <br>
__Output:__ true <br>
__Explanation:__ Jump 1 step from index 0 to 1, then 3 steps to the last index.

__Example 2:__

__Input:__ nums = [3,2,1,0,4] <br>
__Output:__ false <br>
__Explanation:__ You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
<hr>

### Constraints:

- <code>1 <= nums.length <= 10<sup>4</sup></code>
- <code>0 <= nums[i] <= 10<sup>5</sup></code>