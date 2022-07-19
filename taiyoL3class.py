import requests
import csv
from bs4 import BeautifulSoup as bs

class Scraper:
    def __init__(self, link):
        self.url=requests.get(link)
        self.soup=bs(self.url.content,'html.parser')
        self.filename='California_Procurement.csv'
        self.csv_writer=csv.writer(open(self.filename,'w'))
    def scrap(self):
        for tr in self.soup.find_all('tr'):
            data=[]

    #for extracting table heading this will run only once
            for th in tr.find_all('th'):
                data.append(th.text)
            if(data):
                print("Inserting headers: {}".format(','.join(data)))
                self.csv_writer.writerow(data)
                continue

            #for scraping the actual table data values

            for td in tr.find_all('td'):
                data.append(td.text.strip())
            
            if(data):
                print("Inserting Table Data:{}".format(','.join(data)))
                self.csv_writer.writerow(data)
            
            #for adding metadata
            self.metak=[]
            self.metad=self.soup.find_all('meta')

            #inserting Meta Data
            for meta in self.soup.find_all('meta'):
                self.metak.append(meta)
                # print(meta)
            if(self.metak):
                with open(self.filename,'w')as f:
                    writer=csv.writer(f)
                    for val in self.metak:
                        writer.writerow([val])

sc = Scraper("https://dot.ca.gov/programs/procurement-and-contracts/contracts-out-for-bid")
sc.scrap()