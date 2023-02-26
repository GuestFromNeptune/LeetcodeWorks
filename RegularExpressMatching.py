# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 17:06:41 2022

@author: YuanYi
"""
import sys
def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    iStrLen = len(s)
    iPatternLen = len(p)

    print("s=",s)
    print("p=",p)
    lastChar = ""
    
    bOutterFlag = True
    bInnerJumpFlag = False
    bLastMatchFlag = False
    
    iSub_s = 0
    iSub_p=0
    if (p == "" and s != "") :
        print("L",sys._getframe().f_lineno,"(p == "" and s != "") return FALSE!")
        return False

    #应改为用动态规划DP做，例如递归
    while iSub_s < (iStrLen):

        if (bInnerJumpFlag == True) and (bLastMatchFlag == False):
            print("L",sys._getframe().f_lineno,"(bInnerJumpFlag == True) and (bLastMatchFlag == False)","return FALSE")
            return False
        try:
            print("L",sys._getframe().f_lineno,"s[",iSub_s + iSub_p ,":]",s[iSub_s + iSub_p:],"compare to PATTERN p[iSub_p]:",p[iSub_p:])
        except:
            print("L",sys._getframe().f_lineno,"s[",iSub_s," + ",iSub_p,":]","compare to PATTERN p[",iSub_p,":]")
            print("L",sys._getframe().f_lineno,"compare to PATTERN: FALSE!")
            return False
        
        #bInnerFlag = False #本题要求全字符串匹配，所以此处不必清空
        #lastChar = ""#p[0]
        #iSub_p=0
        
        while iSub_p < iPatternLen:
            try:
                print("L",sys._getframe().f_lineno,"\ts[",iSub_s ,"+", iSub_p,"]",s[iSub_s + iSub_p],"<===>p[",iSub_p,"]:",p[iSub_p],"<=lastchar==>",lastChar)
            except:
                print("L",sys._getframe().f_lineno,"\ts[iSub_s(",iSub_s ,")+(", iSub_p,")]","<===>p[",iSub_p,"]<=lastchar==>",lastChar)
            if (p[iSub_p:]=="" and s[iSub_s + iSub_p:]!=""):
                '''
                bLastMatchFlag = False
                bInnerJumpFlag = True
                '''
                print("L",sys._getframe().f_lineno,"return FALSE")
                return False
            try:
                print("L",sys._getframe().f_lineno,"currtent s goes to:",s[iSub_s + iSub_p])
            except:
                print("L",sys._getframe().f_lineno,"string index s out of range","return FALSE")
                return False
            
            try:
                print("L",sys._getframe().f_lineno,"currtent PATTERN goes to:",p[iSub_p])
            except:
                print("L",sys._getframe().f_lineno,"PATTERN index p out of range","return FALSE")
                return False
            
            #if ((s[iSub_s + iSub_p] == p[iSub_p]) or ("." == p[iSub_p])):
            if ((s[iSub_s + iSub_p] == p[iSub_p]) or ("." == p[iSub_p]) or ("." == lastChar) ):
                
                #1006加入
                print("L",sys._getframe().f_lineno,"s[iSub_s + iSub_p] == p[iSub_p]")
                print("L",sys._getframe().f_lineno,"\ts[",iSub_s ,"+", iSub_p,"]",s[iSub_s + iSub_p],"<===>p[",iSub_p,"]:",p[iSub_p],"<=lastchar==>",lastChar)
                lastChar = p[iSub_p]
                bInnerJumpFlag = False
                bLastMatchFlag = True
                
                #判断            #需要用新的判定方式
                if (s[iSub_s + iSub_p+1:]==""):  #s字符串走到最后
                    print("L",sys._getframe().f_lineno,"(s[iSub_s + iSub_p+1:]=="")")
                #--------------------    
                #if  (iSub_p + iSub_s  == iStrLen -1): #and (iSub_p + iSub_s == iStrLen -1):
                #    print("L",sys._getframe().f_lineno,"(iSub_p + iSub_s  == iStrLen -1)")
                    if (iSub_p < iPatternLen -2) :
                        if (p[iSub_p + 2] == "*"):
                            print("L",sys._getframe().f_lineno,"(p[iSub_p + 2] == *)","return TRUE")
                            return True
                        else:
                            print("L",sys._getframe().f_lineno,"(p[iSub_p + 2] != *)","return TRUE")
                            return False
                    elif (iSub_p == iPatternLen -2) and (p[iSub_p + 1] != "*"):
                        print("L",sys._getframe().f_lineno,"(p[iSub_p + 1] ==", p[iSub_p + 1],"return False")
                        return False
                    else:
                        print("L",sys._getframe().f_lineno,"(iSub_p + iSub_s  == iStrLen -1)","return TRUE")
                        bLastMatchFlag = True
                        return True
                elif  (p[iSub_p+1:]=="") :
                        if(p[iSub_p]!="*"): #s未结束，p结束了
                            return False
                        else:
                            return True
                    
                
                if (iSub_p == iPatternLen -1) and (iSub_s  == iStrLen -1):
                    print("L",sys._getframe().f_lineno,"(iSub_p == iPatternLen -1) and (iSub_s  == iStrLen -1)")
                    return True
                #end of 判断
                
                
                print("L",sys._getframe().f_lineno,"To Next loop")
                #若continue，bInnerJumpFlag 为false，若break则为True；
                #iSub_p += 1
                #continue
                
                #应该在此处立即判断，符合条件立刻return
            
            elif ("*" == p[iSub_p]):

                lastChar = p[iSub_p-1]
                
                if (s[iSub_s + iSub_p] == lastChar) or ("." == lastChar):
                    #如果s的当前字符与正则式*前面字符相等，实际正则式仍应继续匹配
                    #内循环停止，外循环继续
                    #iSub_p += 1
                    bInnerJumpFlag = True
                    bLastMatchFlag = True
                    
                    if(iSub_s + iSub_p  == iStrLen-1):
                        print("L",sys._getframe().f_lineno,"(iSub_s + iSub_p  == iStrLen-1)","return TRUE")
                        return True
                    #应该在此处立即判断，符合条件立刻return
                    
                    break
        
                else:
                    #s[iSub_s + iSub_p] == lastChar
                    #当前[iSub_s + iSub_p]的末端s匹配了lastChar(0)，正则式退出匹配，
                    #将patter中*以后的字符串与s当前位置及以后的部分进行匹配
                    print ("L",sys._getframe().f_lineno,"recursor calling isMatch",s[iSub_s + iSub_p:],"...VS....",p[iSub_p+1:])
                    return isMatch(s[iSub_s + iSub_p:],p[iSub_p+1:])
            else:
                if ( iSub_p + 1 <=iPatternLen -1) and ("*" == p[iSub_p+1]):
                    #此处需要加入
                    print ("L",sys._getframe().f_lineno,"recursor calling isMatch",s[iSub_s + iSub_p:],"...VS....",p[iSub_p + 2:])
                    return isMatch(s[iSub_s + iSub_p:],p[iSub_p +2:])
                
                lastChar = p[iSub_p]
                
                bInnerJumpFlag = True
                bLastMatchFlag = False

                print("L",sys._getframe().f_lineno,"Falling to else! return FALSE")
                return False
            
                if (iSub_p ==iPatternLen -1 ) and (bLastMatchFlag == True):
                    print("L",sys._getframe().f_lineno,"(iSub_p ==iPatternLen -1 ) and (bLastMatchFlag == True)","Falling to else! return FALSE")
                    return True
                break

            iSub_p += 1
            
            #if (iSub_s + iSub_p) > iStrLen -1:
            #    print("(iSub_s + iSub_p) > iStrLen -1, returning False!")
        if (bInnerJumpFlag == True):
            print("L",sys._getframe().f_lineno,"bInnerJumpFlag == True","iSub_s += 1")
            iSub_s += 1
        
        #最好在这里不用作判断了…………………………………………
        '''
        if ((iSub_p > iPatternLen -1) or (iSub_s >iStrLen-1)) : 
            print("L",sys._getframe().f_lineno,"iSub_p (",iSub_p,") > iPatternLen(",iPatternLen,") -1, returning")
            print("L",sys._getframe().f_lineno,"iSub_s (",iSub_s,") > iStrLen(",iStrLen,") , returning")

            return bLastMatchFlag
        
        if (iSub_s + iSub_p +1 > iStrLen-1):
            return bLastMatchFlag
        '''
        #………………………………………………………………………………………………
        
    return bInnerJumpFlag

'''
print(isMatch(s="abbcdefghij",p="abbcde"))#<------False
print(isMatch(s="abbcdefghij",p="abbcde*fghij"))#<------True
print(isMatch(s="missssipi",p="mis*ip."))#<------True
print(isMatch(s="aa",p="a"))  #<----False
print(isMatch(s="mississippi",p="mis*is*ip*."))#<------True
print(isMatch(s="aa",p="a"))#<------False
print(isMatch(s="aa",p="a*"))#<------True
print(isMatch(s="aa",p="ab"))#<------False
print(isMatch(s="ab",p=".*"))#<------True-----正则式应匹配最大字符串
print(isMatch(s="aab",p="c*a*b"))#<------True-----
print(isMatch(s="ab",p=".*c"))#<------False
print(isMatch(s="aaa",p=".*"))#<------True
'''
print(isMatch(s="a",p="ab*a"))#<------True
#以上不完全正常，leetcode中358个案例大概能通过259个。