#!/usr/bin/python
import sys

# 
# INSERT DESCRIPTION HERE
#
def count_letters(word_list):
	"""
	a helper function for counting letters in a list of words,
	and return the number of letters.
	"""
	letter_sum = 0
	for a_word in word_list:
		letter_sum += len(a_word)
	return letter_sum
def whitespace_list_generator(justify_length, word_sum, word_number):
	"""
	a helper function for generating a list of the number of whitespace 
	"""
	whitespace_list = []
	if word_number == 1:
		return [0]
	for dummy_index in range(justify_length - word_sum):
		whitespace_index = dummy_index % (word_number - 1)
		if whitespace_index >= len(whitespace_list):
			whitespace_list.append(1) 
		else:
			whitespace_list[whitespace_index] += 1
	#print justify_length - word_sum
	return whitespace_list

def concatenate_words(word_list, whitespace_list):
	"""
	a helper function for concatenate words from a word list, 
	using a certain number of whitespace, 
	and then return the string
	"""
	if word_list == []:
		return ""
	a_string = ""
	dummy_index = 0
	# print whitespace_list
	for a_word in word_list[ : -1]:
		# print dummy_index, a_word
		a_string +=  a_word + " " * whitespace_list[dummy_index]
		dummy_index += 1
	a_string += word_list[-1]
	return a_string

def justify(file_name, justify_length):
	input_file = open(file_name)
	input_text = input_file.read()
	input_lines = input_text.split("\n")
	input_lines = input_lines[ : -1]

	word_list = []
	for a_line in input_lines:
		word_list = a_line.split(" ")
		word_sum = count_letters(word_list)
		if (word_sum + len(word_list)) > justify_length:
			exit("Justify length error. lines are longer than the input justify length.")
		whitespace_number = whitespace_list_generator(justify_length, word_sum, len(word_list))
		print concatenate_words(word_list, whitespace_number)


# Program justifies text contents of a given file
# This is the actual code that gets run when the
# program is run. 
#
# DO NOT EDIT BELOW HERE.
if __name__ == "__main__":

	file_name = ''
	length = -1

	# Parse command line arguments
	try:
		for i in range(len(sys.argv)):
			if sys.argv[i] == '-f':
				file_name = sys.argv[i+1]
			elif sys.argv[i] == '-l':
				length = int(sys.argv[i+1])
	except:
		exit('Input error. Example input: justifytext -f mytextfile -l 80')

	if file_name == "" or length < 1:
		exit('Input error. Example input: justifytext -f mytextfile -l 80')
		
	justify(file_name, length)
