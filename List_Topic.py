frutis = ["apple", "banana", "cherry", "kiwi", "mango","apple"]

print(frutis)

#List Mur=table hai
#Multiple Data type allow hai
#List following index
#Duble cate allolow in Python List

print(frutis[0])
print(frutis[::-1])
print(frutis[1:])
print(frutis[1:3])

frutis[0] = "orange"
print(frutis) 

#slicing in List

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(number[::2])
number[0] = 10
number[1:4] = [20, 30, 40]
print(number)
number[1:4] = [100]
print(number)



number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in number: 
    print(i)

if 100 in number:
    print("Yes")
else:
    print("No")

#List Methods

#add last me add karne ke liye append method use hota hai
number.append(10)
#lasyt ma remove 
number.pop()
#specific numbery ys valusr remove karna ka leya 
number.remove(5)
#Inset karne ke liye insert method use hota hai
number.insert(2, 100)


print(number)

#Like mujai list ka copy creat karna ho and Diffrnet Memorry refrence ka leya 
number_copy = number.copy()
print(number_copy)  

number.append(200)
print(number)

print(number_copy)


Square_number = [ x ** 2 for x in range(1, 11)]
print(Square_number)