# a=10
# b=20
# print("addition of 2 numbers:",a+b)

# str1="hello"
# str2="world"
# print("concatination of 2 strings:",str1+str2)

# list1=[1,2,3]
# list2=["A","B"]
# print("concatination of 2 lists:",list1+list2)

# class Age:
#     x=10+8
#     y="shabna"+"shihab"

# obj=Age()
# print(obj.x)
# print(obj.y)

#function polymorphism
# print(len("hellofriends"))

# print(len(["python","java","c++","c"]))
# print(len(["name:shabna","age:11","city:ernakulam"]))

# class Shape:
#     def area(self):
#         return 0
# class Circle(Shape):
#         def __init__(self,radius):
#             self.radius=radius
#         def area(self):
#             return 3.14 *self.radius**2
# Circle=Circle(radius=2)
# print(Circle.area())


# class Shape:
#     def area(self):
#         return 0
# class triangle(Shape):
#         def __init__(self,base ,height):
#             self.base=base
#             self.height=height
#         def area(self):
#             return 1/2 *self.base*self.height
# triangle=triangle(base=2,height=3)
# print(triangle.area())


class Greek:

    def __init__(self,name,age):
        self.geekName=name
        self.geekAge=age

    def displayAge(self):
        print("Age:",self.geekAge)

obj=Geek("R2j",20)









