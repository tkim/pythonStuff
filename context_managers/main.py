#f = open('test.txt', 'r')
with open('test.txt', 'r') as f:
file_contents = f.read()

#f.close()

words = file_contents.split(' ')
word_count = len(words) 
print(word_count)

