cd C:\Users\madde\Documents\work\JPSM\BIGDATA_699
# store file name.
file_name = "pg1513.txt"

# open the file.
my_file = open( "pg1513.txt", "r")
num_lines = 0
num_words = 0
num_chars = 0

with open("pg1513.txt", 'r') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)
print (num_lines)
print (num_words)
print (num_chars)
my_file.close()