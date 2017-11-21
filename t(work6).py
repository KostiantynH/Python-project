#----------------------------------------
import os
os.system('cls')
print('\n\t Start')
#----------------------------------------
import requests
import csv
import re
from bs4 import BeautifulSoup


def get_html(url):
	r = requests.get(url)
	return r.text

def get_last_page(html):
	soup = BeautifulSoup(html, 'lxml')
	pages = soup.find('div', class_ = 'pager rel clr').find_all('a', class_ = 'block br3 brc8 large tdnone lheight24')[-1].get('href')
	last_page = pages.split('=')[-1]
	return int(last_page)
	
def write_csv(data):
	with open('olx.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow((data['title'],';'+data['price'],';'+data['location'],';'+data['time'],';'+data['url']))
	
def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	ads = soup.find('table', class_ = 'fixed offers breakword ').find_all('tr', class_ = 'wrap')
	
	for ad in ads:
		#title, price, location, url, time
		try:
			title = ad.find('strong').text	
		except:
			title = ''
	
		try:
			price = ad.find('p', class_ = 'price').text
			price = re.sub('\n','',price)
			price = re.sub('  ','',price)
		except:
			price = ''	
		
		try:
			location = ad.find('p', class_ = 'color-9 lheight16 marginbott5').text
			location = re.sub('\n','',location)
			location = re.sub('  ','',location)		
		except:
			location = ''

		try:
			time = ad.find('p', class_ = 'color-9 lheight16 marginbott5 x-normal').text
			time = re.sub('\n','',time)
			time = re.sub('  ','',time)
		except:
			time = ''
			
		try:
			url = ad.find('a', class_ = 'marginright5 link linkWithHash detailsLink').get('href')
			url = re.sub(';promoted','',url)
		except:
			url = ''
		
		data={'title':title, 'price':price, 'location':location, 'time':time, 'url':url}
		write_csv(data)
	return int(len(ads))
	
def main():
	ads_sum = 0
	url_base = 'https://www.olx.ua/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/apple'
	url_query = '/q-iphone-X'
	url_page = '/?page='
	last_page = get_last_page(get_html(url_base+url_query))
	
	#for i in range(1, last_page+1):
	for i in range(1, 2):
		url_gen = url_base + url_query + url_page + str(i)
		#print(url_gen)#----------------------------------------
		html = get_html(url_gen)
		ads_sum+=get_page_data(html)
	
	
	
	print ("ads found", ads_sum)
	
	
if __name__ == '__main__':
	main()

#----------------------------------------
print('\t End')
#----------------------------------------
