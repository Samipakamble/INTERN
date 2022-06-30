#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get('https://www.wikipedia.org/')
page


# In[4]:


page.content


# In[5]:


soup = BeautifulSoup(page.content, "html.parser")


# In[6]:


header = soup.find('div', class_="central-featured-lang lang1")
header.text


# In[7]:


header = soup.find('div', class_="central-featured-lang lang2")
header.text


# In[8]:


header = soup.find('div', class_="central-featured-lang lang3")
header.text


# In[9]:


header = soup.find('div', class_="central-featured-lang lang4")
header.text


# In[10]:


header = soup.find('div', class_="central-featured-lang lang5")
header.text


# In[11]:


header = soup.find('div', class_="central-featured-lang lang6")
header.text


# In[12]:


header = soup.find('div', class_="central-featured-lang lang7")
header.text


# In[13]:


header = soup.find('div', class_="central-featured-lang lang8")
header.text


# In[14]:


header = soup.find('div', class_="central-featured-lang lang9")
header.text


# In[15]:


header = soup.find('div', class_="central-featured-lang lang10")
header.text


# In[ ]:




