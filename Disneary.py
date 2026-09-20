Person_info = {
    "name": "John Doe", 
    "age": 30,
    "city": "New York", 
    "email": 'john.doe@example.com',
    "phone": "123-456-7890",
    "age": 2001,
}



#acess list value by key
print(Person_info["name"])
print(Person_info.get("age"))

#Looping to access all elements in Dictionary
for info in Person_info:
    print(info, ":", Person_info[info])

#change in list value by key
# Person_info["age"] = 31

print(Person_info)
print(Person_info.get("age"))

if "email" in Person_info:
    print("Email is present in the dictionary.")  


for key, value in Person_info.items():
    print(key, ":", value)

# add iteam in Disneary 

Person_info["gender"] = "male"

print(Person_info)

#last iteam delet karna ka leaya 

Person_info.popitem()

#specific Delet mate 
Person_info.pop("phone")

del Person_info["city"]

print(Person_info)


square_number = {x:x**2 for x in range(1, 11)}
print(square_number)

info = {"first" : {
    "name": "Jane Doe",
    "age": 25,
    "city": "Los Angeles"
}, "second" : {
    "name": "Alice Smith",
    "age": 28,
    "city": "Chicago"
  }}

print(info["first"]["age"])  # Output: 25


kets = ["first", "second", "third"]
values = ["John", "Alice", "Bob"]

new_dict = dict.fromkeys(kets, values)
print(new_dict)  # Output: {'first': ['John', 'Alice', 'Bob'], 'second': ['John', 'Alice', 'Bob'], 'third': ['John', 'Alice', 'Bob']}

new_dict = {key: value for key, value in zip(kets, values)}
print(new_dict)  # Output: {'first': 'John', 'second': 'Alice', 'third': 'Bob'}