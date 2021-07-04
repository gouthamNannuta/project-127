from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

start_url='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser=webdriver.Chrome('chromedriver')
browser.get(start_url)
time.sleep(10)

def scrape():
    headers=['proper_Name','Distance','Mass','Radius']
    stars_data=[]
    for i in range(0,20):
        soup=BeautifulSoup(browser.page_source, 'html.parser')
        for tr_tag in soup.find_all('tr'):
            td_tags=tr_tag.find_all("td")
            temp_list=[]
            for index,td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("span")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            stars_data.append(temp_list)
with open ("scrape_data.csv","w") as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
scrape()


                