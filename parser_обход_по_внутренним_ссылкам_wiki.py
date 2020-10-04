'''
part 2

a - для моздания ссылок в html

href -  адрес документа url , на который происходит переход

прога  проходит только 1 раз по статьям Вики , без повторных проходов 

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 

pages = set()

'''
set() - множество. Контейнер, который содержит не повторяющиеся элементы в случайном порядке

ищем внутренние нужные ссылки, начинающиеся с /wiki/

страница-статья не содержит :

страница загрузки файлов, обсуждений содержит

'''
def get_links(Url):
	global pages
	html = urlopen("https://en.wikipedia.org" + Url)
	a = BeautifulSoup(html , features = "html.parser")

	for lin in  a.findAll("a" , href = re.compile("^(/wiki/)")):

#глобальный набор страниц , определенных скриптом
		if 'href' in lin.attrs:

			if lin.attrs['href'] not in pages:
				new_page = lin.attrs['href']
				print(new_page)
				pages.add(new_page)
# рекурсивно вызывается
				get_links(new_page)
get_links(" ")











