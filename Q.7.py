#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


url = "https://www.cnbc.com/world/?region=world"


# In[3]:


page = requests.get(url)
page


# In[4]:


page.content


# In[5]:


soup = BeautifulSoup(page.content, "html.parser")


# In[8]:


scraped_headlines = soup.find_all('div', class_='LatestNews-headlineWrapper')
scraped_headlines


# In[12]:


scraped_headlines = soup.find('div', class_='LatestNews-headlineWrapper')
scraped_headlines


# In[14]:


scraped_Time = soup.find('time', class_='LatestNews-timestamp')
scraped_Time


# In[17]:


Newslinks = soup.find('div', class_="QuickLinks-scrollableContainer")
Newslinks.text


# In[ ]:




