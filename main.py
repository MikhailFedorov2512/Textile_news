import requests
from bs4 import BeautifulSoup
import pandas as pd





def nordtex():
  url = 'https://www.nord-tex.ru/press-tsentr/'
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  resultlist =[]
  dateresult = []
  dateresultformated = []
  dataformated = ''
  titleresult = []
  urlresult = []
  nord=[]

  dates = soup.select(".news-item__date")
  for item in dates:
    soup1=BeautifulSoup(str(item), 'html.parser')
    datesresult=soup1.p.text
    dateresult.append(datesresult)
  for i in dateresult:
    formateddate = i.split(" ")
    for item in formateddate:
      if item!= '':
        dataformated+=item +' '
    dateresultformated.append(dataformated[:-1])
    dataformated=''



  titles = soup.select(".news-item__title")
  for item in titles:
    soup1=BeautifulSoup(str(item), 'html.parser')
    titles=soup1.p.text
    titleresult.append(titles.strip())

  urls = soup.select(".news-item")
  for item in urls:
    soup1=BeautifulSoup(str(item), 'html.parser')
    link=soup1.a.get('href')
    urlresult.append('https://www.nord-tex.ru'+link)
  for i in range(len(dateresultformated)):
    nord.append('Нордтекс')
  resultlist  = (zip(nord,titleresult,dateresultformated,urlresult))
  df = pd.DataFrame(list(resultlist))
  return df

def baltiiskiy_tekstil():
  url = 'https://balttex.ru/novosti/'
  result = requests.get(url)
  resultlist=[]
  soup = BeautifulSoup(result.text, 'html.parser')
  result = soup.select(".body-info")
  for item in result:
    soup1=BeautifulSoup(str(item), 'html.parser')
    link = soup1.a.get('href')
    link='https://balttex.ru'+link
    title = soup1.a.text
    title = title.strip()
    date = soup1.span.text
    resultlist.append(['Балтийский текстиль',title,date,link])
    df = pd.DataFrame(resultlist)
  return df

def textime():
  url = 'https://www.textime.ru/news/'
  headers = requests.utils.default_headers()
  headers.update(
    {
      'User-Agent': 'My User Agent 1.0',
    }
  )
  result = requests.get(url, headers=headers, verify = False)
  resultlist=[]
  titles=[]
  dates=[]
  links=[]
  name=[]
  soup = BeautifulSoup(result.text, 'html.parser')
  result = soup.select(".article")
  for item in result:
    soup1=BeautifulSoup(str(item), 'html.parser')
    link=item.a.get('href')
    links.append('https://www.textime.ru'+link)
    title = soup1.select(".name")
    dates.append(soup1.div.div.text)
    for item in title:
      titles.append(item.text)
      name.append('Текстайм')
  df = pd.DataFrame(list((zip(name,titles,dates,links))))
  return df

def mirteks():
  url = 'https://www.mirtex.ru/novosti/'
  result = requests.get(url)
  resultlist=[]
  titles=[]
  dates=[]
  links=[]
  name=[]
  soup = BeautifulSoup(result.text, 'html.parser')
  result = soup.select(".wrapper-post")
  for item in result:
    soup1=BeautifulSoup(str(item), 'html.parser')
    link = item.a.get('href')
    links.append(link)
    title=item.a.text
    titles.append(title)
    date = soup1.span.time.text
    dates.append(date)
  for i in range(len(dates)):
    name.append('Миртекс')
  df = pd.DataFrame(list((zip(name,titles,dates,links))))
  return df
def raiteks():
  url = 'https://raiteks.ru/novosti/'
  result = requests.get(url)
  resultlist=[]
  titles=[]
  dates=[]
  links=[]
  name=[]
  soup = BeautifulSoup(result.text, 'html.parser')
  result = soup.select(".info_news")
  for item in result:
    soup1=BeautifulSoup(str(item), 'html.parser')
    title =soup1.div.div.text
    s=title.split(' ')
    titleresult=''
    for i in s:
      if i!='\r\n' and i!='':
        titleresult+=i+' '
    titles.append(titleresult)
    titleresult=''
    link =soup1.div.a.get('href')
    links.append(link)
    res = soup1.select(".news_date")
    for i in res:
      s=i.text
      splitted = s.split(' ')
      resultdate=''
      for i in splitted:
        if i!='\r\n' and i!=' ':
          resultdate+=i
      dates.append(resultdate)
      resultdate=''
  for i in range(len(dates)):
    name.append('Райтекс')
  df = pd.DataFrame(list((zip(name,titles,dates,links))))
  return df

