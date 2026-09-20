
list = [-1,1,2,3,-4,5,-6,-10,11]

#find the how many Positive number in list 

count = 0
for i in list:
  
    if i > 0:
        count += 1
print(count)


# n = int(input("Enter a number: "))

# count2 = 0

# for i in range(1, n+1):
#     if i % 2== 0:
#         count2 += 1
# print(count2)


n = 2
for i in range(1, 11):
    if i == 5:
        continue
    print(n * i)


#String revresce

text = "Hello World"
rev_text = ""

for i in text:
    rev_text = i + rev_text
print(rev_text)


#cheK THE FIRST STRING CHEAR ON REPATADE FIND

text2 = "Hello World"

for chat in text2:
    if text2.count(chat) == 1:
        print(f"{chat} is not repeated")
        break


fact_num = 5


for i in range (1, fact_num):
    fact_num *= i
print(fact_num)

# fact = 1
# while fact_num > 0:
#     fact *= fact_num
#     fact_num -= 1
# print(fact)



#cheak number between 1 to 10 

while True:
    num = int(input("Enter a number between 1 to 10: "))
    if num < 1 or num > 10:
        print("Invalid input. Please try again.")
    else:
        print(f"You entered: {num}")
        break