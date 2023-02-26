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

    print("s=",s)
    print("p=",p)
    lastChar = ""
    bOutterFlag = True
    bInnerFlag = ""
    iSub_s = 0
    iSub_p=0
    if p == "" and s != "" :
        return True
    #for iSub_s in range(0,iStrLen-iPatternLen+1):
        #应改为用动态规划DP做，例如递归
    while iSub_s < (iStrLen):
        #bJumpFlow = False
        #print("s[",iSub_s ,":", iSub_s+iPatternLen,"]",s[iSub_s:iSub_s + iPatternLen],"compare to PATTERN:",p)
        print("s[",iSub_s ,":]",s[iSub_s:],"compare to PATTERN:",p)
        #bInnerFlag = False #本题要求全字符串匹配，所以此处不必清空
        #lastChar = ""#p[0]
        #iSub_p=0
        if ("*" == p[iSub_p]):
            #pass
            bInnerFlag = True
            bOutterFlag = True
            #iSub_s += 1
            lastChar = p[iSub_p-1]
        else:
            lastChar = p[iSub_p]
        
        while iSub_p < iPatternLen:
        #for iSub_p in range(0,iPatternLen):
            
            if (iSub_p < iPatternLen-1) and ("*" == p[iSub_p+1]):
                print("p[",iSub_p+1,"] is ",p[iSub_p+1],"|||iSub_p <iPatternLen-1",iSub_p, "?less than?",iPatternLen-1)
                if isMatch(s[iSub_s + iSub_p:],p[iSub_p+2:]) == True:
                    print("isMatch(s[iSub_s + iSub_p:],p[iSub_p+2:])")
                    return True
                elif isMatch(s[iSub_s + iSub_p+1:],p[iSub_p+2:]) == True:
                    print("isMatch(s[iSub_s + iSub_p+1:],p[iSub_p+2:])")
                    if s[iSub_s + iSub_p] == p[iSub_p]:
                        return True
                    else:
                        return False
                else:
                    return False
               
            if ("*" == p[iSub_p]):
                #pass
                bInnerFlag = True
                bOutterFlag = True
                #iSub_s += 1
                lastChar = p[iSub_p-1]
            else:
                lastChar = p[iSub_p]
            
            print("\ts[",iSub_s ,"+", iSub_p,"]",s[iSub_s + iSub_p],"<===>p[",iSub_p,"]:",p[iSub_p],"<=lastchar==>",lastChar)
                
            if ((s[iSub_s + iSub_p] == lastChar) or ("." == lastChar)):
                bInnerFlag = True
                bOutterFlag = False
                
                if (iSub_p == iPatternLen-1) and (iSub_p + iSub_s == iStrLen -1):
                    return True
            else:
                bInnerFlag = False
                bOutterFlag = True
                break

            iSub_p += 1
            
            #if (iSub_s + iSub_p) > iStrLen -1:
            #    print("(iSub_s + iSub_p) > iStrLen -1, returning False!")
            
            if (iSub_p > iPatternLen -1) or (iSub_s >iStrLen-1):
                print("iSub_p (",iSub_p,") > iPatternLen(",iPatternLen,") -1, returning False!")
                return False
            
            '''
            if (iSub_p > iPatternLen -1):
                lastChar = ""
                bInnerFlag = False
                return False
            elif ("*" == p[iSub_p]):
                #pass
                bInnerFlag = True
                bOutterFlag = True
                #iSub_s += 1
                lastChar = p[iSub_p-1]
            else:
                lastChar = p[iSub_p]
            '''
        iSub_s += 1
    return bInnerFlag
 
#print(isMatch(s="abbcdefghij",p="abbcde"))
#print(isMatch(s="abbcdefghij",p="abbcde*fghij"))
#print(isMatch(s="missssip",p="mis*ip."))
#(isMatch(s="aa",p="a"))
#print(isMatch(s="mississippi",p="mis*is*ip*."))
print(isMatch(s="issippk",p="is*ip*."))
#print(isMatch(s="aa",p="a"))
