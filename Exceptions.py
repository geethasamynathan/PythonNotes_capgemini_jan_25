# how to handle errors
# age=int(input('Age:'))
#     print(age)

# try:
#     age=int(input('Age:'))
#     income=20000
#     risk=income/age
#     print(age)
# except ValueError:
#     print('Inuput should be number')
# except ZeroDivisionError:
#     print('age cannot not be zero')

# # example  for try except and general exceptions
# try:
#     # get input net sales
#     print('Enter the net sales for')

#     previous = float(input('- Prior period:'))
#     current = float(input('- Current period:'))

#     # calculate the change in percentage
#     change = (current - previous) * 100 / previous

#     # show the result
#     if change > 0:
#         result = f'Sales increase {abs(change)}%'
#     else:
#         result = f'Sales decrease {abs(change)}%'

#     print(result)
# except ValueError:
#     print('Error! Please enter a number for net sales.')
# except ZeroDivisionError:
#     print('Error! The prior net sales cannot be zero.')
# except Exception as error:
#     print(error)

