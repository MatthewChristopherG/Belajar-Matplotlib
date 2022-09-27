#!/usr/bin/env python
# coding: utf-8

# # 08: Memeriksa kesamaan antar dua buah kolom (Series) pada Data Frame

# In[ ]:


Import Modules


# In[1]:


import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)


# Pesiapan Data Frame

# In[2]:


data = {'A':[15, 15, 18, np.nan, 12],
        'B':[15, 15, 18, np.nan, 12]}

df = pd.DataFrame(data)
df


# Mengenal Pandas Series

# In[3]:


df['A']


# In[4]:


type(df['A'])


# In[5]:


type(df)


# Memeriksa kesamaan dengan operator ==

# In[6]:


df['A'] == df['B']


# Memeriksa kesamaan dengan method equals()

# In[7]:


df['A'].equals(df['B'])


# In[ ]:


Memeriksa kesamaan anta dua Data Frame


# In[8]:


df1 = df.copy(deep=True)

df.equals(df1)


# In[11]:


df == df1

