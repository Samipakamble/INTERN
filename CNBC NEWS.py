#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page = requests.get('https://www.cnbc.com/world/?region=world')
page


# In[4]:


page.content


# In[5]:


soup = BeautifulSoup(page.content, "html.parser")


# In[6]:


headline = soup.find('ul', class_="LatestNews-list")
headline.text


# In[ ]:




