list_of_passwords = []
other_list_of_passwords = []

def increasing_digits(input):
    index = 0
    input = str(input)
    for digit in input:
        for digits in range(index, len(input) - 1):
            if digits == len(input):
                return True
            elif input[index] > input[index+1]:
                return False
                
                
            
for number in range(168630, 718099):
    number = str(number)
    for digit in number:
        if number[index] == number[index + 1] and increasing_digits(number):
            list_of_passwords.append(number)

print(len(other_list_of_passwords))
    
    