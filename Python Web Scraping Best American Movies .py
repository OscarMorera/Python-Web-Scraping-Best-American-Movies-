#!/usr/bin/env python
# coding: utf-8

# In[58]:


from bs4 import BeautifulSoup
import requests


# In[59]:


url = 'https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[60]:


print(soup)


# In[61]:


table = soup.find_all('table')[1]


# In[62]:


print (table)


# In[63]:


world_titles = table.find_all('th')


# In[64]:


print(world_titles)


# In[65]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[66]:


import pandas as pd


# In[67]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[68]:


column_data = table.find_all('tr')


# In[69]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[70]:


df


# In[71]:


df.to_csv(r'C:\Users\Admin\Desktop\Python Web Scraping\AFIs_100_Years.csv', index = False)


# In[ ]:




