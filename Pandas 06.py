#!/usr/bin/env python
# coding: utf-8

# # 06 Mengganti nama (label) kolom pada Data Frame

# Import Modules

# In[2]:


import pandas as pd 
import numpy as np

print(pd.__version__)
print(np.__version__)


# In[4]:


n_rows = 5
n_cols = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(n_rows, n_cols)),
                 columns=cols)

df


# Mengganti nama (label) untuk sebuah kolom pada Data Frame

# In[5]:


df.rename(columns={'C':'Hobi'})


# Mengganti nama (label) untuk banyak kolom pada Data Frame

# In[9]:


df.rename(columns={'A':'Nama', 'B':'Alamat', 'D':'Kota'})

