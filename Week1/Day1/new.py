# list1 = [5, 10, 15, 20, 25, 50, 20]
# list1[3] = 200
# list1.append(40)
# list1.remove(10)

# list2 = ["John", "Lennon", "Kiss"]
# print(list1 + list2)

# loop
# cities = ["London", "Moscow", "New-York"]
# for city in cities:
#     print("I was in " + city)

# range
# numbers = range(1,21)
# for number in numbers:
#     print(number)

# numbers = list(range(1,6))
# numbers.append("40x")
# print(numbers)

# number = int(input())
# times = range(0,10)
# numbers = [number * time for time in times]
# print(numbers)

# number = 1
# while number <= 8:
#     print(number)
#     number += 1
# print("Finished")


#flag
# active = True
# while active: 
#     city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
#     if city == 'quit':
#         active = False
#     elif city == 'leave me alone':
#         active = False
#     elif city == 'stop':
#         active = False
#     else:
#         print("I'd love to go to", city)
# print("Goodbye !")

# while True: 
#     city = input("Please enter the name of a city you have visited (enter 'quit'  when you are finished): ")
#     if city == 'quit':
#         break
#     else:
#         print("I'd love to go to", city)

# print("Goodbye !")


# while True:
#     city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
#     if 'quit' in city:
#         break
#     else:
#         print("I'd love to go to", city)

# print("Goodbye!")



#password checker
# username = input("Type in username: ")
# password = input("Type in your password: ")
# password_lenght = len(password) * "*"
# print(f"Hey there, your password {password_lenght}")

# username2 = input("Type in username: ")
# password2 = input("Type in your password: ")
# password_lengh2t = len(password2) * "*"

# if password_lenght == password_lengh2t and password == password2 and username == username2:
#     print("Confirmed")
# else:
#     print("Not confirmed")

#age checker
# restriction = "18"
# age = input("Type in your age: ")
# if int(age) > int(restriction):
#     print("You are old enough")
# elif int(age) < int(restriction):
#     print("You are not old enough")
# else:
#     print("You should type in how old are you")

is_friend = False
can_message = "message allowed" if is_friend else "message is not allowed"
print(can_message)