# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:49:40 2021

@author: IBTIHAL
"""

import random 
n=random.randint(1,99)
print(n)
coup=1
while True:
    m = input("donner un nombre: ") 
    if m == 'exit':
        print('goodbye!')
        exit()
    if m.isnumeric():
        m = int(m)
        if m < n:
            print("Too low!")
        elif m > n:
            print("too high")
        else:
            break     
        coup += 1
    else:
        print('only numbers')
print ("Congratulations, you've got it in :",coup,"tries")



