# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:49:40 2021

@author: IBTIHAL
"""

import random 
n=random.randint(1,99)
m=int(input("donner un nombre"))
coup=0
while (m != n):    
    if (n> m):       
        print("Too low!");
        m=m+1
    else:        
        if (n < m):            
            print("Too high!")    
            m=int(input("donner un nombre"))    
            coup+=1
            print ("Congratulations, you've got it in :",coup,"tries")


