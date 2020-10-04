class Dog():
	def __init__(sek, name , age):
		sek.name = name
		sek.age = age
	def sleep(sek):
		print(sek.name.title() + 'sleep all days at home')

	def agge(sek):
		print(str(sek.name) + ' is ' + str(sek.age) + ' years old')
#экземпляр
new_dog = Dog('Seed' , 1)
print('age: ' + str(new_dog.age))

new_dog.agge()
	
