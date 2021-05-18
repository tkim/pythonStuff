import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "0123456789"
symbols = "#!@$%^&*"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums: 
    all += numbers
if syms:
    all += symbols

length = 17
amount = 5

f = open("pw5.txt", "w+")

for x in range(amount):
    password = "".join(random.sample(all, length))
    #print(password)
    f.write("Passwords  %s\r\n" % (password))

f.close()