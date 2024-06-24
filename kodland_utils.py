import random

character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

pass_p = int(input("masukkan panjang password: "))
password = ""

for char in range(pass_p):
    password += random.choice(character)

print(password)