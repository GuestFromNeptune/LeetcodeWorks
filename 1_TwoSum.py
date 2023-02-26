# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 10:50:56 2022

@author: YuanYi

1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return [0,0]
    
ListA=[2,7,11,15]
aTarget = 9
print("Input nums=", ListA, "target=", aTarget)
print("Solution:", twoSum(nums=ListA, target=aTarget), "\n")

ListA=[3,2,4]
aTarget = 6
print("Input nums=", ListA, "target=", aTarget)
print("Solution:", twoSum(nums=ListA, target=aTarget), "\n")

ListA=[3,3]
aTarget = 6
print("Input nums=", ListA, "target=", aTarget)
print("Solution:", twoSum(nums=ListA, target=aTarget), "\n")


ListA=[1,3,2,6,4,8,9]
aTarget = 10
print("Input nums=", ListA, "target=", aTarget)
print("Solution:", twoSum(nums=ListA, target=aTarget), "\n")