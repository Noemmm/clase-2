import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("introduce la longitud de tu contraseña:"))
contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

print(contraseña)
