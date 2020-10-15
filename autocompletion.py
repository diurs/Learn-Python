import collections
quantity= int(input())
strok= input()
all_words= strok.split()
dictionary = []
summa=[]

#print(len(all_words))

def haha():
	for i in range(len(all_words)):
		if len(dictionary) == 0 or dictionary.count(all_words[i]) == 0:
			dictionary.append(all_words[i])
			#print('Слова, которые добавим в словарь: ', all_words[i])
			summa.append(len(all_words[i]))

		else:
			if dictionary.count(all_words[i]) == 1:
				print('Слово для автодополнения:  ', all_words[i])
				m=list(all_words[i])
				tmp_sravn=[]
				for d in m:
					tmp_sravn.append(d)
					stroka = ''.join(map(str,tmp_sravn))
					keks=[]
					for w in dictionary:
						sr= w.startswith(stroka)
						if sr is True:
							keks.append(w)

					if len(keks)==1:
						#print('подходящее: ', keks)
						summa.append(len(stroka))
						break		
	print(sum(summa))

if __name__ == "__main__":
	if len(all_words) == quantity:
		haha()
	






