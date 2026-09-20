#List are muttable and memory wirking the Behind 

l1 = [1,2,3,4]
l2 = l1
print(l1)
print(l2)

#change the l1 and change the l2 automatic like same memory adress the considering this list

l1[0] = 33
print(l1)
print(l2)


#like l2 ko new assign memory karu to badme chges karo 
l2 = [1,2,3]

print(l1)
print(l2)

l1[0] = 23
print(l1)
print(l2)

