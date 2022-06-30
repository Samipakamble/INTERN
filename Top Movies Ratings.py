#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


url = "https://www.imdb.com/india/top-rated-indian-movies/"


# In[4]:


page = requests.get(url)
page


# In[5]:


page.content


# In[6]:


soup = BeautifulSoup(page.content, "html.parser")


# In[7]:


scraped_movies= soup.find_all('td', class_='titleColumn')
scraped_movies


# In[8]:


movies = []
for movie in scraped_movies:
    movie = movie.get_text().replace('\n', "")
    movie = movie.strip(" ")
    movies.append(movie)
movies
    


# In[9]:


scraped_ratings = soup.find_all('td', class_='ratingColumn imdbRating')
scraped_ratings


# In[11]:


ratings = []
for rating in scraped_ratings:
    rating = rating.get_text().replace('\n', '')
    ratings.append(rating)
ratings


# In[13]:


data = pd.DataFrame()
data['Movie Names'] = movies
data['Ratings'] = rating
data.head()


# In[15]:


data.to_csv('IMDB Top Movies.csv', index = False)


# In[ ]:





# In[ ]:




