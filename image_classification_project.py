#!/usr/bin/env python
# coding: utf-8

# In[11]:


# importing dependencies
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


# using pandas to read the database stored in the same folder
data = pd.read_csv('mnist.csv')


# In[13]:


# view column heads
data.head()


# In[14]:


# extracting data from the dataset and viewing them upclose
a = data.iloc[3,1:].values


# In[15]:


# reshaping the extracted data into a reasonable size
a = a.reshape(28,28).astype('uint8')
plt.imshow(a)


# In[16]:


# preparing the data
# separating the labels and data values
df_x = data.iloc[:,1:]
df_y = data.iloc[:,0]


# In[17]:


# creating test and train batches
x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.2,random_state=4)


# In[19]:


x_train.head()


# In[20]:


# call rf classifier
rf = RandomForestClassifier(n_estimators=100)


# In[21]:


# fit the model
rf.fit(x_train,y_train)


# In[22]:


# prediction on test data
pred = rf.predict(x_test)


# In[23]:


pred


# In[24]:


# check prediction accuracy
s = y_test.values
# calculate number of correctly predicted values
count = 0
for i in range(len(pred)):
    if pred[i] == s[i]:
        count = count + 1


# In[25]:


count


# In[26]:


# total values that the prediction code was run on
len(pred)


# In[27]:


# accuracy value
8070/8400


# In[ ]:




