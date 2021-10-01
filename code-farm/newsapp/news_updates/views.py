from django.shortcuts import render
from newsapi import NewsApiClient


def Index(request):
    newsapi = NewsApiClient(api_key='dde538d14c8d41fbb0a43959159d1b95')

    topheadlines = newsapi.get_top_headlines(sources='bbc-news,the-verge')
    articles = topheadlines['articles']

         
    desc = []
    news = []
    img = []
   

    for i in range(len(articles)):
        myarticles = articles[i] 

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        


    
    mylist = zip(news, desc, img)

    return render(request, 'index.html', context = {"mylist": mylist})

