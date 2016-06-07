import requests
from urllib.parse import urlencode
from os.path import join, basename
from bs4 import BeautifulSoup
from os import makedirs

counties = ["Alameda","Butte","Los Angeles","Marin","Orange","Placer","Riverside","Sacramento","San Bernardino","San Francisco","San Joaquin","San Luis Obispo","San Mateo","Santa Clara","Ventura","Monterey","Nevada","Santa Barbara","Contra Costa","Fresno","Kern","Mendocino","Merced","San Benito","San Diego","Santa Cruz","Sonoma","Shasta","Tuolumne","El Dorado","Napa","Trinity","Sierra","Tulare","Alpine","Colusa","Del Norte","Imperial","Inyo","Solano","Kings","Amador","Calaveras","Glenn","Humboldt","Madera","Modoc","Mono","Plumas","Siskiyou","Stanislaus","Lake","Lassen","Mariposa","Tehama","Yolo","Yuba","Sutter"]

index_link = 'http://www.meganslaw.ca.gov/cgi/prosoma.dll?w6=224629&searchby=CountyList&SelectCounty='
end = '&SB=0&PageNo='
page_no = 1

makedirs('pages', exist_ok=True)

# def get_index(url):
#     resp = requests.get(url)
#     txt = resp.text
#     with open(index_name, 'w') as w:
#         w.write(txt)

county = 'Alameda'

path = 'pages/' + county
makedirs(path,exist_ok=True)
county = county.upper()
county.replace(' ', '%20')

url = index_link + county + end + str(page_no)

r = requests.get(url)
text = r.text

soup = BeautifulSoup(text, 'lxml')
a = soup.select('table > a')
last = int(a[-4].text)

for page_no in range(1, last + 1):
	url = index_link + county + end + str(page_no)
	resp = requests.get(url)
	fpath = path + '/' + str(page_no)
	with open(fpath, 'w') as w:
		w.write(resp.text)



# Loop through each county
# for county in counties:
# 	path = 'pages/' + county
# 	makedirs(path,exist_ok=True)
# 	county = county.upper().replace(' ', '%20') #encoding for URL

# 	url = index_link + county + end + page_no
# 	makedirs(path)

