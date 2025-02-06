# birth_year = input("Enter your birth year: ")
# age = 2020 - int(birth_year)
# print(age)
#
# Built in functions for converting variables:
#     int()
#     str()
#     float()
#     bool()

# first_num = float(input("First: "))
# second_num = float(input("Second: "))
# sum = first_num + second_num
# print("Sum:" + str(sum))


# course = 'python for me'
# # print(course.replace('for', '4'))
# print('python' in course)

# print(10 // 3)
# print(10 / 3)
# print(10 % 3)
# print(10 ** 3)

# x = 10
# # x = x + 3
# x += 3
# print(x)

# comparison operators
# x = 3 != 2
# print(x)

# temperature = 31
# if temperature > 30:
#     print("It's a hot day")
#     print('Drink plenty of water')
# elif temperature > 20: # (20, 30)
#     print("It's a nice day")
# elif temperature < 10: # 10 , 20
#     print("It's a bit cold")
# else:
#     print('Done')

# weight_1 = int(input("Weight: "))
# weight_2 = int(input("Weight: "))
# total = weight_1 + weight_2
# print(total)

#Converting, formating, and math
# Weight = float(input("Weight: "))
# Weight_measurement = input("(K)g or (L)bs: ")
# set_case = Weight_measurement.lower()
# if Weight_measurement == str("l"):
#     multiplier = float(2.2046)
#     lbs_weight = Weight / multiplier
#     f_weight = "{:.1f}".format(lbs_weight)
#     print(str(f_weight) + "kgs")
# elif Weight_measurement == str("k"):
#     multiplier = float(2.2046226218)
#     kgs_weight = Weight * multiplier
#     f_weight = "{:.1f}".format(kgs_weight)
#     print(str(f_weight) + "lbs")

# While loops
# i = 1
# while i <= 10:
#     print(i * '$')
#     i = i + 1

# Index / Array
# names = ["Brittany", "Natasha", "Mike", "Erika"]
# names[0] = "Brit"
# print(names[0:3])
# print(names)

# Adding to Arrays
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# numbers.insert(0, -1)
# numbers.remove(3)
# numbers.clear()
# print(numbers)
# print(1 in numbers)
# print(len(numbers))

# For loop to print each number on it's own line
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(str(item) + "for loop")
#
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1
# For loops are a little cleaner - Deps on what is need from a while

# The Range Function
# Object that can store a sequence of numbers
# numbers = range(5, 30, 3)
# for number in numbers:
#     print(number)

# for number in range(5, 30, 3):
#     print(number)

# Tuples
# numbers = (1, 2, 3)
    # numbers.add - cannot change the list
    # unchangable list

# Write a converter to convert temperature

# 1. enter the temperature you would like to convert
temp = float(input("Temperature to convert: "))
# 2. Temperature entered in C(Celsius) or F(Fahrenheit)
units = str(input("Unit entered (C)Celsius or (F)Fahrenheit: "))
# 3. Code
    # Set case
unit = units.lower()
if units == "c":
    temp_to_convert = (temp * 1.800) + 32
    f_temp = "{:.2f}".format(temp_to_convert)
    print("The temperature in Fahrenheit is " + f_temp + "\N{DEGREE SIGN}" + "F")
elif units == "f":
    temp_to_convert = (temp - 32) / 1.800
    c_temp = "{:.0f}".format(temp_to_convert)
    print("The temperature in Celsius is " + c_temp + "\N{DEGREE SIGN}" + "C")

# Added a test line - This can be deleted

# Writing methods to parse selectors
# Test Step - app.page.method_name(value)
# test steps linked by application.rb file
# Method Definition
# def method_name(value)
#     returned_value = find("div.child_name" or "div#ID")
#     assert(value == returned_value)
# end
