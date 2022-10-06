import random
import array
# User the Enter maximum length
length = int(input("Enter password length :"))
print("Password maximum length :",length)
# declare arrays of the character that we need in out password
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
 'Z']
PUNCTUATION = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
 '*', '(', ')', '<']
# list
List = digits+lower_characters+upper_characters+PUNCTUATION
# random function use the choice
rand_digits = random.choice(digits)
rand_Lower = random.choice(lower_characters)
rand_upper = random.choice(upper_characters)
rand_punctuation = random.choice(PUNCTUATION)
# combine the character random
temp = rand_digits+rand_Lower+rand_upper+rand_punctuation
# loop
for x in range(length - 4):
    temp = temp + random.choice(List)
    temp_pass_list = array.array('u', temp)
    random.shuffle(temp_pass_list)
password = ""
for x in temp_pass_list:
 password = password + x
# print out password
print(password)
