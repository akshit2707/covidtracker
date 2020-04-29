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

	print(html_view.text)



get_corona_details_india()





