#!/usr/bin/env python
# coding: utf-8

# # 07: Menghapus (drop) missinng values (NaN)

# Import Modules

# In[1]:


import pandas as pd 

print(pd.__version__)


# Pesiapan Data Frame

# In[4]:


df = pd.util.testing.makeMissingDataframe().reset_index()
df.head()


# In[5]:


df = df.rename(columns={'index':'Z'})
df.head()


# In[6]:


df_backup = df.copy(deep=True)


# Menghapus (drop) setiap kolom yang mengandung missing values

# In[7]:


df = df.dropna(axis='columns')
df.head()


# In[ ]:


Menghapus (drop) setiap baris yang mengandung missing values


# In[8]:


df = df_backup.copy(deep=True)
df = df.dropna(axis='rows')
df.head()


# Pesentase missing values untuk tiap kolom

# In[9]:


df = df_backup.copy(deep=True)
df.isna().mean()


# Menghapus (drop) setiap kolom yang mengandung missing values berdasarkan threshold

# In[10]:


treshold = len(df) * 0.9
df = df.dropna(thresh=treshold, axis='columns')
df.head()

