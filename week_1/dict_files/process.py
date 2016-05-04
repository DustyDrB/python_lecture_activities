# Read contents from a file
filename = 'poem.txt'
# Open with filename
opened_file = open(filename, 'rb')

# print opened_file
# Iterate through the file line by line and add that to a string
text = opened_file.read()

opened_file.close()
# Split the text into a list
list_of_text = text.split('\n')



# Use a dictionary to build a string that we will write to report.txt
word_occurence = {}


for line in list_of_text:

    # Does the key exist?
    line_list = line.split(' ')

    for word in line_list:
        if word in word_occurence:
            word_occurence[word] += 1
        else:
            word_occurence[word] = 1

# By here, we've built a working dictionary

# build a string that we will

output_string = ''
for key in word_occurence.keys():
    output_string += "Word: {}, Occurence: {} \n".format(key, word_occurence[key])

# write to report.txt
# Read contents from a file
filename = 'report.txt'
# Open with filename
opened_file = open(filename, 'w')

opened_file.write(output_string)
