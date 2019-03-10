from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep

def modify_links(links):
    path = 'https://www.seattletimes.com'
    for i in range(len(links)):
        try:
            if links[i][0]=='/':
                links[i]= path+links[i]
        except:
            pass
    return links
def get_driver(link):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)
    return driver
def get_all_links(driver):
    links=[]
    links+=get_links_from_page(driver.page_source)
    driver.find_element_by_xpath('//*[@id="pagination"]/div/a').click()
    sleep(3)
    t=1
    found = True
    while(found):
        t+=1
        try:
            links+=get_links_from_page(driver.page_source)
            driver.find_element_by_xpath('//*[@id="pagination"]/div[2]/a').click()
            sleep(3)
        except :
            found = False
        print(t,end='')
    driver.quit()
    return links
def get_links_from_page(html):
    links = []
    soup = bs(html,'html.parser')
    articles = soup.find_all('div',class_='results-story')
    for article in articles:
        lnk = article.a.get('href').strip()
        links.append(lnk)
    return links


link = 'https://www.seattletimes.com/search/?query=HIV&startdate=2000-01-01&enddate=2019-12-31&types[]=article&sections[]=life&sections[]=seattle-news&sections[]=nation-world&sections[]=news&sortby=mostrecent&page=1&perpage=200'
driver = get_driver(link)

raw_links = get_all_links(driver)
mod_links = modify_links(raw_links)

with open('article_links.txt','w') as fl:
    fl.write('\n'.join(mod_links))

