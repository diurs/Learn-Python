from ccar import Car
from ccar import ElCar

new_car = Car('bmw' , 'x4')
#used_car= Car('toyota' , 'rx')

print(new_car.opisanie())
new_car.odometr()
# прямое
new_car.odometrr = 2
new_car.odometr()
new_car.update(1)
new_car.odometr()

new_car.update(1222)
new_car.odometr()
new_car.u(86)
new_car.odometr()
new_car.gas()

tesla = ElCar('S ' , '2021')
print('tesla ' + tesla.opisanie())
tesla.gas()
dir(Car)
