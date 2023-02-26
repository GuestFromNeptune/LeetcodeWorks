# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 19:57:50 2022

@author: YuanYi
"""

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    strRoman =""
    RomanIntArray = [
                ["M",1000],
                ["CM",900],
                ["D",500],
                ["CD",400],
                ["C",100],
                ["XC",90],
                ["L",50],
                ["XL",40],
                ["X",10],
                ["IX",9],
                ["V",5],
                ["IV",4],
                ["I",1]
                ]
    for item in RomanIntArray:
        while num >= item[1]:
            num -= item[1]
            strRoman +=item[0]
        print("item:",item)
        
    print(RomanIntArray[2])
    
    return strRoman
        
gotstr=intToRoman(2)
print("2","gotstr:",gotstr)

gotstr=intToRoman(1000)
print("1000","gotstr:",gotstr)

gotstr=intToRoman(900)
print("900","gotstr:",gotstr)
