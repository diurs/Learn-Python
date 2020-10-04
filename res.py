class Rest():
	def __init__(s, res_name, cuisine_type):
		s.res_name = res_name
		s.cuisine_type = cuisine_type

	def describe(s):
		print(s.res_name)
		print(s.cuisine_type)

	def open(s):
		print(str(s.res_name) + ' is open')
restaurant = Rest('Moxiti' , '1')
restaurant.describe()
restaurant.open()
	
