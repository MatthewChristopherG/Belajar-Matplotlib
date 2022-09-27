#!/usr/bin/env python
# coding: utf-8

# # Pengenalan pyplot
# 
# pyplot merupakan koleksi atau kumpulan fungsi yang menjadikan Matplotlib dapat bekerja menyeupai MATLAB.
# pyplot API secara umum less-flexible bila dibandingkan object-oriented API

# Import modules

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)


# Membuat plotting sederhana

# In[4]:


plt.plot([2, 5, 7, 11])
plt.ylabel('sumbu y')
plt.show()


# Pemanggilan fungsi plot() dapat dilakukan dengan menyertakan hanya sebuah deret bilangan (list/array) ataupun dua buah deret bilangan (list/array).
# Bila pemanggilan hanya menyertakan sebuah deret bilangan, maka nilai pada deret bilangan tersebut akan dijakikan data point untuk nilai pada sumbu y; sedangkan nilai pada sumbu x akan secara otomatis dibuatkan sebuah deret bilangan teruut dengan nilai dimulai dari nol.

# In[5]:


plt.plot([2, 3, 4, 7], [5, 4, 2, 16])
plt.show()


#  Pengatuan Format pada plot

# Selain menyertakan dua buah deet bilangan sebagai parameter untuk sumbu x dan y, terdapat paamete ketiga yang bisa kita sertakan untuk mengatur warna dan jenis plotting.
# 
# Pengaturan parameter ketiga ini sepenuhnya mengadopsi gaya formatting pada MATLAB.
# 
# Nilai default untuk parameter ketiga ini adalah 'b-'
# 
# Pemanggilan fungsi axis() menyertakan sebuah list [xmin, xmax, ymin, ymax].

# In[11]:


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
plt.axis([0, 6, 0, 20])
plt.show()


# parameter ketiga pengatur bentuk marker yang dimaksud adalah karakter o dan bukan nol

# In[12]:


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b-')
plt.axis([0, 6, 0, 20])
plt.show()


# In[15]:


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b*')
plt.axis([0, 6, 0, 20])
plt.show()


# Multi plot dalam satu pemanggilan fungsi plot()

# In[16]:


t = np.arange(0., 5., 0.2)
t


# In[20]:


plt.plot(t, t, 'r--')
plt.plot(t, t**2, 'gs')
plt.plot(t, t**3, 'b^')
plt.show()


# Kita juga dapat melakukan multi plot dalam satu pemanggilan fungsi plot()

# In[22]:


plt.plot(t, t, 'b--',
         t, t**2, 'rs',
         t, t**3, 'g^')
plt.show()


# Plotting dengan keywords

# Matplotlib juga memungkinkan kita untuk melakukan plotting sekumpulan nilai yang tersimpan dalam struktur data yang disertai keywords argument (kwargs) seperti pada dictionary dan Pandas DataFrame.

# In[27]:


data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

data


# In[29]:


plt.scatter('a', 'b', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


# In[30]:


plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


# # Plotting untuk tipe data categorical
# 
# Matplotlib juga mendukung plotting untuk data dengan tipe kategori atau biasa dikenal dengan istilah categorical data atau categorical variables.
# 

# In[31]:


names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]


# In[32]:


plt.plot(names, values)
plt.show()


# In[33]:


plt.scatter(names, values)
plt.show()


# In[34]:


plt.bar(names, values)
plt.show()

