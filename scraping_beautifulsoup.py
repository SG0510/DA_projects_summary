import requests
from bs4 import BeautifulSoup
htmlObj = requests.get("https://junocollege.com/course/data-analytics/")

soup = BeautifulSoup(htmlObj.text,'html.parser')
m_list = soup.find_all('meta')


## what we craping
# title, h1,h2,h3, meta,discrption, key words, og , twitter

# Stored by JSON type of data

print(soup.title)
# date = soup.find_all('title')
#
#
seo_data ={'data':{'2023-05-07':[],'2023-06-07':[]}}

cur_date_note = seo_data['data']['2023-06-07']
cur_date_note['meta'] = {}

for tag in ['title','h1','h2','h3']:
      data = soup.find_all(tag)
      cur_date_note.append({tag:data[0].text})


data = soup.find_all('meta',{'name':'description'})
cur_date_node = seo_data['meta']['description']=data[0]['content']
data = soup.find_all('meta',{'name':'keywords'})
if data != []:
      cur_date_node['meta']['keywords']=data[0]['content']

# data = soup.find_all('title')

print(seo_data)
