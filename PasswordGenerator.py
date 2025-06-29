#------------------Password Generator-----------------
import random
import string

#____________________Simple Logic___________________
pass_len=12
charValues=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(pass_len):
    password+=random.choice(charValues)

print("Your Password is :",password)

#_______________________List Comperehension______________________

res="".join([random.choice(charValues) for i in range(pass_len)])
print(res)

#______________________END OF PROGRAM____________________________