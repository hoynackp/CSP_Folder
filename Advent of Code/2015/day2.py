infile = open('Inputs/day2.txt', 'r')
data_list = infile.readlines()
infile.close()
def part_one():
    total = 0
    for line in data_list:
        list_of_dimensions = line.split('x') # replaces the commented code
        #line = line.strip()
        #first_x = line.find('x')
        #second_x = line.rfind('x')
        #list_of_dimensions = []
        #list_of_dimensions.append(line[:first_x])
        #list_of_dimensions.append(line[first_x+1:second_x])
        #list_of_dimensions.append(line[second_x+1:])
        length, width, height = int(list_of_dimensions[0]), int(list_of_dimensions[1]), int(list_of_dimensions[2])
        area = 2*length*width + 2*width*height + 2*height*length
        extra_paper = min(length*width, width*height, height*length)
        total += area + extra_paper
    print("They should order", total, "square feet of wrapping paper.")

def part_two():
    total = 0
    for line in data_list:
        list_of_dimensions = line.split('x') # replaces the commented code
        #line = line.strip()
        #first_x = line.find('x')
        #second_x = line.rfind('x')
        #list_of_dimensions = []
        #list_of_dimensions.append(line[:first_x])
        #list_of_dimensions.append(line[first_x+1:second_x])
        #list_of_dimensions.append(line[second_x+1:])
        length, width, height = int(list_of_dimensions[0]), int(list_of_dimensions[1]), int(list_of_dimensions[2])
        ribbon = 2 * min(length+width, width+height, height+length)
        bow = length*width*height
        total += ribbon + bow
    print("They should order", total, "feet of ribbon.")

part_one()
part_two()