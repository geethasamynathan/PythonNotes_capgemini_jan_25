names=['Geetha',"Jey","Tina","Fransy"]
# print(names[0])
# print(names[2])
# print(names[-1])
# print(names[-3])

# print(names[1:]) # to select item from exisiting list  # ['Jey', 'Tina', 'Fransy']
# print(names[1:3])  # ['Jey', 'Tina'] last item omitted

# print(names[:]) # which generates a new list which is not affecting our original list
# print(names[2:])  # ['Tina', 'Fransy']  # new list
# print(names)      # ['Geetha', 'Jey', 'Tina', 'Fransy']  # original list

# names[1]="Raj"  # we can change the value based on index position
# print(names)    # ['Geetha', 'Raj', 'Tina', 'Fransy']

# Finding largest number in a list

# numbers =[2,45,76,45,86,1]
# max=numbers[0]
# for num in numbers:
#     if num>max:
#         max=num
# print(max)        

# 2 dimensional list
 # maily used in datascience and machine learning
 # matrix
#  [
#   1 2 3
#   4 5 6
#   7 8 9
#  ]

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print(matrix[0][1])
# matrix[0][1]=20  # can change the value
# print(matrix[0][1])

# for row in matrix:
#     for item in row:
#         print(item)


numbers =[3,56,67,34,66]
# numbers.append(450)
# print(numbers)

# # add numbers in the middle
# numbers.insert(1,900)
# print(numbers)

# # remove the item
# numbers.remove(900)
# print(numbers)


# clear
# numbers.clear();
# print(numbers)


# # pop remove lastitem in the list
# numbers.pop()
# print(numbers)

# to check the existance of given value
# print(numbers.index(56))  # 1
# print(numbers.index(560))  # error as the given value is not exist

# print (560 in numbers)  # it will return boolean value. It wont give any error like index so in used to safer for existance
# numbers.append(3);
# print(numbers.count(3)) # it will numbers items(3) found in the list
numbers =[3,56,67,34,66,3]
# # Sort in ascending
# print(numbers.sort()); # none it is an object but it will not retun any value

# numbers.sort()
# print(numbers)  # none sorted in ascending order


# # sort descending
# numbers.reverse()
# print(numbers)

# # Copy()
# numbers2=numbers.copy();
# numbers.append(999); # it is not affecting the second list (numbers2)
# print(numbers2)

# # write a program to remove the duplicates in the list
# numbers3=[2,2,4,6,3,4,6,1]
# uniques=[]
# for number in numbers3:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# # sort() method to sort a list of tuples
# companies = [('Google', 2019, 134.81),
#              ('Apple', 2019, 260.2),
#              ('Facebook', 2019, 70.7)]

# # sort the companies by revenue
# companies.sort(key=lambda company: company[0])

# # show the sorted companies
# print(companies)


# sorted()
#The sort() method sorts a list in place. In other words, 
# it changes the order of elements in the original list.

#To return the new sorted list from the original list,
#  you use the sorted()

# guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
# sorted_guests = sorted(guests)

# print(guests)
# print(sorted_guests)

employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 60000},
    {"name": "Rajesh", "salary": 40000},
    {"name": "Harini", "salary": 50000},
    {"name": "Nithin", "salary": 60000},
    {"name": "Charlie", "salary": 40000}
]

# Sorting by salary, and then by name alphabetically
sorted_employees = sorted(employees, key=lambda x: (x["salary"], x["name"]))

for item in sorted_employees:
 print(item)