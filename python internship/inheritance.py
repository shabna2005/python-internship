# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def make_sound(self):
#         return "woof"
# d1=Dog("jack")
# print(d1.name)
# print(d1.make_sound())

# class Brands:
#     brand_name_1="Amazon"
#     brand_name_2="Ebay"
#     brand_name_3="olx"

# class Products(Brands):
#     prod_1="Online Ecomerce store"
#     prod_2="online store"
#     prod_3="online buy sell store"

# obj_1=Products()
# print(obj_1.brand_name_1+"is an" +obj_1.prod_1)

class Brands:
    brand_name_1="Amazon"
    brand_name_2="Ebay"
    brand_name_3="olx"

class Products(Brands):
    prod_1="Online Ecomerce store"
    prod_2="online store"
    prod_3="online buy sell store"

class Popularity(Brands,Products):
    prod_1_popularity=180
    prod_2_popularity=70
    prod_3_popularity=60

obj_1=Popularity()      
print(obj_1.brand_name_1+"is an"+obj_1.prod_1)

