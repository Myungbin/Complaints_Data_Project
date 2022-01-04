#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[24]:


data = pd.read_csv("국민권익위원회 경진 대회 데이터.csv", encoding="CP949")
data


# In[16]:


data['담당부서명'].value_counts()


# In[17]:


data['최상위기관명'].value_counts()


# In[18]:


data['답변내용']


# In[19]:


data.isnull().sum()


# ### 답변내용 결측치 제거하기

# In[74]:


df = data.dropna(subset=['답변내용'])
df


# ### 주차 관련 topic 
# 주차, 주정차, 정차, 불법, 단속, 주차장

# In[91]:


topic = ['주차, 주정차', '정차', '단속','주차장']
topic_join = '|'.join(topic)
topic_join


# ### 각 column별 topic을 포함하는 데이터 추출

# In[87]:


a = df[df['제목'].str.contains(topic_join)] 
b = df[df['질문내용'].str.contains(topic_join)] 
c = df[df['답변내용'].str.contains(topic_join)]


# In[89]:


# 3개 데이터 concat
df_new = pd.concat([a,b,c],axis=0, join='outer') 
df_new


# In[95]:



df_parking = df_new.drop_duplicates(keep = 'first')
df_parking


# In[96]:


# csv파일로 저장
# df_parking.to_csv('주차관련민원.csv', encoding= 'cp949', index= False)


# In[9]:


import pandas as pd
df = pd.read_csv('주차관련민원.csv', encoding= 'cp949')
df


# # 워드클라우드
# 

# In[9]:


from wordcloud import WordCloud
from konlpy.tag import Twitter
from collections import Counter


# In[16]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from konlpy.tag import Okt


# In[10]:


okt = Okt()


# In[11]:


all_complain_list = df['제목'].values.tolist()
all_complain_list


# In[12]:


complain_list = []

for title in all_complain_list:
    tokens = okt.morphs(title)
    complain_list.append(tokens)


# In[13]:


# 불용어 사전 텍스트 파일을 오픈

korean_stopwords_path = "불용어.txt"

with open(korean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]


# In[14]:


title = []

for i in range(len(complain_list)):
    for j in range(len(complain_list[i])):
        if complain_list[i][j] not in stopwords:
            title.append(complain_list[i][j])
title


# In[15]:


import re

title_word = [re.sub('[^A-Za-z가-힣0123456789]', '', i) for i in title]
title_word.remove('')
title_word


# In[16]:


#가장 많이 쓰이는 단어 200개 추출한다.
from collections import Counter

count_title_word = Counter(title_word).most_common(200)
del count_title_word[0]
count_title_word

# # 한글자 단어 제거한다.
count_title_word = [(tup[0], tup[1]) for tup in count_title_word if len(tup[0]) > 1]
count_title_word


# In[17]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS

def wordcloud(data, width=1200, height=500):
    word_draw = WordCloud(
        font_path=r"C:\Windows\Fonts\malgun.ttf" ,
        width=width, height=height,
        stopwords=stopwords, 
        background_color="white",
        random_state=42
    )
    word_draw.generate(data)

    plt.figure(figsize=(15, 7))
    plt.imshow(word_draw)
    plt.axis("off")
    plt.show()


# In[18]:


title_word_cloud = str(count_title_word)


# In[19]:


title_word_cloud=wordcloud(title_word_cloud, width=1200, height=500)
title_word_cloud


# In[32]:


all_complain_list = df['답변내용'].values.tolist()
all_complain_list

complain_list = []

for title in all_complain_list:
    tokens = okt.morphs(title)
    complain_list.append(tokens)
    
# 불용어 사전 텍스트 파일을 오픈

korean_stopwords_path = "불용어.txt"

with open(korean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]    


title = []

for i in range(len(complain_list)):
    for j in range(len(complain_list[i])):
        if complain_list[i][j] not in stopwords:
            title.append(complain_list[i][j])
title

import re

title_word = [re.sub('[^A-Za-z가-힣0123456789]', '', i) for i in title]
title_word.remove('')
title_word

#가장 많이 쓰이는 단어 200개 추출한다.
from collections import Counter

count_title_word = Counter(title_word).most_common(200)
del count_title_word[0]
count_title_word

# # 한글자 단어 제거한다.
count_title_word = [(tup[0], tup[1]) for tup in count_title_word if len(tup[0]) > 1]
count_title_word

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS

def wordcloud(data, width=1200, height=500):
    word_draw = WordCloud(
        font_path=r"C:\Windows\Fonts\malgun.ttf" ,
        width=width, height=height,
        stopwords=stopwords, 
        background_color="white",
        random_state=42
    )
    word_draw.generate(data)

    plt.figure(figsize=(15, 7))
    plt.imshow(word_draw)
    plt.axis("off")
    plt.show()
    
title_word_cloud = str(count_title_word)    

title_word_cloud=wordcloud(title_word_cloud, width=1200, height=500)
title_word_cloud


