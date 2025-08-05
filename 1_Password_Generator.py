import random

total_chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+.>,</?~`"
pass_length = int(input("Enter the length of your password: "))
password = " "

for a in range(pass_length):

    password += random.choice(total_chars)
    

print(password)
