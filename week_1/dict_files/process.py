# Import this module to generate regex to test word pattern
import re

# Read contents from a file
filename = 'poem.txt'
# Open with filename
opened_file = open(filename, 'rb')
# Iterate through the file line by line and add that to a string

# Use regex to generate pattern to find words
word_pattern = re.compile('\w+')

# Use regex findall method to generate list of words from the string output by read() method
words = word_pattern.findall(opened_file.read())

# Use a dictionary to build a string that we will write to report.txt
word_occurence = {}

for word in words:
    if word in word_occurence:
        word_occurence[word] += 1
    else:
        word_occurence[word] = 1

# By here, we've built a working dictionary

# Build a string that we will place into report.txt

output_string = ''

# Function to use as parameter when sorting list of tuples. Can also use lambda function.
def sort_by_second_item_in_tuple(word_pair):
    return word_pair[1]

for word_tuple in sorted(word_occurence.items(), key = sort_by_second_item_in_tuple, reverse = True):
    output_string += "'{}' ........ {} \n".format(word_tuple[0], word_tuple[1])

# write to report.txt
open('report.txt', 'w').write(output_string)
