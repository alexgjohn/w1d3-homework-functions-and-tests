def return_10():
    return 10

def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(first_number_string, second_number_string):
    return int(first_number_string) + int(second_number_string)

months_of_the_year = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def number_to_full_month_name(number_of_month_in_year):
    return months_of_the_year[number_of_month_in_year - 1]

def number_to_short_month_name(number_of_month_in_year):
    return months_of_the_year[number_of_month_in_year - 1][0:3]


def volume_of_cube(length_of_side):
    return length_of_side**3

def reverse_string(normal_string):
    return normal_string[::-1]

def fahrenheit_to_celsius(number_in_fahrenheit):
    return ((number_in_fahrenheit-32)*5)/9

# print(fahrenheit_to_celsius(7))






