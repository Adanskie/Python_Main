print("Hello World")

numOne = 25
numTwo = 25

sum = numOne + numTwo
print("The Result : " + str(sum))

age = 20

if age >= 18:
  print("Legal age")
elif age <= 17:
  print("Not Legal age")

user = input("Enter a name : ")

if user == "adanielle":
  print(f"You are the user {user}")
else:
  print(f"You are not a user {user}")

list = ["adanielle","rhea","ereca","aiza"]

print(list[0])
print(list[1])
print(list[2])
print(list[3])
print("\n")

for get_value in list:
  print("Your name is : " + get_value)


print("\n")

# delete value using index number
delete = list.pop(0)
print(f"Delete value {delete}")

# delete value using the value
list.remove("ereca")
print(list)

# delete value
del list[0]

# lower case
name = "AdAnIeLLe".lower()
lastname = "SaBaRiA".lower()

print(name + " " + lastname)

# upper case
name = "rhea".upper()
lastname = "sabaria".upper()

print(name + " " + lastname)

