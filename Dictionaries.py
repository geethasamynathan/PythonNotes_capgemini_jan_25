# customer 
# Name:"Geetha"
# Email:"geetha@mail.com"
# Phone:45677

customer ={
    "name":"Geetha Eswaramurthi",
    "email":"geetha@mail.com",
    "phone":45677,
    "age":23,
    "is_verified":True
}
print(customer["name"])

# print(customer["Name"]) # error

print(customer.get('name'))

print(customer.get('birthdate')) # None

# if the dictionary does not have value we can pass default value
print(customer.get('birthdate',"1-1-1985"))

# if you want to change the value for any key
customer["name"]="Riya sam"

print(customer['name']) # it will update

# if we need to add one more key value pair we can add
customer['location']='Chennai';

print(customer.get('location'))

#assignment

phone=input("Enter phone No:")
# "1"=>"one"

digits_mapping={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}

output=""
for ch in phone:
 output+=digits_mapping.get(ch,"!")+" "
print(output) 