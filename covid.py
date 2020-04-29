#importing libraries

import requests
import bs4
import plyer
import tkinter as tk
import time 
import datetime


# defininfg functions
def get_data(url):

	data = requests.get(url)
	return data


def get_corona_details_india():
	url = "https://www.mohfw.gov.in/"

	html_view = get_data(url)

	#use of beautifulsoup

	bs = bs4.BeautifulSoup(html_view.text , 'html.parser')
	# print(bs.prettify())
	info_div = bs.find("div" , class_ = "site-stats-count")

	print(info_div.prettify())








def main():

	get_corona_details_india()



if __name__ == '__main__':
		main();





