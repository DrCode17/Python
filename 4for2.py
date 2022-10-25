tanulok = ["Pisti", "Pál", "Anna", "Aranka"]

leghosszabbnev = tanulok[0]

for x in tanulok:
    if len(x) > len(leghosszabbnev):
        leghosszabbnev = x

print(leghosszabbnev)

legrovidebbnev = tanulok[0]

for x in tanulok:
    if len(x) < len(legrovidebbnev):
        legrovidebbnev = x

print(legrovidebbnev)
