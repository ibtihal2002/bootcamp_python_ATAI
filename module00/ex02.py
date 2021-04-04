# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:44:44 2021
@author: IBTIHAL
"""

def number(nb):
    if type(nb)==str or type(nb)==float:
        print("error the input should be an integer")
    elif nb==0:
        print("I'm Zero.")
    elif nb%2==0:
        print("I'm Even.")
    else:
        print ("I'm Odd.")
