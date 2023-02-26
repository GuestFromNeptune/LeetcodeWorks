# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:55:08 2022

@author: YuanYi
1480. 一维数组的动态和
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。

 

示例 1：

输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
示例 2：

输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
示例 3：

输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]
 

提示：

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
通过次数224,688提交次数276,596

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/running-sum-of-1d-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

来自 <https://leetcode.cn/problems/running-sum-of-1d-array/> 

"""
    

def anotherSum(nums):
    for i in range(1,len(nums)):
        print("i=",i,"nums[i]",nums[i])
        #if i > 0:
        nums[i]= nums[i-1]+nums[i]
    return nums

    

ListA=[1,2,3,4]


#ListB=runningSum(nums=ListA)
print("Input",ListA)
ListB = anotherSum(nums=ListA)
print("Output:",ListB,"\r")
print("   ")

ListA=[3,1,2,10,1]
print("Input",ListA)
ListB = anotherSum(nums=ListA)
print("Output:",ListB,"\r")
print("   ")

ListA=[1,1,1,1,1]
print("Input",ListA)
ListB = anotherSum(nums=ListA)
print("Output:",ListB,"\r")