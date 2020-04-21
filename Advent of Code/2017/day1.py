with open('Inputs/day1.txt', 'r') as infile:
    data = infile.read()

def part_one():
    total = 0
    for index in range(len(data)):
        if index < len(data) - 1 and data[index] == data[index+1]:
            total += int(data[index])
        elif index == len(data) - 1 and data[index] == data[0]:
            total += int(data[index])
    print(total)

def part_two():
    total = 0
    circular_data = data*2
    for index in range(len(data)):
        if circular_data[index] == circular_data[index+int(len(data)/2)]:
            total += int(data[index])
    print(total)

part_one()
part_two()