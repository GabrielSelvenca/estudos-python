import json

array = []
n = 0
while len(array) < 20:
    if n % 2 == 0:
        array.append(n)
    n += 1

with open("array.json", "w") as arquivo:
    json.dump(array, arquivo)