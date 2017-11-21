#----------------------------------------
import os
os.system('cls')
print('\n\t Start')
#----------------------------------------
import requests
from bs4 import BeautifulSoup

def get_html(url):
	r = requests.get(url)
	return r.text

def get_last_page(html):
	soup = BeautifulSoup(html, 'lxml')
	pages = soup.find('div', class_ = 'pager rel clr').find_all('a', class_ = 'block br3 brc8 large tdnone lheight24')[-1].get('href')
	last_page = pages.split('=')[-1]
	return int(last_page)
	
def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	ads = soup.find('table', class_ = 'fixed offers breakword ').find_all('tr', class_ = 'wrap')
	print(len(ads))
	
	for ad in ads:
		#title, price, location, url, time
		try:
			title = ad.find('strong').text	
			print(type(title), '\ttitle\t' ,title)#----------------------------------------
		except:
			title = ''
	
		try:
			price = ad.find('p', class_ = 'price').text
			print(type(price), '\tprice\t' ,price)#----------------------------------------
		except:
			price = ''	
		
		try:
			location = ad.find('p', class_ = 'color-9 lheight16 marginbott5').text
			print(type(location), '\tlocation\t' ,location)#----------------------------------------
		except:
			location = ''
		
		try:
			url = ad.find('a', class_ = 'marginright5 link linkWithHash detailsLink').get('href')
			print(type(url), '\turl\t' ,url)#----------------------------------------
		except:
			url = ''
		
		try:
			time = ad.find('p', class_ = 'color-9 lheight16 marginbott5 x-normal').text
			print(type(time), '\ttime\t' ,time)#----------------------------------------
		except:
			time = ''			 

	

	

	


	#my_file = open("some.txt", "w")
	#my_file.write(title + price + location + url + time)
	#my_file.close()
	
	
	
def main():
	url_base = 'https://www.olx.ua/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/apple'
	url_query = '/q-iphone-X'
	url_page = '/?page='
	last_page = get_last_page(get_html(url_base+url_query))
	
	#for i in range(1, last_page+1):
	for i in range(1, 2):
		url_gen = url_base + url_query + url_page + str(i)
		#print(url_gen)#----------------------------------------
		html = get_html(url_gen)
		get_page_data(html)
	
	
	
	
	
	



	

	
	
	
if __name__ == '__main__':
	main()

#----------------------------------------
print('\t End')
#----------------------------------------
