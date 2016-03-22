#! python3
# -*- coding: utf-8 -*-
# BMI Body Mass Index
height=input ('升高')
weight=input ('体重')
h=float(height)
w=float(weight)
bmi=w/(h*h)
print (bmi)
if bmi < 18.5 :
  print('过轻')
elif bmi < 25 :
  print('正常')
elif bmi < 28 :
  print('过重')
elif bmi < 32 :
  print('肥胖')
else :
  print('严重肥胖')
  