'''
part 2

a - для создания ссылок

href -  адрес документа url , на который происходит переход

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 
import random

def get_links(articleUrl):

	html = urlopen("https://en.wikipedia.org" + articleUrl)

	a = BeautifulSoup(html , features = "html.parser")


	return a.find("div" , {"id" : "bodyContent" } ).findAll("a" , href = re.compile("^(/wiki/)((?!:).)*$"))
	
	#print("список всех URL-адресов статей , с которыми связана данная статья")

ssilki = get_links("/wiki/Apollo_program")

while len(ssilki) > 0:
	newZagolovok = ssilki[random.randint(0, len(ssilki)-1 ) ].attrs["href"]
	print(newZagolovok)
	ssilki = get_links(newZagolovok)









