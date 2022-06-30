#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc/"


# In[4]:


page = requests.get(url)
page


# In[5]:


page.content


# In[6]:


soup = BeautifulSoup(page.content, "html.parser")


# In[21]:


scraped_ratings = soup.find_all('div', class_='ratings-bar')
scraped_ratings


# In[20]:


scraped_year = soup.find_all('span', class_='lister-item-year text-muted unbold')
scraped_year


# In[23]:


scraped_headings = soup.find_all('h3', class_='lister-item-header')
scraped_headings


# In[27]:


data = pd.DataFrame()
data['Ratings'] = ratings
data['Year'] = Year
data['Headings'] = headings
data.head()


# In[ ]:




