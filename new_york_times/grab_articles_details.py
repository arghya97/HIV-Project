from newspaper import Article
import pandas as pd
import datetime
from time import sleep

def get_links():
    with open('article_links.txt','r') as fl:
        links = fl.readlines()
    return links
def article_details(link):
    f={}
    article = Article(link)
    article.download()
    article.parse()
    f['headline'] = article.title
    date = article.publish_date
    f['publish_date'] = date.strftime('%d/%m/%Y')
    f['newspaper_name'] = 'The New York Times'
    f['article_text']= article.text
    return f

def get_df(links):
    l=[]
    for i,link in enumerate(links):
        try:
            l.append(article_details(link))
            sleep(2)
            print(i,end='')
        except:
            pass
    df = pd.DataFrame(l)
    df = df[['newspaper_name','headline','article_text','publish_date']]
    df.to_csv('nytimes.csv',index=False)

links = get_links()
get_df(links)
