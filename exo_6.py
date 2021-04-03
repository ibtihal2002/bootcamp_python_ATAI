# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 09:12:49 2021

@author: IBTIHAL
"""

dic= {"key 1":"value 1","key b":"value b"}
for key in dic:
    print (dic.key)
for value in dic.values():
    print (dic.value)
for key, value in dic.items():
    print(key,value)
#question 2
def function():
    name=input("please enter the recepe name to get more details: ")
    dic={"sandwich":"the ingredients are :ham,bread,tomaoes,cheese.It's going to take you 10 min.It's considered as lunch meal","cake":"ingredients are floor,eggs,suger.It's going to take you 60 min. It's considered as desert ","salad":"ingredients are avocado,arogula,tomatoes,spinach.It's a lunch meal.It going to take you 20 min."}
    if(name=="cake"): 
        d = dic["cake"]
        print(d)
    
    if (name=="salad"):
        s=dic["salad"]
        print(s)
    if (name=="sandwich"):
        t=dic["sandwich"]
        print(t)
#question 3
def delete_recepe(name):
     dic={"sandwich":"the ingredients are :ham,bread,tomaoes,cheese.It's going to take you 10 min.It's considered as lunch meal","cake":"ingredients are floor,eggs,suger.It's going to take you 60 min. It's considered as desert ","salad":"ingredients are avocado,arogula,tomatoes,spinach.It's a lunch meal.It going to take you 20 min."}
     if (name=="sandwich"):
         dic.pop("sandwich") 
     if (name=="cake"):
         dic.pop("cake")
     if (name=="salad"):
         dic.pop("salad")
     print(dic)
#question 4  
x=str(input("please enter the name of the recepe: "))
y=str(input("please enter the ingredients: "))
z=str(input("please enter the type of the meal: "))
t=str(input("please enter the time of the prepation: ")) 
dic={"sandwich":"the ingredients are :ham,bread,tomaoes,cheese.It's going to take you 10 min.It's considered as lunch meal","cake":"ingredients are floor,eggs,suger.It's going to take you 60 min. It's considered as desert ","salad":"ingredients are avocado,arogula,tomatoes,spinach.It's a lunch meal.It going to take you 20 min."}
dic.update({x:y+z+t})
print(dic)
#question 5  
dic={"sandwich":"the ingredients are :ham,bread,tomaoes,cheese.It's going to take you 10 min.It's considered as lunch meal","cake":"ingredients are floor,eggs,suger.It's going to take you 60 min. It's considered as desert ","salad":"ingredients are avocado,arogula,tomatoes,spinach.It's a lunch meal.It going to take you 20 min."}
for key,value in dic:
    print(' the recepe of {0} is {1}' .format('key','value'))
#question 6
def choice():
    print("1: Add a recipe","2: Delete a recipe ","3: Print a recipe","4: Print the cookbook","5: Quit",sep='\n')
    x=input("Please select an option bellow by typing the corresponding number: ")
    print(x)
    
