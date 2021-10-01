# 1.  You have rented some movies for your kids: 
# The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

price = 3 
the_little_mermade = 3 
brother_bear = 5 
hercules = 1 
total = (3+5+1)* 3
print(total)

# 2 Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook,
#  they pay you a different rate per hour. 
# Google pays 400 dollars per hour, 
# Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon



payment_for_week = {'company_name':['google', 'amazon','facebook'],
                    'pay_rate': [400, 380, 350],
                    'hour_worked':[6, 4, 10]} 
print(payment_for_week)

agg_pay = ('pay_rate')* ('hour_worked')
 
g= int(400)
a= int(380)
f = int(350)
p_r_g= int(6)
p_r_a= int(4)
p_r_f= int(10)

total_pay = (400*6)+(380*4)+(350*10)
print(total_pay)

total_pay1 = (g * p_r_g) + (a * p_r_a) + (f * p_r_f)
print(total_pay1)



#3 A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

can_be_enrolled = True 
class_full = False
class_schedule = True
conflit_current_schedule= False 
student_enrollemnt_status = (can_be_enrolled and not class_full) and (class_schedule and not conflit_current_schedule)
print (student_enrollemnt_status)


# 4 A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

buy_two_items = True
offer_expired = False 
premium_member = True 

product_offer = buy_two_items and not offer_expired or premium_member 
print (product_offer)


# Use the following code to follow the instructions below:

#   username = 'codeup'
#   password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:


# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace
 # the password must be at least 5 characters
 username = 'codeup'
 password = 'notastrongpassword'

passsword_length = False 
if len(password) >= 5:
    passwprd_length = True 

# the username must be no more than 20 characters
password = 'notastrongpassword'

username_length = False 
if len(username) < 20:
    username_length = True 

# the password must not be the same as the username
same_password_username = False 
if password != username:
    same_passwprd_suername = True 

# bonus neither the username or password can start or end with whitespace

if username[0] == ' ':
    username = username.strip()
    print('remove whitespace before username')
if password[0] == '':
    password = password.strip()
    print('remove whitespace after password')










