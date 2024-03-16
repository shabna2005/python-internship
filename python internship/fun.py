#def my_function():
 #   print("my name is irfana")
#my_function() 

# def add_num(a,b):
#     sum=a+b
#     return sum
# num1=25
# num2=55
# print("the sum is",add_num(num1,num2))

# def multiply_num(a,b):
#     product=a*b
#     return product
# num1=22
# num2=46
# print("the product is",multiply_num(num1,num2))

# def check_odd_even(number):
#     if number % 2 ==0:
#         return"even"
#     else:
#         return"odd"
# num=25
# result=check_odd_even(num)
# print(result)

# def find_square(num):
#     result=num*num
#     return result
# square=find_square(3)
# print(square)

# def find_cube(num):
#     result=num*num*num
#     return result
# cube=find_cube(2)
# print(cube)

# def add_numbers(a=7,b=8):
#     sum=a+b
#     print("sum",sum)
# add_numbers()

# def display_info(subject,mark):
#     print("subject:",subject)
#     print("mark:",mark)
# display_info(mark="80",subject="english")

# def find_sum(*numbers):
#     result=0
#     for num in numbers:
#         result=result+num
#     print("sum=",result)
# find_sum(1,2,3)
# find_sum(4,9)

def find_product(*numbers):
    result=1         
    for num in numbers:
        result=result*num
    print("product=",result)
find_product(5,6,7)
find_product(9,8) 