def mogotex():
  url = 'https://mogotex.com/info/news/'
  headers = requests.utils.default_headers()
  headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
  )
  result = requests.get(url,headers=headers)
  resultlist=[]
  titles=[]
  dates=[]
  links=[]
  name=[]
  soup = BeautifulSoup(result.text, 'html.parser')
  result = soup.select(".body-info")
  for item in result:
    soup1=BeautifulSoup(str(item), 'html.parser')

    date = soup1.div.div.span.text
    dates.append(date)
    link = 'https://mogotex.com' + soup1.div.div.a.get('href')
    links.append(link)
    title = soup1.div.div.a.text
    titleformatted=''
    for i in title:
      if i!='\t':
        titleformatted+=i
    titles.append(titleformatted)
  for i in range(len(titles)):
    name.append('Моготекс')
  df = pd.DataFrame(list((zip(name,titles,dates,links))))
  return df
def chaikovskiy_tekstil():
  url = 'https://textile.ru/presscenter/news'
  result = requests.get(url, verify=False)
  resultlist=[]
  titles=[]
  dates=[]
  links=[]
  name=[]
  soup = BeautifulSoup(result.text, 'html.parser')
  result = soup.select(".date")

  for item in result:
    dates.append(item.text)
  result = soup.select(".name")
  for item in result:
    titles.append(item.text)
    links.append('https://textile.ru'+item.a.get('href'))
  for i in range(len(titles)):
    name.append('Чайковский текстиль')
  df = pd.DataFrame(list((zip(name,titles,dates,links))))
  return df

def shuiskie_sitcy():
  url = 'https://sitsy.ru/news/'
  result = requests.get(url)
  resultlist=[]
  titles=[]
  dates=[]
  links=[]
  name=[]
  soup = BeautifulSoup(result.text, 'html.parser')
  #print(soup)
  result = soup.select(".news-hero")
  for item in result:
    soup1 = BeautifulSoup(str(item.text), 'html.parser')
    titles.append(soup1.text.split('\n')[5])
    link =item.get('href')
    links.append('https://sitsy.ru'+link)
    res = item.select(".index-news__date")
    for item in res:
      dates.append(item.text)

  result = soup.select(".news-item")
  for item in result:
    link =item.get('href')
    links.append('https://sitsy.ru'+link)
    dates.append(item.text.split('\n')[3])
    titles.append(item.text.split('\n')[4])
  for i in range(len(titles)):
    name.append('Шуйские ситцы')
  df = pd.DataFrame(list((zip(name,titles,dates,links))))
  return df

def rutkani():
  url = 'https://rutkani.ru/news/'
  result = requests.get(url)
  resultlist=[]
  titles=[]
  dates=[]
  links=[]
  name=[]
  soup = BeautifulSoup(result.text, 'html.parser')
  result = soup.select(".bx-newslist-title")
  for item in result:
    links.append('https://rutkani.ru'+item.a.get('href'))
    titles.append(item.text.split('\n')[1])

  result = soup.select(".bx-newslist-date")
  for item in result:
    dates.append(item.text)
  for i in range(len(titles)):
    name.append('Руткани')
  df = pd.DataFrame(list((zip(name,titles,dates,links))))
  return df

def balteks_balashov():
  resultlist=[]
  titles=[]
  dates=[]
  links=[]
  name=[]
  for i in range(0,70,5):
    url = f'https://www.newbaltex.ru/news.html?start={i}'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    result = soup.select(".news-block")
    for item in result:
      date = item.p.text
      dates.append(date)
      link = item.a.get('href')
      links.append(link)
      title = item.a.text
      titles.append(title)
  for i in range(len(titles)):
    name.append('Балтекс Балашов')
  df = pd.DataFrame(list((zip(name,titles,dates,links))))
  return df

def russkiy_dom():
  url = 'https://tkrusdom.ru/news/'
  result = requests.get(url)
  result.encoding = 'utf8'
  resultlist=[]
  titles=[]
  dates=[]
  links=[]
  name=[]
  soup = BeautifulSoup(result.text, 'html.parser')
  result = soup.select(".insection-offer-unit")
  for item in result:
    link = 'https://tkrusdom.ru' + item.a.get('href')
    links.append(link)
    date = item.a.div.span.text
    dates.append(date.strip())
    title = (item.text.split('\n')[5])
    titles.append(title)
  for i in range(len(titles)):
    name.append('Русский дом')
  df = pd.DataFrame(list((zip(name,titles,dates,links))))
  return df


russkiy_dom = russkiy_dom()
balteks_balashov = balteks_balashov()
rutkani = rutkani()
shuiskie_sitcy = shuiskie_sitcy()
chaikovskiy_tekstil = chaikovskiy_tekstil()
mogotex = mogotex()
raiteks = raiteks()
mirteks = mirteks()
baltiiskiy_tekstil = baltiiskiy_tekstil()
textime=textime()
nordtex=nordtex()
resultdf=pd.concat([baltiiskiy_tekstil,nordtex,mirteks,raiteks,mogotex, textime,chaikovskiy_tekstil,shuiskie_sitcy,rutkani,balteks_balashov,russkiy_dom])
resultdf.to_csv('result.csv', index=False,encoding='utf-8',header=['компания','новость','дата','ссылка'])