# In[31]:


all_complain_list = df['질문내용'].values.tolist()
all_complain_list

complain_list = []

for title in all_complain_list:
    tokens = okt.morphs(title)
    complain_list.append(tokens)
    
# 불용어 사전 텍스트 파일을 오픈

korean_stopwords_path = "불용어.txt"

with open(korean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]    


title = []

for i in range(len(complain_list)):
    for j in range(len(complain_list[i])):
        if complain_list[i][j] not in stopwords:
            title.append(complain_list[i][j])
title

import re

title_word = [re.sub('[^A-Za-z가-힣0123456789]', '', i) for i in title]
title_word.remove('')
title_word

#가장 많이 쓰이는 단어 200개 추출한다.
from collections import Counter

count_title_word = Counter(title_word).most_common(200)
del count_title_word[0]
count_title_word

# # 한글자 단어 제거한다.
count_title_word = [(tup[0], tup[1]) for tup in count_title_word if len(tup[0]) > 1]
count_title_word

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS

def wordcloud(data, width=1200, height=500):
    word_draw = WordCloud(
        font_path=r"C:\Windows\Fonts\malgun.ttf" ,
        width=width, height=height,
        stopwords=stopwords, 
        background_color="white",
        random_state=42
    )
    word_draw.generate(data)

    plt.figure(figsize=(15, 7))
    plt.imshow(word_draw)
    plt.axis("off")
    plt.show()
    
title_word_cloud = str(count_title_word)    

title_word_cloud=wordcloud(title_word_cloud, width=1200, height=500)
title_word_cloud


# In[39]:


df


# In[40]:


df['분야명'].value_counts()


# In[6]:


import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from konlpy.tag import Okt
data = pd.read_csv("국민권익위원회 경진 대회 데이터.csv", encoding="CP949")

okt = Okt()


# In[7]:


all_complain_list = data['질문내용'].values.tolist()
all_complain_list

complain_list = []

for title in all_complain_list:
    tokens = okt.morphs(title)
    complain_list.append(tokens)
    
# 불용어 사전 텍스트 파일을 오픈

korean_stopwords_path = "불용어.txt"

with open(korean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]    


title = []

for i in range(len(complain_list)):
    for j in range(len(complain_list[i])):
        if complain_list[i][j] not in stopwords:
            title.append(complain_list[i][j])
title

import re

title_word = [re.sub('[^A-Za-z가-힣0123456789]', '', i) for i in title]
title_word.remove('')
title_word

#가장 많이 쓰이는 단어 200개 추출한다.
from collections import Counter

count_title_word = Counter(title_word).most_common(200)
del count_title_word[0]
count_title_word

# # 한글자 단어 제거한다.
count_title_word = [(tup[0], tup[1]) for tup in count_title_word if len(tup[0]) > 1]
count_title_word

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from wordcloud import STOPWORDS

def wordcloud(data, width=1200, height=500):
    word_draw = WordCloud(
        font_path=r"C:\Windows\Fonts\malgun.ttf" ,
        width=width, height=height,
        stopwords=stopwords, 
        background_color="white",
        random_state=42
    )
    word_draw.generate(data)

    plt.figure(figsize=(15, 7))
    plt.imshow(word_draw)
    plt.axis("off")
    plt.show()
    
title_word_cloud = str(count_title_word)    

title_word_cloud=wordcloud(title_word_cloud, width=1200, height=500)
title_word_cloud


# ### 민원데이터 질문내용은 신청, 신고 허가, 서류가 많다
# => 신고의 단어의 크기가 큼

# # 주차, 단속의 문제점이 많다고 생각함

# In[22]:


df['최상위기관명'].value_counts()
#경찰청          416
#국토교통부        219
#해양수산부        130
#충청북도 충주시     121
#서울특별시        105


# In[25]:


df_police = df[df['최상위기관명']=='경찰청']
df_police

all_complain_list = df_police['질문내용'].values.tolist()
all_complain_list

complain_list = []

for title in all_complain_list:
    tokens = okt.morphs(title)
    complain_list.append(tokens)
    
# 불용어 사전 텍스트 파일을 오픈

korean_stopwords_path = "불용어.txt"

with open(korean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]    


title = []

for i in range(len(complain_list)):
    for j in range(len(complain_list[i])):
        if complain_list[i][j] not in stopwords:
            title.append(complain_list[i][j])
title

import re

title_word = [re.sub('[^A-Za-z가-힣0123456789]', '', i) for i in title]
title_word.remove('')
title_word

#가장 많이 쓰이는 단어 200개 추출한다.
from collections import Counter

count_title_word = Counter(title_word).most_common(200)
del count_title_word[0]
count_title_word

# # 한글자 단어 제거한다.
count_title_word = [(tup[0], tup[1]) for tup in count_title_word if len(tup[0]) > 1]
count_title_word


# In[ ]:




