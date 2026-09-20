name = "Om Pansala"


#Slicing in Strings
print(name)
print(name[0])  
print(name[1:4])  
print(name[::2])
print(name[::-1])


#methods in Strings
print(name.upper())   
print(name.lower())
print(name.title())
print(name.strip())
print(name.replace("Om", "Omkar"))
print(name)

chai = "I love Chai"
print(chai.split(" "))

#S
print(chai.find("Chai"))

#How many times a character is present in the string
print(chai.count("a"))

chai_Flavour = "Masala Chai"
quantity = 2

#String formatting using innear variables
chai = "I want {quantity} {chai_Flavour}"

print(chai.format(quantity=quantity, chai_Flavour=chai_Flavour))

chai = f"I want {quantity} {chai_Flavour} This is formating method"
print(chai)

#list convert to string using join method
list1 = ["Om", "Pansala", "is", "a", "good", "boy"]
k = " ".join(list1)
print(k)  

path = r"C:\new\test"
print(path)



name = 'om Patel'
print(name)
name = "om Patel"
print(name)
name = '''om Patel'''
print(name)