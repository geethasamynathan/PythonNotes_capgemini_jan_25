# bonuses=[100,200,300]
# new_bonuses=[]

# for bonus in bonuses:
#     new_bonuses.append(bonus*2)

# print(new_bonuses)   
 
# Python provides a nicer way to do this kind of task by using the map() built-in function.

# The map() function iterates over all elements in a list (or a tuple), applies a function to each, and returns a new iterator of the new elements.

# #using map function generating new bonus
# def double(bonus):
#     return bonus*2

# bonuses=[100,200,300]
# newbonus=map(double,bonuses)

# print(list(newbonus))

# # using map and lambda

# bonuses=[100,200,300]
# new_bonus=map(lambda bonus:bonus*2,bonuses)
# print(list(new_bonus))


# #map() function for a list of string

# names=['geetha','muthu','murthi','vedha']

# new_names=map(lambda name:name.capitalize(),names)
# print(list(new_names))

# # Python map() function to a list of tuples

# carts=[['smartphone',56000],
#        ['Laptop',890000],
#        ['projector',23000]
# ]

# print(list(carts))
# TAX=0.1
# carts_with_tax=map(lambda item:[item[0],item[1],item[1] * TAX],carts)
# print(list(carts_with_tax))