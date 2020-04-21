with open('./garden.jpg', 'r') as f:
    garden = str(f.read())



picoctf = ''
for i in range(len(garden)):
    if kitters[i] != cattos[i]:
        picoctf += str(cattos[i])
