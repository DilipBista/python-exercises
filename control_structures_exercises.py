
##1. Conditional Basics
 #prompt the user for a day of the week, print out whether the day is Monday or not
 day_of_the_week_monday = True
if day_of_the_week == 'monday':
    print("Its monday")
else:
    print("its not monday yet")

 # prompt the user for a day of the week, print out whether the day is a weekday or a weekend
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
weekend = ['saturday', 'sunday']
weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
user_input = input(days)

for day in days:
    if user_input == weekday:
        print('It is weekday')
    else:
        print('It is weekend')
#create variables and make up values for the number of hours worked in one week the hourly rate how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. 
#You get paid time and a half if you work more than 40 hours 
worked_hours = int (input('input number of hours worked'))
rate = 10
regular_check = worked_hours * rate 
overtime_check =  (regular_check + ((worked_hours - 40) * (rate * 1.5)))

if worked_hours <= 40:
    print(regular_check)
else:
    print(overtime_check)

# Loop Basics
#While Create an integer variable i with a value of 5. Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.
#Your output should look like this

i = 5
while i <= 15:
    print(i)
    i= i+1


# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.
i = 0
while i <=100:
        print(i)
        i = i+2
     
        
      

# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10 :
    print(i)
    i = i - 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.
# Output should equal:  
i = 2 
while i <=1000000:
    print (i)
    i = i ** 2

# '''Write a loop that uses print to create the output shown below'''
i = 100 
while i >=5:
    print (i)
    i = i-5

#  b. For Loops

#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# For example, if the user enters 7, your program should output:
x = 7 
for y in range (1,11):
    print (x, 'x', y, '=', x*y)


# ii. Create a for loop that uses print to create the output shown below '''

for i in range(1,10):
    print(str(i)*i)

'''# break and continue

Prompt the user for an odd number between 1 and 50.
Use a loop and a break statement to continue prompting
the user if they enter invalid input. 
(Hint: use the isdigit method on strings to determine this). 
Use a loop and the continue statement to output all 
the odd numbers between 1 and 50, except for the number the user entered.''' 

print('Number to skip is: 27')

num = input('Enter a number')
while True:
    if(num.isdigit()== False 
       or int(num) > 50 
       or int(num)<= 0
       or int(num)%2 ==0):
        print ('Enter an odd number only')
        num = input('Enter a number')
    else:
        break
num = int(num)
print('The number to skip is ', num)
for i in range(1,50):
    if i%2 == 0:
        continue 
    elif i== num:
        print('Yikes! Skipping tghis number', i)

''' d. The input function can be used to prompt for input and use that input in your python code.
Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
(Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)'''
def pos_number(numbers):
    numbers = int(input('enter a positive number'))
    for number in numbers >=0:
        print(pos_number)


num = input('Entar a positive number')

while True:
    if (num.isdigit()==False
        or int(num)< 0):
        Print('Invalid number')
        num = input('Entar a positive number')
    else:
        break
for i in range(0, int(num)+1):
    print(i)
''' 2 e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.'''

numb = input('Enter a positive number')

while True:
    if (numb.isdigit()==False
        or int(numb)< 0):
         Print('Invalid number')
         numb = input('Enter a positive number')
    else:
        break
for i in reversed(range(1,int(numb)+ 1)):
    print(i)
''' Fizzbuzz
One of the most common interview questions for entry-level programmers 
is the FizzBuzz test. Developed by Imran Ghory,
the test is designed to test basic looping and conditional logic skills.'''
for number in range (1,100): 
    number = int(input('enter a number'))
    if number %3==0 and number %5==0:
        print("FizzBuzz")
    elif number %3== 0:
        print("fizz")
    elif number %5==0:
        print("Buzz")
print(number)


''' Display a table of powers.

Prompt the user to enter an integer.
Display a table of squares and cubes from 1 to the value entered.
Ask if the user wants to continue.
Assume that the user will enter valid data.
Only continue if the user agrees to.'''
num = input('enter a positive number')
print ('There is atable below ')
print('number| sqaured| cubed')
print('------|--------  |------')
num = int(num)
for i in range (1,4):
    print(f'{i}    |{i**2}|    {i**3}')


''' 5. Convert given number grades into letter grades.

Prompt the user for a numerical grade from 0 to 100.
Display the corresponding letter grade.
Prompt the user to continue.
Assume that the user will enter valid integers for the grades.
The application should only continue if the user agrees to.
Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0'''

while True:
    num = input(' Enter number: ')
    num = int(num)
    
    if num >= 88:
        print('A')
    elif num>= 80:
        print('B')
    elif num>=67:
        print('C')
    elif num>= 60:
        print('D')
    else:
        print('F')
    choice= input('If you want to continue, Enter yes: ')
    if choice.lower() in'yes':
        continue 
    else:
        break


    


   
        
    