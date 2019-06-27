from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def index(request):
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=ebe856c106e546d6b6670b3181d1212c'
    newsapi = NewsApiClient(api_key='ebe856c106e546d6b6670b3181d1212c')
    top=newsapi.get_top_headlines(sources='the-times-of-india,the-hindu')
    l=top['articles']
    desc=[]
    news=[]
    img=[]
    u=[]
    for i in range(len(l)):
        f=l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        u.append(f['url'])
    mylist = zip(news, desc,img,u)
    return render(request,'index.html',context={"mylist":mylist})

def international(request):
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=ebe856c106e546d6b6670b3181d1212c'
    newsapi = NewsApiClient(api_key='ebe856c106e546d6b6670b3181d1212c')
    top=newsapi.get_top_headlines(sources='bbc-news,the-verge,abc-news,al-jazeera-english')
    l=top['articles']
    desc=[]
    news=[]
    img=[]
    u=[]
    for i in range(len(l)):
        f=l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        u.append(f['url'])
    mylist = zip(news, desc,img,u)
    return render(request,'international.html',context={"mylist":mylist})

def tech(request):
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=ebe856c106e546d6b6670b3181d1212c'
    newsapi = NewsApiClient(api_key='ebe856c106e546d6b6670b3181d1212c')
    top=newsapi.get_top_headlines(sources='techcrunch,techradar,crypto-coins-news,techcrunch-cn')
    l=top['articles']
    desc=[]
    news=[]
    img=[]
    u=[]
    for i in range(len(l)):
        f=l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        u.append(f['url'])
    mylist = zip(news, desc,img,u)
    return render(request,'tech.html',context={"mylist":mylist})


def sports(request):
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=ebe856c106e546d6b6670b3181d1212c'
    newsapi = NewsApiClient(api_key='ebe856c106e546d6b6670b3181d1212c')
    top=newsapi.get_top_headlines(sources='fox-sports,bbc-sport,espn-cric-info,talksport')
    l=top['articles']
    desc=[]
    news=[]
    img=[]
    u=[]
    for i in range(len(l)):
        f=l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        u.append(f['url'])
    mylist = zip(news, desc,img,u)
    return render(request,'sports.html',context={"mylist":mylist})
