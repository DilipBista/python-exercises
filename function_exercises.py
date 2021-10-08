''' Define a function named is_two. 
It should accept one input and return True 
if the passed input is either the number or the string 2, False otherwise.'''

def is_two(one_input):
    if one_input == 2 or one_input =='2':
        return True
    else:
        return False
is_two('1')

''' Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.'''
def is_vowel(words):
     return words.lower()in 'aeiou'
print(is_vowel('a'))

''' Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
Use your is_vowel function to accomplish this.'''
def is_consonant(words):
    return words.lower() not in 'aeiou'
print(is_consonant('p'))

''' Define a function that accepts a string that is a word. 
The function should capitalize the first letter of the word if the word starts with a consonant.'''
def capitalize_consonant(word):
    if word[0]not in ['a','e','i','o','u']:
        capitalize_word = word.capitalize()
        return capitalize_word
print(capitalize_consonant('ball'))
''' 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and
the bill total, and return the amount to tip.'''
def calculate_tip(tip_percentage, bill_total):
    if tip_percentage <=1:
        tip = (tip_percentage*bill_total+ bill_total)
        return tip
print(calculate_tip(1,25))

''' 6. Define a function named apply_discount. It should accept a original price, 
and a discount percentage, and return the price after the discount is applied.'''

def apply_discount(original_price, discount_percentage):
    discount = original_price- (original_price * discount_percentage)
    return discount 
apply_discount(40,.10)

''' 7. Define a function named handle_commas. It should accept 
a string that is a number that contains commas
in it as input, and return a number as output.'''
def handle_commas(number):
    delete_commas= number.replace(',', '')
    return int(delete_commas)
handle_commas ('50,00,000')

''' 8. Define a function named get_letter_grade. 
It should accept a number and return the letter grade associated with that number (A-F).'''
def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B '
    elif score >=70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
get_letter_grade(85)
''' 9. Define a function named remove_vowels 
that accepts a string and returns a string with all the vowels removed.'''

def remove_vowels(words):
    vowels = ['a','e','i','o','u']
    result =[ word for word in words if word.lower() not in vowels]
    new_result= ''.join(result)
    print(new_result)

words= 'i hate typing things'
remove_vowels(words)

''' 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
anything that is not a valid python identifier should be removed
leading and trailing whitespace should be removed
everything should be lowercase
spaces should be replaced with underscores
for example:
Name will become name
First Name will become first_name
% Completed will become completed'''

def noramlize_name(name):
    
    
    # remove leading and trailing whitespace( use.strip)
    # everything should be in lower (use.lower)
    # replace space with underscore. replace ('', '_')
    # remove % 
    
    
    new_name = ' '
    for character in new_name:
        if character.lower() in character == ' ':
            new_name += character.lower()
    new_name = new_name.strip()
    for character in new_name:
        if character in new_name:
            if character == '':
                new_name = new_name.replace('', '_')
    
    return new_name
    
    
noramlize_name('Name')
noramlize_name('First Name')
noramlize_name('% Completed')

''' 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
cumulative_sum([1, 1, 1]) returns [1, 2, 3]
cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]'''

def cumulative_sum(new_list):
    
    new_cumulative_list = []
    
    length = len(new_list)
    
    new_cumulative_list = [sum(new_list[0:i:1]) for i in range (0, length +1 )]
    
    return new_cumulative_list[1:]


new_list= [1,1,1]
new_list = [1,2,3,4]


print(cumulative_sum(new_list))


