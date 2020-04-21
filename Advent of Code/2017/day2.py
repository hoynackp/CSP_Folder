with open('Inputs/day2.txt', 'r') as infile:
    data = infile.read()
list_of_row = data.split('\n')
list_of_rows = []
for row in list_of_row:
    list_of_rows.append(row.split())

def part_one():
    checksum = 0
    for row in list_of_rows:
        numbers_in_row = []
        for number in row:
            numbers_in_row.append(int(number))
        difference = max(numbers_in_row) - min(numbers_in_row)
        checksum += difference
    print("The checksum is", checksum)
    
part_one()
