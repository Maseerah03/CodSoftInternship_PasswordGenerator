import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[]{};_._=?+-"
length = int(input("Enter the desired length of password: "))
password = ""

for a in range(length):
    password+=random.choice(chars)
print("The generated password is:" ,password)