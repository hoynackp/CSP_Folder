with open('day1.in', 'r') as infile:
    data = infile.read()

def solve_captcha(input):
    sum = 0
    for index in range(len(input) - 1):
        if input[index] == input[index + 1]:
            sum += int(input[index])
    if input[0] == input[-1]:
        sum += int(input[-1])
    return sum

def solve_part_two(data):
    sum = 0
    two_data = data * 2
    for index in range(len(data)):
        if int(data[index]) == int(two_data[int(index + (len(data)/2))]):
            sum += int(data[index])
    return sum

print('TOTAL FOR PART ONE:', solve_captcha(data))
print('TOTAL FOR PART TWO:', solve_part_two(data))