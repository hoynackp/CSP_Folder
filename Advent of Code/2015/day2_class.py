def get_dimensions(line):
    x1 = line.find('x')
    x2 = line.rfind('x')
    l = int(line[:x1])
    w = int(line[x1+1:x2])
    h = int(line[x2+1:])
    return(l, w, h)

def get_surface_area(l, w, h):
    return(2*l*w + 2*w*h + 2*h*l)

def get_slack(l, w, h):
    return(min(l*w, w*h, h*l))


with open('Inputs/day2.txt') as infile:
    data = infile.readlines()

def part_one():
    total_paper = 0
    for line in data:
        line = line.strip()
        l, w, h = get_dimensions(line)
        total_paper += get_surface_area(l, w, h) + get_slack(l, w, h)
    print(total_paper)

part_one()