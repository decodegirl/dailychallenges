# Write a password generator in Python.
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters,
#  uppercase letters, numbers, and symbols.
#  The passwords should be random, generating a new password every time the user asks for a new password.
# Include your code in a main method.


import random

password_length = int(input("How long do you want your password to be?:"))

y = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

p = "".join(random.sample(y,password_length))

print(p)
