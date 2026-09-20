#call asnd orbject 


# class Strudent:

#    def __init__(self,name,surename):      
#       #atributes = variable
#       self.name = name 
#       self.surname = surename
#    #add fuctionality

#    def full_name(self):
#       return f"This student name is :- {self.name} and surname is :- {self.surname}"
   
# Std1  = Strudent("OM" , "Pansala")
# print(Std1.name)
# print(Std1.full_name())


class car:

 total_car = 0

 def __init__(self,brand,modeal,price):
    self.brand = brand 
    self.__modeal = modeal
    self.__price = price
    car.total_car += 1

 def full_name(self):
    return f"This car brand is :- {self.brand} and model is :- {self.__modeal}"

 def get_price(self):
    return self.__price

 def fuil_type(self):
    return "Petrol"  
 
 @staticmethod
 def full_description():
    return f"This is a car class"
#proprty decorate use like hame attribuse owerwrite nahi karna dana hai tab use hota hai 
 @property
 def modeal(self):
    return self.__modeal


class Electric_car(car):
  
  def __init__(self,brand,modeal,battery):
    super().__init__(brand,modeal,price=0)
    self.battery = battery

  def fuil_type(self):
    return "Electric"

car1 = car("Toyeato","z21",20000)
# print(car1.modeal)
# print(car1.brand)
# print(car1.get_price())
# print(car1.fuil_type())
# print(car1.full_description())
# print(car.full_name())
print(car1.modeal)

# tesla = Electric_car("tesla","model s",100)
# print(tesla.brand)
# print(tesla.battery)
# print(tesla.full_name())
# print(tesla.fuil_type())


# print(car.total_car)