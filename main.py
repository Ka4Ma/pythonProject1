import pandas as pd
import requests
data1 = pd.read_csv('IP.csv')
data2 = pd.read_csv('full_blacklist_database.csv')
url1 = "https://api.hetrixtools.com/v2/"
url2 = "/blacklist-check/ipv4/"
API = input("Paste your API: ")
Blacklist = {}
for row in data1.itertuples():
    IP = row.IP
    #print(IP)
    #print(url1+str(API)+url2+str(IP)+"/")
    response = requests.get(url1+str(API)+url2+str(IP)+"/")
    file = response.json()
    for item in file:
        IP_details = {"blacklisted_count":None}
        IP_details['blacklisted_count'] = item['blacklisted_count']
        if IP_details.values() >= 0:
            Blacklist.append(item)
print(Blacklist)
