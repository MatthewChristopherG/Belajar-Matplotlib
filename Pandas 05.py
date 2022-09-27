#!/usr/bin/env python
# coding: utf-8

# # 05 Membalik urutan baris dan kolom pada Data Frame

# Import Modules

# In[2]:


import pandas as pd 
import numpy as np

print(pd.__version__)
print(np.__version__)


# Persiapan Data Frame

# In[4]:


n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                 columns=cols)

df


# Membalik Urutan Kolom

# In[5]:


df.loc[:, ::-1]


# Membalik Urutan Baris

# In[7]:


df.loc[::-1, :]


# Membalik urutan baris dan melakukan penyesuaian ulang index

# In[8]:


df.loc[::-1].reset_index(drop=True)

