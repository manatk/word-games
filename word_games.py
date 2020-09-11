print('Enter a word!')
word = input()
valid_words = {}

with open("names.txt", 'r') as f:
    for line in f:
        if len(line.strip()) == len(word):
            if sorted(line.strip()) in valid_words:
                valid_words[line.strip()].append(line.strip())
            else:
                valid_words.append(sorted(line.strip()))
            valid_words.append(line.strip())

sorted_words = []
sorted_word = sorted(word)

for i in valid_words:
    sorted_words.append(sorted(i))

#print (sorted_words)

final_list = []
#print (sorted_word)
for i in sorted_words:
    #print (i)
    if i == sorted_word:
        #print (i)
        final_list.append(i)

print (final_list)


#print(sorted_words)
