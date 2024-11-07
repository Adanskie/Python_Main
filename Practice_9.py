class Restaurant:
    def __init__(self,restaurant_name,cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine} These two pieces of information,")

    def open_restaurant(self):
        print(f"indicating that restaurant is open.")


restaurant = Restaurant("KALINDERYA NI IKLOY","MANOK")

print("Restaurant : " + restaurant.restaurant_name)
print("cuisine : " + restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n")

restaurant = Restaurant("Kalinderya ni Palcon", "Talong")

print("Restaurant : " + restaurant.restaurant_name)
print("cuisine : " + restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print()
get_1 = Restaurant("dogstyle",19)
get_2 = Restaurant("catstyle",20)
get_3 = Restaurant("venice",24)

get_1.describe_restaurant()
get_2.describe_restaurant()
get_3.describe_restaurant()

print("\n")

class User:
    def __init__(self,first_name,last_name,good):
        self.firstname = first_name
        self.lastname = last_name
        self.good = good

    def describe_user(self):
        print(f"Your name is {self.firstname} {self.lastname}")

    def greet_user(self):
        print(f"The best {self.good}")

user_1 = User("adanielle","Sabaria","programmer")
user_2 = User("Venice","Paculba","Nursing")

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
