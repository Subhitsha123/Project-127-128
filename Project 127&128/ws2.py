from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

temp_list= []

table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Names = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
    
    Names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(Names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df)

df.to_csv('final_dwarf.csv')