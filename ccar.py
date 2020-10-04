class Car():
	def __init__(sek, model, year):
		sek.model = model
		sek.year = year
#по умолчанию
		sek.odometrr = 0
	def odometr(sek):
		print('miles 0s ' + str(sek.odometrr))

	def opisanie(sek):
		name = str(sek.year) + ' ' + sek.model
		return name
	def update(sek , znachenie):
		sek.odometrr = znachenie
	def u(sek, z):
		sek.odometrr += z
	def gas(sek):
		print(sek.model + ' требуется бензин')


class Characteristics():
	def __init__(sek, battery = 5 , price = 53):
		sek.battery = battery
		sek.price = price

	def pricee(sek):
		print('Экземпляр в качестве атрибута')
		print('цена авто : ' + str(sek.price))

	def bat(sek):
		print('Экземпляр в качестве атрибута')
		print('емкость : ' + str(sek.battery) + ' kwh ')

class ElCar(Car):
	def __init__(sek, model , year):
		super().__init__(model , year)

		sek.characteristics = Characteristics()

	def gas(sek):
		print('\n переопредееление класса-родителя \n')
		print('This car doesn t need a gas')

