# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:39:37 2021

@author: IBTIHAL
"""
#kata00
def tpl(t):
    n=len(t)
    print("the",n," numbers are:",end='')
    for i in range (0,n):
        print(t[i],end=',')
        
#kata01
languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
for key,value in languages.items():
    print(key," was created by ",value)

#kata02
def timing(hour, minutes, year, month, day):
    print(month ,"/" ,day,"/",year," ",hour,":",minutes)
    
#kata03
def kata03(phrase):
    print(phrase.rjust(42,"-"))
    
#kata04
"{:2e}".format( 0, 4, 132.42222, 10000, 12345.67)
    