#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


url = "https://scholar.google.com/citations?view_op=top_venues"


# In[4]:


page = requests.get(url)
page


# In[5]:


page.content


# In[6]:


soup = BeautifulSoup(page.content, "html.parser")


# In[12]:


scraped_publication = soup.find_all('td', class_="gsc_mvt_t")
scraped_publication


# In[11]:


scraped_h5index = soup.find('td', class_="gsc_mvt_n")
scraped_h5index


# In[15]:


h5index = []
for h5index in scraped_h5index:
    h5index = h5index.get_text().replace('\n', '')
    h5index.append(h5index)
h5index


# In[16]:


data = pd.DataFrame()
data['Publication'] = Publication
data['h5index'] = h5index
data.head()


# In[1]:


rank = soup.find('td', c;ass_="gsc_mvt_p")
rank.test


# In[ ]:




