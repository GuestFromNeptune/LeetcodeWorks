# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:13:47 2022

@author: YuanYi
"""

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    inStr = str(x)
    revStr = "".join(reversed(inStr))
    revStr = inStr[::-1]
    return (inStr == revStr)

def isPalindrome1(x):
    """
    :type x: int
    :rtype: bool
    自行两端开始比较，效率提高一些。
    """
    inStr = str(x)
    iLen = len(inStr)
    for i in range(0,int(iLen/2)):
        if inStr[i] != inStr[iLen-1-i] :
            return False
    return True

def isPalindrome2(x):
    '''
    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
        without convert x into a String
    Returns
    -------
    bool
        DESCRIPTION.

    '''
    if x < 0:
        return False
    lixt = []
    tmpX = x
    iLen = 0
    #singleDit = tmpX % 10
    while tmpX > 0:
        singleDit = tmpX % 10
        tmpX = int(tmpX / 10)
        print("singleDit:",singleDit,"tmpX:",tmpX)
        lixt.append(singleDit)
        iLen +=1
    print(lixt)
    print("iLen=",iLen)
    
    while iLen > 1:
        if(lixt.pop(0) != lixt.pop(-1)):
            return False
        else:
            iLen -=2
    return True
    
#    return lixt
    
#isPalindrome(x=121)

#isPalindrome1(121)
lista=isPalindrome2(12345)

'''
简单]9. Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
通过次数1,172,162提交次数2,064,392

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''