import my_module

filename = 'words.txt'


word_list = my_module.read_list_from_file(filename)

word_list = []

word = input('Enter a word (or \'quit\' to quit): ')

while word != 'quit':
    word_list.append(word)
    word = input('Enter a word (or \'quit\' to quit): ')

print(word_list)
my_module.write_list_to_file('words.txt', word_list)