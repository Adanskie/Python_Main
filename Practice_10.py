class User:
    def __init__(self, first_name, last_name, age, email, location):
        # Instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        # Method to describe the user
        print(f"User Info: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        # Method to greet the user
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

    def increment_login_attempts(self):
        total = self.login_attempts = self.login_attempts + 1
        return total

    def reset_login_attempts(self):
        reset = self.login_attempts = 0
        return reset

# Creating instances of the User class
user1 = User("John", "Doe", 28, "john.doe@example.com", "New York")
user2 = User("Jane", "Smith", 34, "jane.smith@example.com", "Los Angeles")
user3 = User("Alice", "Johnson", 25, "alice.johnson@example.com", "Chicago")

# Calling methods for each user
print("User 1:")
user1.describe_user()
user1.greet_user()
print("\nUser 2:")
user2.describe_user()
user2.greet_user()
print("\nUser 3:")
user3.describe_user()
user3.greet_user()
print("\n\n")

user1 = User("Adanielle",
            "Sabaria",
            19,
            "adanskie2555@gmail.com",
            "Philipines")

print(user1.login_attempts)
user1.greet_user()
user1.describe_user()
user1.increment_login_attempts()
print()

user2 = User("Venice",
            "Paculba",
            19,
            "venice2555@gmail.com",
            "Philipines")

print(user2.increment_login_attempts())
user2.greet_user()
user2.describe_user()

user3 = User("Edith","Sabaria",60,"Edith@Gmail.com","Philipines")
user3.reset_login_attempts()

print("\nReset login_attempts")
print(user3.login_attempts)
