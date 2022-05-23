from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("C:/Users/Admin/Desktop/Purvaa coding folder/chromedriver")
browser.get(start_url)
time.sleep(10)
def scrape():
    headers=["Name","Distance","Mass","Radius"]
    star_data=[]

    
    soup=BeautifulSoup(browser.page_source,"html.parser")
    tr_tags=soup.find_all('tr')

    for i in range(1,len(tr_tags)):
        temp_list=[]
        td_tags=tr_tags[i].find_all('td')

        try:
            temp_list.append(td_tags[1].text.strip())
            temp_list.append(td_tags[3].text.strip())
            temp_list.append(td_tags[5].text.strip())
            temp_list.append(td_tags[6].text.strip())

        except:
            temp_list.append('')    

        star_data.append(temp_list)

    
    with open("scraper.csv" , "w") as f :
        csv_writer=csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(star_data)

scrape()