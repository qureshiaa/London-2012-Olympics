#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd

data = pd.read_excel(r"Olympic 2012 Medal Tally.xlsx",skiprows=2,)


# In[15]:


data = pd.DataFrame(data)


# In[16]:


data.info()


# In[17]:


data.drop(['Unnamed: 0'], axis=1, inplace=True)


# In[19]:


data.index += 1 


# In[23]:


data = data.rename(columns={"Unnamed: 1": "Country", "Unnamed: 2": "Country Code","Unnamed: 3": "Olympics Year"})


# In[24]:


data


# In[28]:


import numpy as np


# In[29]:


max_gold = np.max(data['Gold'])


# In[43]:


gold_max = data['Gold'].max()
gold_max


# In[51]:


np_countries = np.array(data['Country'])
np_gold = np.array(data['Gold'])


# In[54]:


max_gold = np_gold.argmax()


# In[55]:


np_countries[max_gold] # Country with Max Gold Medals


# In[58]:


more_than_20 = np.argwhere(np_gold > 20)


# In[59]:


np_countries[more_than_20] # Countries with more than 20 Gold Medals


# In[61]:


np_silver,np_bronze = np.array(data['Silver']), np.array(data['Bronze'])


# In[65]:


total_medals = np_gold + np_silver + np_bronze
np.add(np_gold,np_silver,np_bronze)


# In[78]:


total_medals_won = sum(data['Gold'] + data['Silver'] + data['Bronze'])


# In[69]:


sum(total_medals) # Total amount of medals awarded


# In[81]:


data['Total Medals Won'] = data['Gold'] + data['Silver'] + data['Bronze']


# In[82]:


data


# In[83]:


medal_won_total = np.array(data['Total Medals Won'])


# In[85]:


medal_won_total


# In[86]:


data[['Country','Total Medals Won']] # Number of Total Medals by Country

