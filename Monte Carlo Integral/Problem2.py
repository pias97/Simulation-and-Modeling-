# -*- coding: utf-8 -*-
"""Problem2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11TQru54SmlaAzlUMV25ecYL5l0zoE-LW

#Library
"""

import random
import math
from math import exp
import matplotlib.pyplot as plt

"""#For Area"""

random.seed(20)
n=[100,1000,5000,10000]
a1=0
b1=4
a2=4
b2=8
error1_array=[]
error2_array=[]
for trials in n:
  func1_sum=0 # f_avg
  func2_sum=0 # f_avg
  func1_square_sum=0 # f_square_avg
  func2_square_sum=0 # f_square_avg

  for i in range(trials):
    #randomly pick a value of x between a and b
     x1= random.uniform(a1,b1)
     x2= random.uniform(a2,b2)
    #find f(x) value
    #Equation (i) and (ii)
     h1= 4*x1
     h2= 8-x2
    #func_sum update
     func1_sum += h1
     func2_sum += h2
     func1_square_sum += (h1**2)
     func2_square_sum += (h2**2)
    #func_squared_sum update
  
  func1_average=func1_sum/trials
  func2_average=func2_sum/trials
  func1_squared_average=func1_square_sum/trials
  func2_squared_average=func2_square_sum/trials
  print("Function 1 average(4x):-")
  print(func1_average, func1_squared_average, " :: err")
  print("Function 2 average(8-x):-")
  print(func2_average, func2_squared_average, " :: err")
  integral1_value=func1_average*(b1-a1) 
  integral2_value=func2_average*(b2-a2) 
 
  error1=((b1-a1)/math.sqrt(trials))*(math.sqrt(func1_squared_average - (func1_average**2) ))
  error2=((b2-a2)/math.sqrt(trials))*(math.sqrt(func2_squared_average - (func2_average**2) ))
  error1_array.append(error1)
  error2_array.append(error2)
  print("For number of points= ", trials)
  print("Integral value of Function 1(4x): ",integral1_value)
  print("Integral value of Function 2(8-x): ",integral2_value)
  print("Integral value of Function 1(4x):", error1)
  print("Integral value of Function 1(8-x):", error2)
  print("-----------------------------------------------------------------------------------------------------")

"""#For Function (ii)"""