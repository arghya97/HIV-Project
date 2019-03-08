from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep

def modify_links(links):
    path = 'https://www.newsday.com'
    for i in range(len(links)):
        if links[i][0]=='/':
            links[i]= path+links[i]
    return links
def get_driver(link):
    driver = webdriver.Chrome()
    driver.get(link)
    search_field = driver.find_element_by_xpath('//*[@id="searchbox"]/div/form/input')
    search_field.send_keys('HIV')
    sleep(5)
    return driver
def load_page(driver):
    t=0
    found = True
    while(found):
        t+=1
        try:
            driver.find_element_by_xpath('//*[@id="hits"]/div/button').click()
            sleep(5)
        except:
            found = False
        print(t,end='')
    page = driver.page_source
    return page
def get_links(html):
    links = []
    soup = bs(html,'html.parser')
    articles = soup.find_all('div',class_='article')
    
    for article in articles:
        lnk = article.a.get('href').strip()
        links.append(lnk)
    return links


link = 'https://www.newsday.com/search'
driver = get_driver(link)

loaded_page = load_page(driver)
raw_links = get_links(loaded_page)
mod_links = modify_links(raw_links)

with open('article_links.txt','w') as fl:
    fl.write('\n'.join(mod_links))
driver.quit()
