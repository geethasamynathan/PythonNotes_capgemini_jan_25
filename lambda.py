# def lambdaexample1():
#     add_10=lambda x:x+10
#     print(add_10(20))

# lambdaexample1();

# def lambdaExample2():
#     num1=int(input('Enter the First Number'))
#     num2=int(input('Enter the Second Number'))
#     product =lambda num1,num2:num1*num2    
#     print("-----------------")
#     print(f'Product of {num1} * {num2} = {product(num1,num2)}');

# lambdaExample2()

# Assignment 
# calculate the total amount based price and quantity as input from the user
# using lambda function


# def lambdaExample3():
#     check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
#     print(check_even(4))  
#     print(check_even(7)) 
# lambdaExample3()


# def lambdawithmap():
#     numbers=[2,4,5,7,9];
#     result =map(lambda x:x*3,numbers)

#     print(list(result))
# lambdawithmap();    


# def lambda_with_filter():
#     numbers = [1, 2, 3, 4, 5]
#     result = filter(lambda x: x > 3, numbers)
#     print(list(result))
# lambda_with_filter()   

# def lambda_with_sort():
#     numbers = [11, 321, 32, 4, 50]
#     print("ascending order\n *******************")
#     numbers.sort()
#     print(numbers)
#     print("descending order\n *******************")
#     numbers.reverse()
#     print(numbers)

# lambda_with_sort() 

def lambdawithsorted():
    people = [("Alice", 30),('Denil',23), ("Bob", 25), ("Charlie", 35)]
    sorted_people = sorted(people, key=lambda person: person[0])
    print(sorted_people)

lambdawithsorted()   