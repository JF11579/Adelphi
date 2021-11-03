#!/usr/bin/env python
# coding: utf-8

# Apply **multiple** clustering algorythms to wine data set
# Cluster according to wine label
# Use column "0" as labeling plots

# https://archive.ics.uci.edu/ml/datasets/wine

# Libraries

# In[2]:


import pandas as pd


# In[ ]:


# *italics*   JUST COPY AND PATE THESE INTO
# <b>bold</b>   THE CELL AND SIMPLY REVISE THE TEXT


# Data pothole.  Someone saved the Wine data with the suffix as "data".
# Confess i tripped over this trying to figure out why Libre 
# insisted on opening the file as text file.  In the download
# folder revise the name to *wine_data.csv*
# 

# In[8]:


data = pd.read_csv("wine_data.csv",header = None)
data.head(5)


# In[10]:


data.tail(3)


# We have to restore the row and col labels
# before we can check data types.

# In[31]:


data.columns = ['name','Alcohol','Malic_acid','Ash','Alcalinity_ash',
               'Magnesium','Total_phenols','Flavanoids','Nonflavanoid phenols',
                'Proanthocyanins','Color_intensity','Hue',
               'OD280/OD315_of_diluted wines','Proline ']


# In[32]:


data.head(2)


# In[35]:


data.head(3)


# In[36]:


data.tail(3)


# In[39]:


#ck data types 
#print(type(data))
print(data.dtypes)


# In[42]:


data.shape


# In[43]:


# missing valus?
data.isnull().sum
# this tells us row by row where any missing 
#values are but... we have too many rows


# In[44]:


# Before we figure out a method 
# to located any NAs let us check if 
# there even any  NAs.
# Here we sum all of the 
# NAs dusicovered above into a single 
# number
# 
# We got lucky
data.isnull().sum().sum()


# https://machinelearningmastery.com/standardscaler-and-minmaxscaler-transforms-in-python/
# Accordning to Dr. Jason Brownlee the two most popular wasy of scaling data
# are **Normalization** and **Standardization**.  **Normalization** "Scales each variable sepearetly to a valuee btwn 0:1.   **Standaridzation** changes the distribution of the values so tha tthey have a mean of 0 and a std dev of 1.
# 
# We will see the effect of each method on our clustering.

# In[ ]:


plot the distributions of each
plot the distrutions now.  do a boxplot of each variable.


# In[45]:


#https://seaborn.pydata.org/examples/grouped_boxplot.html
import seaborn as sns


# In[ ]:


sns.set_theme(style="ticks", palette="pastel")


# In[59]:


########################################
### It seems no one has figured out  ###
### how to rotate Seaborn plots yet? ###
########################################

#https://seaborn.pydata.org/examples/grouped_boxplot.html
#import seaborn as sns
#sns.set_theme(style="ticks", palette="pastel")
#sns.boxplot(data=data)


# In[58]:


fig = plt.figure(figsize =(10, 7))
plt.boxplot(data, vert = False)
plt.title("And thisIs Why We Scale the Data To Start")
plt.xlabel("")
plt.ylabel("Our Variables")
plt.show()

#INTERESTING (to me). When one rotates a plot 90deg in R'sGGPLOT
#     The X & Y stay who they are.  One is just roatating the 
#     piece of paper the plot is printed on.  Makes Sense.
#     But Matplot calls whichever axis horizontal the X-axis
#     ODD


# In[60]:


# A better way to appreciate the differnces in values among the 
# features is look over the "describe" output.

describe = data.describe()
describe


# In[ ]:


# data_safety = data


# In[62]:


#. ok back to Jason Brownlee and scaling our data both ways
# First the 0 to 1 , the normalization method.

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
print(scaler.fit(data))
print(scaler.transform(data))


# Now let us re -run our box plot

# In[64]:


fig = plt.figure(figsize =(10, 7))
plt.boxplot(data, vert = False)
plt.title("And thisIs Why We Scaled the Data")
plt.xlabel("")
plt.ylabel("Our Variables")
plt.xlim([0, 3])
plt.show()


# Let us change the *Y* axis

# In[ ]:





#  do I want all of the cols?
