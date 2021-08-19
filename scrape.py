from os import error
from bs4 import BeautifulSoup
import requests
import csv
from requests.models import Response
 
arr= []
csv_file = open('bb_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['S.no', 'Name', 'Adress', 'Phone','Fax', 'Email'])

short_url = 'https://www.eraktkosh.in/BLDAHIMS/bloodbank/nearbyBB.cnt?hmode=GETNEARBYSTOCKDETAILS&stateCode=-1&districtCode=-1&bloodGroup=all&bloodComponent=11&lang=0&_=1629287944696'
response = requests.get(short_url)
response.raise_for_status()
entry = response.json()['data']

for i in range(0, len(entry)):
    try:
        flag = 0
        #serial number
        s_number = entry[i][0]
        #details - name + adress
        details = entry[i][1].split('<br/>')
        name = details[0]
        adress = details[1]
        #phone mail and fax
        if details[2] != 'null':
            string = details[2].replace('Phone: ','?')  
            string2 = string.replace(',Fax: ','?')
            string3 = string2.replace('Email: ','?')

            phone = string3.split('?')[1]
            fax = string3.split('?')[2].replace(',',' ')
            email = string3.split('?')[3]
            flag = 1
        
        if flag == 0:
            phone = '-'
            email = '-'
            fax = '-'

        csv_writer.writerow([s_number,name,adress,phone,fax,email])
        
    except:
        arr.append(i)

csv_file.close()
print(arr)