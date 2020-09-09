print('enter a word')
word = input()
valid_words = []

with open("names.txt", 'r') as f:
    for line in f=
        if len(line) == len(word):
            valid_words.append(line)

print (valid_words)

'''
valid_words = []


    lines_in_file = f.readlines()
    for line_number in range(0,5):
        print(lines_in_file[line_number])

def input_function:
'''
