'''

# https://www.w3schools.com/python/python_ml_getting_started.asp

# ML is a step towards AI
# ML analyzes data and LEARNS to predict outcomes.

# 3 kinds of data
# 	1. Numerical ( discrete and continuous)
#	2. Categorical (Yellow / blue, Male/Female)
# 	3. Ordinal (School grades, safety grades)

#ML particuarly intersted in these 3 stats:
#	1. Mean
#	2. Median
#	3. Mode

print("Hello World")
#NUMPY W3 module:https://www.w3schools.com/python/numpy/default.asp
# 

#pip3  install --upgrade pip
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)
#Hello World
#89.76923076923077


# MEDIAN , sort, then find the middle or avg
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)
print("The MEDIAN values is", + x)

##
#if there are 2 numbers in the middle , avg them
speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print("The MEDIAN values is", + x)

######### For Mode We Need scipy 
# pip3 install numpy   
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)
print(x)
#print("The MODE of SPEED  is", + x)

########## STANDARD DEVIATION ##############
# https://www.w3schools.com/python/python_ml_standard_deviation.asp

import numpy

speed = [86,87,88,86,87,85,86]

x = numpy.std(speed)

print("The Std Dev is", + x)
#print(x)

########## VARIANCE   ##################
# https://www.w3schools.com/python/python_ml_standard_deviation.asp

# Sq root of variance is Std Dev
#  Std Dev ^2 is Variance

import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)

print(x)
print("The Variance  is", + x)

########## PERCENTILES ##################
# https://www.w3schools.com/python/python_ml_percentile.asp

# Percentile answers how what percent  people are below.
# E>G, how many peopl are below the age
# of 75?  33% are below the age of 75
#import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)
print("The Percentile  is", + x)
#
# What is the age that 90%  of the people are 
#younger  than?

#import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 90)

print(x)
print("What is the age that 90% are youngert than?", + x)

######### DATA DISTRIBUTION ###########
# https://www.w3schools.com/python/python_ml_data_distribution.asp

# to create a data array
# This is 250 random floats btwn 0 and 0.5

#import numpy

#x = numpy.random.uniform(0.0, 5.0, 250)

#print(x)

###### HISTOGRAM  #############

#pip3 install matplotlib  #    <<<-------------------

import numpy
import matplotlib.pyplot as plt      ## <<<-----------

#x = numpy.random.uniform(0.0, 5.0, 250)
#### 5 bars
#plt.hist(x, 5)
#plt.show()

# 10 bars
#plt.hist(x, 10)
#plt.show()

# CREATE A DATA SET OF 100K RANDOM NUMBERS 
# AND DISPLAY THM IN A HISTOGRAM OF 100 BARS.

#x = numpy.random.uniform(0.0, 50, 100000)
#plt.hist(x, 100)
#plt.show()

####### NORMAL DATA DISTRIBUTION ##########
#https://www.w3schools.com/python/python_ml_normal_data_distribution.asp

import numpy
import matplotlib.pyplot as plt

#Numpy.random.normal( mean value = 5, std dev = 1, 100k #s)
x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
#plt.show()
'''
############# SCATTER PLOT  ################
#https://www.w3schools.com/python/python_ml_scatterplot.asp


import matplotlib.pyplot as plt
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#plt.scatter(x, y)
#plt.show()

# tow arrays,  1k numbersin each
# Two arrrays. First with mean of 5, std dev of 1
# and second mea=10, std dev = 2

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

#plt.scatter(x, y)
#plt.show()

####### LINEAR REGRESSION #############
# https://www.w3schools.com/python/python_ml_linear_regression.asp

#Linear Regression : finding the relation btwn variables
#Knowing one might tell us what the other will be.  Prediction.

# Simple LR draws a stright line closest to all data points


import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#plt.scatter(x, y)
#plt.show()

# To draw the line of linear regression import SCIPY 
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)
print("The slope is", slope)
print("The intercept is",intercept )
print("the r is", r)
print("The p is ", p)
print("The std_err is", std_err)


def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

#plt.scatter(x, y)
#plt.plot(x, mymodel)
#plt.show()



# Creat a function that uses slope and intercept that determiens where 
# where on  x y graph the point will be placed.

def myfunc(x):
  return slope * x + intercept

# run each value throuht he function.
#The reulst will be new values on the y axis.

mymodel = list(map(myfunc, x))

#Now draw the original scatter
#plt.scatter(x, y)

# add the regression line
#plt.plot(x, mymodel)

#Display
#plt.show()

############## R is for Relatioship ###########
#https://www.w3schools.com/python/python_ml_linear_regression.asp

# R is the coefficient of correaltion
# R ranges from -1 to +1
#It is ameasuer eof how well the data fit the regression

from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)
print("The R is", r)

##### Predict Future Values ############
# https://www.w3schools.com/python/python_ml_linear_regression.asp

############ PRedict the age of car  ########
# https://www.w3schools.com/python/python_ml_linear_regression.asp



'''
Example : Predict speed of a 10y.o car
we need the same myfunct() function from above:
def myfunc(x):
  return slope * x + intercept
'''
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print(speed)
print("The speed is",speed)

#########  An example of a Bad fit  #########
# https://www.w3schools.com/python/python_ml_linear_regression.asp

import matplotlib.pyplot as plt
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

#plt.scatter(x, y)
#plt.plot(x, mymodel)
#plt.show()

###### Polynomial Regression ################
# https://www.w3schools.com/python/python_ml_polynomial_regression.asp

# A non straight line regression line

#Cars going through a toll booth
# x = time of day
# Y = speed

import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

#plt.scatter(x, y)
#plt.show()

import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

myline = numpy.linspace(1, 22, 100)

#plt.scatter(x, y)
#plt.plot(myline, mymodel(myline))
#plt.show()

# Numpy has a method for making polynomial model
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Specify haoe thw line will display
#Start at 1 end at 22
# myline = numpy.linspace(1, 22, 100)

# Draw the original scatter
# myline = numpy.linspace(1, 22, 100)

#Draw the line of polynomial regression:
# plt.plot(myline, mymodel(myline))

#Display the diagram:
# plt.show()

######### R SQUARED #################
# https://www.w3schools.com/python/python_ml_polynomial_regression.asp
'''
'''
#Btwn 0 and 1, measure of relation btwn x & y.
#Btwn o & 1
'''
'''




# run:  this in the terminal
# pip3 install sklearn
import numpy
from sklearn.metrics import r2_score


x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

print("last line")












