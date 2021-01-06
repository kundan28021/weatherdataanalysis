#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


from datetime import datetime 


# In[6]:


import glob


# In[7]:


cd /Users/kundan/Desktop


# In[8]:


path = '/Users/kundan/Desktop' # use your path
all_files = glob.glob(path + "/*.csv")


# In[13]:


li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0,parse_dates = [2])
    li.append(df)


# In[25]:


finalDf = pd.concat(li, axis=0, ignore_index=True)


# In[20]:


finalDf.head()


# In[26]:


finalDf.isnull().sum()


# In[29]:


len(finalDf)


# In[29]:


len(finalDf)


# In[27]:


finalDf = finalDf.drop(['WindGust','Visibility','Pressure','Country'],axis = 1)


# In[30]:


len(finalDf)


# In[31]:


finalDf.isnull().sum()


# In[33]:


finalDf = finalDf.groupby('ObservationDate').max()[['ScreenTemperature','Region']].max()


# In[34]:


finalDf


# In[ ]:




