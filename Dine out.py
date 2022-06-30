#!/usr/bin/env python
# coding: utf-8

# In[15]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[24]:


url = "https://www.dineout.co.in/mumbai-restaurants"


# In[25]:


page = requests.get(url)
page


# In[26]:


page.content


# In[18]:


soup = BeautifulSoup(page.content, "html.parser")


# In[36]:


first_title.text


# In[33]:


loc = soup.find('div',class_="restnt-loc ellipsis")
loc.text                         


# In[35]:


loc = soup.find('div',class_="detail-info")
loc.text


# In[ ]:




