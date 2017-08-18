
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

import pandas as pd


# In[3]:

import seaborn as sns


# In[4]:

from PIL import Image


# In[5]:

import matplotlib.pyplot as plt


# In[6]:

get_ipython().magic('matplotlib inline')


# In[7]:

#return type of pandas.read_csv is DataFrame
data  = pd.read_csv("/home/devops/Documents/Practice-Python/Shakespeare_data.csv" , sep = ',')


# In[8]:

wordcld = pd.Series(data['PlayerLine'].tolist()).astype(str)


# In[9]:

image = np.array(Image.open("/home/devops/Documents/Practice-Python/william-shakespeare-black-silhouette.png"))


# In[11]:

from wordcloud import WordCloud


# In[12]:

wc = WordCloud(mask = image, margin=1, max_font_size=125)


# In[13]:

wc.generate(' '.join(wordcld.astype(str)))


# In[14]:

#store to file
wc.to_file('/home/devops/Documents/Practice-Python/shakespear.png')


# In[15]:

#plot
plt.imshow(wc,interpolation='bilinear')


# In[16]:

plt.axis('off')


# In[17]:

plt.figure()


# In[18]:

plt.imshow(image, cmap = plt.cm.gray , interpolation='bilinear')


# In[19]:

plt.axis('off')


# In[20]:

plt.show()


# In[10]:

data.head(8)


# In[11]:

data['Player'].replace(np.nan,'Other',inplace = True)


# In[12]:

data.head(8)


# In[13]:

#group the players according to play

play = data.groupby('Play').count().sort_values(by = 'PlayerLine',ascending = False)['PlayerLine']


# In[14]:

#convert play data to frame
play = play.to_frame()


# In[15]:

play['Play'] = play.index.tolist()


# In[17]:

play.index


# In[18]:

#convert this str index which is play(name) to numbers
play.index  = np.arange(0,len(play)) 


# In[19]:

play


# In[20]:

#now analysing player info
no_player  = data.groupby(['Play'])['Player'].nunique().sort_values(ascending = False).to_frame()


# In[21]:

no_player['Play'] = no_player.index.tolist()


# In[22]:

no_player.index


# In[23]:

no_player.index = np.arange(0 , len(no_player))


# In[24]:

no_player


# In[25]:

plt.figure(figsize=(150,150))


# In[26]:

#plotting using sns -> seaborn
#plotting a barplot

ax = sns.barplot(data = no_player , x = 'Player' , y = 'Play')


# In[27]:

ax.set(xlabel = 'Number Of Players' , ylabel = 'Play_Name')


# In[28]:

fig = ax.get_figure()


# In[29]:

fig.savefig('/home/devops/Documents/Practice-Python/number_players.png')


# In[30]:

plt.show()


# In[ ]:



