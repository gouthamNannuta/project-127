from bs4 import BeautifulSoup
import time 
import csv
import requests

start_url='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
headers=['proper_Name','Distance','Mass','Radius']
planet_data=[]
new_planet_data = []

planet_data.append(start_url)

def scrape_more_data(hyperlink):
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []
        for th_tag in soup.find_all("th"):
            tr_tags = th_tag.find_all("tr")
            for tr_tag in tr_tags:
                try:
                    temp_list.append(tr_tag.find_all("td"))
                except:
                    temp_list.append("")
        new_planet_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)

#scrape_more_data()
for index, data in enumerate(planet_data):
    scrape_more_data(data[5])
    print(f"{index+1} page done 2")
final_planet_data = []

for index, data in enumerate(planet_data):
    new_planet_data_element = new_planet_data[index]
    new_planet_data_element = [elem.replace("\n", "") for elem in new_planet_data_element]
    new_planet_data_element = new_planet_data_element[:7]
    final_planet_data.append(data + new_planet_data_element)
with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_planet_data)
