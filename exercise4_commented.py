#Change the directorty in python to where the Romeo and Juliet file is located
# C:\Users\madde\Documents\work\JPSM\BIGDATA_699
# store the Romeo and Juliet file name.
file_name = "pg1513.txt"

# open the file.
my_file = open( "pg1513.txt", "r")
# create variable names for lines, words, characters to count
num_lines = 0
num_words = 0
num_chars = 0
#run loop to go through and count each line
with open("pg1513.txt", 'r') as filename:
	#for each line in the file
    for line in filename:
    	#define words by each space in the line
        words = line.split()
		#count the number of lines
        num_lines += 1
        #count the number of words
        num_words += len(words)
        #count the number of characters
        num_chars += len(line)
#print the number of lines, words, and characters
print (num_lines)
print (num_words)
print (num_chars)
#close the file
my_file.close()