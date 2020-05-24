import requests
url = 'https://www.timeshighereducation.com/student/best-universities/best-universities-united-states#survey-answer'

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
r = requests.get(url, headers = header)
print(r.content.decode())

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('tr')
results = results[1:90]
records = []

for result in results:
    us = result.contents[0].text
    world = result.contents[2].text
    university = result.contents[4].text
    city = result.contents[6].text
    state = result.contents[8].text
    records.append((us, world,university,city,state))



import pandas as pd
df1 = pd.DataFrame(records, columns=['US Rank 2020','World University Rank 2020','University',"City","State"])
df1.to_excel("University.xlsx", sheet_name="University ranking")
import os
# results1 = results[0]
# print(results1)
# item1 = results1.contents[0].text
# item2 = results1.contents[2].text
# item3 = results1.contents[4].text
# item4 = results1.contents[6].text
# item5 = results1.contents[8].text
# results1 = results[0]
# results2 = results[1]
# item1 = results1.contents[0].text
# item2 = results1.contents[2].text
# item3 = results1.contents[4].text
# item4 = results1.contents[6].text
# item5 = results1.contents[8].text
# item21 = results2.contents[0].text
# item22 = results2.contents[2].text
# item23 = results2.contents[4].text
# item24 = results2.contents[6].text
# item25 = results2.contents[8].text





