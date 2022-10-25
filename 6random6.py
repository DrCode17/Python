import string
import random

hossz = int(input("Milyen hosszú jelszót szeretnél? "))
karakterek = string.ascii_letters+string.digits+string.punctuation

jelszo = ""
for x in range(hossz):
    jelszo = jelszo+karakterek[random.randint(0, len(karakterek)-1)]

print(jelszo)