fname = input("Enter file name: ")
num_words = 0
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
    for line in f:
	    num_lines += 1
print("Number of words:")
print(num_words)
print("Number of lines:")
print(num_lines)
