# # function without pramater
# def greetCustomer():
#     ''' Just to fucntion demo'''
#     print("Hey, Welcome to Fucntions in python")

# greetCustomer()

# # function with pramater

# def greetUser(name):
#     print(f'Hey {name}, welcome to international conference')

# greetUser('Peter')    


# # function with more than one parameter with return

# def add(num1,num2):
#     sum=num1+num2;
#     return sum

# num1=int(input('Enter the first number'))
# num2=int(input('Enter the first number'))
# addition_result=add(num1,num2)
# print(f'Addition Result {addition_result}')

# # function with default parameters

# def getEmployeeInfo(name='Geetha',designation='Senior consultant'):
#     print(f' Name : {name} \n Designation={designation}')


# getEmployeeInfo()
# getEmployeeInfo('Hari','Manager')
# getEmployeeInfo('Lalitha')
# getEmployeeInfo(designation='Associate trainee')
# getEmployeeInfo(designation='Admin',name='Yash')

# def customerInfo(name,salary,location='Hyderabad'):
#     print(f'Customer Name: {name}\n Location ={location}')
# customerInfo('Mala')  


# Recursive Function

# def count_down(start):
#     print(start)
#     next=start-1
#     if next>0:
#      count_down(next)

# count_down(3)    

# def sum(n):
#    total=0
#    for index in range(n+1):
#         total+=index
#    return total     
# result =sum(100)
# print(result)


# def sum(n):
#     if(n>0):
#         return n+sum(n-1)
#     return 0

# print(sum(100))


# def sum(n):
#     return n+sum(n-1) if n>0 else 0

# result=sum(100)
# print(result)

# def get_full_name(first_name, last_name, formatter):
#     return formatter(first_name, last_name)

# def first_last(first_name, last_name):
#     return f"{first_name} {last_name}"


# def last_first(first_name, last_name):
#     return f"{last_name}, {first_name}"


# full_name = get_full_name('John', 'Doe', first_last)
# print(full_name) # John Doe


# full_name = get_full_name(
#     'John',
#     'Doe',
#     lambda first_name, last_name: f"{first_name} {last_name}"
# )
# print(full_name)

# Function Docstrings
# help(print)

def add(a,b):
    '''
    Add tow numbers
    Arguments:
        a is integer
        b is integer
    Returns:
        the sum of two integers 
    '''
    return a+b
#help(add)

print(add.__doc__)