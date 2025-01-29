coordinates=(1,2,3)
# coordinates[0]*coordinates[1]*coordinates[2]

# x= coordinates[0]
# y=coordinates[1]
# z=coordinates[2]

x,y,z=coordinates

# print(x)
# print(y)

# this unpacking we can use for list as well

coordinates=[1,2,3]
# x,y,z=coordinates

# print(x)
# print(y)


x,*others=coordinates;
print(x)
print(others)