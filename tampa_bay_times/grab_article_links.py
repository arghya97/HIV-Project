from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep

def modify_links(links):
    path = 'https://www.tampabay.com'
    for i in range(len(links)):
        if links[i][0]=='/':
            links[i]= path+links[i]
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
    t=1
    found = True
    while(found):
        t+=1
        try:
            links+=get_links_from_page(driver.page_source)
            driver.find_element_by_xpath('//*[@id="sectionFrontListWrapper"]/div[3]/div[2]/span[2]/a')
            next_page = link+'&PageNumber={}'.format(t)
            driver.get(next_page)
            sleep(2)
        except :
            found = False
        print(t,end='')
    driver.quit()
    return links
def get_links_from_page(html):
    links = []
    soup = bs(html,'html.parser')
    container = soup.find('div',class_='section-front__story-feed super-donut-item-container').div
    for article in container.find_all('li'):
        lnk = article.a.get('href').strip()
        links.append(lnk)
    return links


link = 'http://www.tampabay.com/section/search?q=HIV'
driver = get_driver(link)

raw_links = get_all_links(driver)
mod_links = modify_links(raw_links)

with open('article_links.txt','w') as fl:
    fl.write('\n'.join(mod_links))

