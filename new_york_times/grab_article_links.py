from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep

def modify_links(links):
    path = 'https://www.nytimes.com'
    for i in range(len(links)):
        if links[i][0]=='/':
            links[i]= path+links[i]
    return links
def get_driver(link):
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(link)
    return driver
def load_page(driver):
    t=0
    found = True
    while(found):
        t+=1
        try:
            driver.find_element_by_xpath('//*[@id="site-content"]/div/div[2]/div[3]/div/button').click()
            sleep(2)
        except:
            found = False
        print(t,end='\r')
    page = driver.page_source
    driver.quit()
    return page
def get_links(html):
    links = []
    soup = bs(html,'html.parser')
    articles = soup.find_all('div',class_='css-138we14')
    
    for article in articles:
        lnk = article.a.get('href').strip()
        links.append(lnk)
    return links


link = 'https://www.nytimes.com/search?query=HIV&sort=best&startDate=20000101'
driver = get_driver(link)

loaded_page = load_page(driver)
raw_links = get_links(loaded_page)
mod_links = modify_links(raw_links)

with open('article_links.txt','w') as fl:
    fl.write('\n'.join(mod_links))
