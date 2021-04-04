# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:42:56 2021

@author: IBTIHAL
"""

def operation(nb1,nb2):
    if type(nb1)==str or type(nb2)==str:
        print("error : only numbers ")
    elif nb2==0:
         S=nb1+nb2
         D=nb1-nb2
         P=nb1*nb2
         print("Sum:",S,"Difference:",D,"Product:",P,"Quotient: ERROR (div by zero)","Remainder: ERROR (modulo by zero)",sep='\n')
    else:     
        S=nb1+nb2
        D=nb1-nb2
        P=nb1*nb2
        Q=nb1/nb2
        R=nb1%nb2
        print("Sum= ",S,"Difference= ",D,"Product=",P,"Quotient= ",Q,"Remainder= ",R,sep='\n')