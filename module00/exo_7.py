# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:58:40 2021

@author: IBTIHAL
"""

def filtrered(phrase,n):
    phrase=phrase.split()
    filtrer = filter(lambda x: len(x)>n, phrase)
    
    return list(filtrer)