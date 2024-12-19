import random
lon = int(input("De que longitud sera la contraseña?"))

password = ''
for i in range(lon):
    ce = random.choice(".,;:?!'()[]{}-0123456789abcdefghijqlmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    password = password + ce

print("La contraseña es: 11" + password)
print(password)
