# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:25:02 2021

@author: IBTIHAL
"""

def revers():
    text=input("please write your text (if the text contain mor than one argument please write space before ""): ")
    space =''
    for char in text:
        space = char + space
    return space

print("hello")

revers()