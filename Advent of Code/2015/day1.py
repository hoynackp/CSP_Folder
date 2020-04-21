infile = open('Inputs/day1.txt', 'r')
data = infile.read()
infile.close()
floor = 0
index = 0
basement = False
for parenthesis in data:
    index += 1
    if parenthesis == '(':
        floor += 1
    else:
        floor -= 1
    if not basement and floor == -1:
        position = index
        basement = True
print('The floor in the first problem is', floor)
print('The position in the second problem is', position)