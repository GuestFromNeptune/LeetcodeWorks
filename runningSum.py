# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:58:27 2022

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
#class Solution(object):
def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    rNums= [0]*len(nums)
    for i in range(0,len(nums)):
        print ("i=",i)
        iSum = 0 
        for j in range(0,i+1):
            print("    ","j=",j)
            iSum = iSum +nums[j]   
        rNums[i] =iSum
         
    return rNums

#不能用i,j作为指标，反查位置
#否则如果数字全部是1，他只匹配第一个位置
'''
    for i in nums:
        iSum = 0 
        for j in nums:
            if nums.index(j) <= nums.index(i):
                iSum = iSum + j
            else:
                break
        rNums[nums.index(i)] =iSum
       # continue
'''


#ListA=[1,2,3,4]
#ListB=runningSum(nums=ListA)

#ListC = [2,4,6,8]
#ListD=runningSum(nums=ListC)

ListA=[1,2,3,4]
ListB=runningSum(nums=ListA)
ListB
