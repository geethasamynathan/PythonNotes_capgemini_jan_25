# for item in "Python":
#     print(item)


# for item in ["Geetha","Riya","Fransy"]:
#     print(item)

# for item in [1,2,3,5,78,34]:
#     print(item)

# for item in range(10):
#     print(item)

for item in range(10,15):
    print(item)   

# for item in range(5,12,2):
#     print(item)

 # calculate the total prices of all items in the cart 
# prices=[100,300,500]
# total=0
# for price in prices:
#  total+=price  
# print(f"Total : {total}")

# Nested for loop

#we can generate co-ordinates
# (x)  (y)
# (0) (0)
# (0) (1)
# (0) (2)
# (1) (0)
# (1) (1)
# (1) (2)

for x in range(4):
    for y in range(3):
        print(f"({x}) ({y})")


# challenge

# numbers=[5,2,5,2,2]
# for x_count in numbers:
#     print('x'*x_count)


#numbers=[5,2,5,2,2]
# numbers=[2,2,2,2,6] # for printing L
# for x_count in numbers:
#   output=''
#   for count in range(x_count):
#     output+='X'
#   print(output)  