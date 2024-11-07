class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

Dogs_1 = Dog("adanielle",19)
Dogs_2 = Dog("venice",69)

print(f"Your Dogs is {Dogs_1.name} {Dogs_1.age} Years Old")
print(f"Your Dogs is {Dogs_2.name} {Dogs_2.age} Years Old")
