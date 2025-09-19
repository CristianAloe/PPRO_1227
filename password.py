import random

elementi = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lunghezza =  int(input("Quanto deve essere lunga la password?"))

password = ""
for i in range(lunghezza):
    password = password + random.choice(elementi)
    #count = count + 1


print(password)
