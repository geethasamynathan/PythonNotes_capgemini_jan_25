from functools import reduce

# Using reduce() to multiply all elements in the list

no_of_element = int(input('Enter the no of elements '))
numbers=[]
for i in range(no_of_element):
    numbers[i]= int(input('enter the value'))

product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 24