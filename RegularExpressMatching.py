# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:06:41 2022

@author: YuanYi
"""
def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    iStrLen = len(s)
    iPatternLen = len(p)
    # asume has no . or *
    '''
    for iSub_s in range(0,iStrLen):
        #for iSub_p in range(0,len(p)):
        if s[iSub_s:iSub_s + iPatternLen] == p:
            return True
        else:
            iSub_s +=1
            continue
    return False    
    '''
    '''
    目前支持s部分匹配p，
        缺陷：*目前程序需要某字符至少出现一次，题目要求0次也可以。
    题目要求s完整匹配p
    '''
    print("s=",s)
    print("p=",p)
    lastChar = ""
    bJumpFlow = False
    iSub_s = 0
    #for iSub_s in range(0,iStrLen-iPatternLen+1):
    while iSub_s < (iStrLen - iPatternLen +1):
        #bJumpFlow = False
        print("s[",iSub_s ,":", iSub_s+iPatternLen,"]",s[iSub_s:iSub_s + iPatternLen])
        bFlag = True
        iSub_p=0
        lastChar = p[0]
        
        while iSub_p < iPatternLen:
        #for iSub_p in range(0,iPatternLen):
            print("\ts[",iSub_s ,"+", iSub_p,"]",s[iSub_s + iSub_p],"<===>",p[iSub_p])
            if (iSub_p+1 < iPatternLen) and ("*" == p[iSub_p+1]):
                #pass
                bJumpFlow = True
                break
            elif (s[iSub_s + iSub_p] == p[iSub_p]) or ("."== p[iSub_p]):
                #iSub_p += 1
                bFlag = True
                bJumpFlow = False
                if iSub_p == iPatternLen-1:
                    return True
                #lastChar = p[iSub_p]
                #pass
            elif ("*" == p[iSub_p]) and (lastChar == s[iSub_s + iSub_p]):
                if iSub_p == iPatternLen-1:
                    return True
                lastChar = p[iSub_p]
                continue
            else:
                bFlag = False
                bJumpFlow = True
                break
            
            lastChar = p[iSub_p]
            iSub_p +=1
        iSub_s += 1
    return bFlag
 

isMatch(s="abbcdefghij",p="bb*")