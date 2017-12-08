from datetime import datetime
import os
import requests
import csv
import re
from bs4 import BeautifulSoup

from tkinter import *

url_base = 'https://www.olx.ua/elektronika/telefony-i-aksesuary/mobilnye-telefony-smartfony/apple'
url_query = '/q-iphone-X'
url_query_for_print = re.sub('/q-','',url_query)
url_page = '/?page='


def get_html(url):
	r = requests.get(url)
	return r.text

def get_last_page(html):
	soup = BeautifulSoup(html, 'lxml')
	pages = soup.find('div', class_ = 'pager rel clr').find_all('a', class_ = 'block br3 brc8 large tdnone lheight24')[-1].get('href')
	last_page = pages.split('=')[-1]
	return int(last_page)
	
def write_csv(data):
	try:
		with open('olx.csv', 'a', newline='') as f:
			writer = csv.writer(f, delimiter=';')
			writer.writerow((data['title'],data['price'],data['location'],data['time'],data['url']))	
	except:
		print("Error: cannot open file")
		
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
	
def main(console):
	Start_working = datetime.now()

	ads_sum = 0
	last_page = get_last_page(get_html(url_base+url_query))
	
	for i in range(1, last_page+1):#last_page+1
		url_gen = url_base + url_query + url_page + str(i)
		html = get_html(url_gen)
		ads_sum+=get_page_data(html)

	Stop_working = datetime.now()
	
	label_Start_working2 = Label(root, text=Start_working)#створення текст(лейба)
	label_URL_search_site2 = Label(root, text=url_base)#створення текст(лейба)
	label_Search_query2 = Label(root, text=url_query_for_print)#створення текст(лейба)
	label_Page_number2 = Label(root, text=last_page)#створення текст(лейба)
	label_Ads_number2 = Label(root, text=ads_sum)#створення текст(лейба)
	label_Stop_working2 = Label(root, text=Stop_working)#створення текст(лейба)
	label_Worked2 = Label(root, text=Stop_working - Start_working)#створення текст(лейба)
	
	label_Ads_number2.place(x=95,y=70)#позиція
	label_Page_number2.place(x=95,y=50)#позиція
	label_URL_search_site2.place(x=95,y=10)#позиція
	label_Search_query2.place(x=95,y=30)#позиція
	label_Stop_working2.place(x=95,y=110)#позиція
	label_Start_working2.place(x=95,y=90)#позиція
	label_Worked2.place(x=95,y=130)#позиція
	
	if console == 1:
		os.system('cls')
		print('--------------------------------------------------------------------------------------------')
		print('\n\t Start working', '[', Start_working,']')
		print('URL search site: ', url_base)
		print('Search query:    ', re.sub('/q-','',url_query))
		print('Page number:     ', last_page)
		print ('Ads number:      ', ads_sum)
		print('\t Stop working', '[', Stop_working,']')
		print('\t Worked', Stop_working - Start_working)
		print('--------------------------------------------------------------------------------------------')
		input()

	
root =Tk() #створеня об'єкту вікна
root.title('Parser')#заголовок
root.geometry('580x220')#розмір
root.resizable(width=False, height=False)# выключаем возможность изменять окно

label_URL_search_site = Label(root, text='URL search site:')#створення текст(лейба)
label_Search_query = Label(root, text='Search query:')#створення текст(лейба)
label_Page_number = Label(root, text='Page number:')#створення текст(лейба)
label_Ads_number = Label(root, text='Ads number:')#створення текст(лейба)
label_Start_working = Label(root, text='Start working:')#створення текст(лейба)
label_Stop_working = Label(root, text='Stop working:')#створення текст(лейба)
label_Worked = Label(root, text='Worked:')#створення текст(лейба)

label_URL_search_site.place(x=5,y=10)#позиція
label_Search_query.place(x=5,y=30)#позиція
label_Page_number.place(x=5,y=50)#позиція
label_Ads_number.place(x=5,y=70)#позиція
label_Start_working.place(x=5,y=90)#позиція
label_Stop_working.place(x=5,y=110)#позиція
label_Worked.place(x=5,y=130)#позиція


output = Text(root, bg="lightblue", font="Arial 12", width=35, height=10)
output.place(x=255,y=30)#позиція
#output.grid(row=2, columnspan=8)
output.insert(END,'This program is designed to receive information from the OLX trading floor upon request \n \"' )
output.insert(END,url_query_for_print)
output.insert(END,'\".')

button_start = Button(root, text='start',width=15,height=3,bg="white",fg="black")#створення кнопки
button_start.bind('<Button-1>', lambda event:main(0))#прив'язка дії
button_start.place(x=5,y=155)#позиція

button_start_consol = Button(root, text='start  \n & \n log to console',width=15,height=3,bg="white",fg="black")#створення кнопки
button_start_consol.bind('<Button-1>', lambda event:main(1))#прив'язка дії
button_start_consol.place(x=130,y=155)#позиція

root.mainloop()