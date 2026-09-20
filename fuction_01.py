def square(num):
  print(num ** 2)


value = square(10)

print(value)


def summ(a, b):
  return a + b

result = summ(1, 2)
print(result)



#passing desault value in parameter 

def greet(name, msg="Hello"):
  print(f"{msg} {name}! How are you doing?")


greet("OM Pansala")

def f(x, lst=[]):
   lst.append(x)
   return lst

def g(x, lst=[]):
   lst.append(x)
   return lst


funcs = [] 
for i in range(5): funcs.append(lambda: i**2) 
result = [f() for f in funcs]

print(result)



#lamda fuction

clube = lambda x: x**3 

print(clube(3))


def Sum(*args):
  return sum(args)

print(Sum(1, 2, 3, 4, 5))


def Sum1(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

Sum1( name = "OM Pansala", age = 20, city = "Pune")


#yield fuction same as retun but memory ma store kare rakhea 

def my_generator(number):
  for i in range(number):
    yield i * 2


for value in my_generator(5):
  print(value)