fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension.
#  Output should be ['MANGO', 'KIWI', etc...]
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
[fruits.upper() for fruits in ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']]

# Exercise 2 - create a variable named capitalized_fruits and use
#  list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
capitalized_fruits = [capitalized_fruits.capitalize() for fruits in capitalized_fruits]
print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']


def more_than_two_vowels(fruits):
    # check if input has moe than two vowels
    return len ([item for item in fruits if item.lower() in 'aeiou'])> 2 
    # now get lists of fruits with more than two vowels 
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if more_than_two_vowels(fruit)==True]
print(fruits_with_more_than_two_vowels)

# # Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
def with_only_two_vowels(fruits):
    return len ([item for item in fruits if item.lower()in 'aeiou'])== 2
fruits_with_only_two_vowels = [fruit for fruit in fruits if with_only_two_vowels(fruit)== True]
fruits_with_only_two_vowels

#  Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

[fruit for fruit in fruits if len(fruit) >5 ]

# 6 # Exercise 6 - make a list that contains each fruit with exactly 5 characters
[fruit for fruit in fruits if len(fruit)==5]

#7 Make a list that contains fruits that have less than 5 characters
[fruit for fruit in fruits if len(fruit) < 5]

#8 Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
len(fruits) # this will count length  of fruits but we need to calculate len(fruit) not len(fruits)
[len(fruit) for fruit in fruits]
len(fruits)

# 9 Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
def contains_letter_a(fruit):
    return len([item for item in fruit if item =='a']) > 0
fruits_with_letter_a = [fruit for fruit in fruits if contains_letter_a(fruit)]
print(fruits_with_letter_a)

#10  Make a variable named even_numbers that holds only the even numbers 
def even_numbers(numbers):
    if numbers  %2==0:
        return True
    else:
        return False 

# 11 Make a variable named odd_numbers that holds only the odd numbers
def odd_numbers(numbers):
    if numbers %2 ==1:
        return True
    else:
        return False

# 12 Make a variable named positive_numbers that holds only the positive numbers
 def positive_numbers (numbers):
     if numbers < 0:
         return True 
     else:
         return False

# 13  Make a variable named negative_numbers that holds only the negative numbers

def negative_numbers (numbers):
    if numbers > 0:
        return True 
    else:
        return False 

# 14 use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
[number for number in numbers if len(str(abs(number)))>=2]

# 15 Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
 
 numbers_squared= [number **2 for number in numbers]
 numbers_squared 


def square_num(number):
     return number **2

# 16 Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [number for number in numbers if (number % 2 !=0) and (number <0)]
odd_negative_numbers

# 17 Make a variable named numbers_plus_5. In it, return a list containing each number plus five.
number_plus_5 = [number +5 for number in numbers ]
number_plus_5 