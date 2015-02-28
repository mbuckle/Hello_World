# Define a function to reverse a sentence
def reverse_sentence(old_sentence):
	print old_sentence
	new_sentence = ""
	saved_index = 0
	
	for index in range(0,len(old_sentence)):
		if old_sentence[index] == " ":
			new_sentence = old_sentence[saved_index:index+1]+new_sentence
			saved_index = index+1
		elif index == len(old_sentence)-1:
			new_sentence = old_sentence[saved_index:index+1]+" "+new_sentence
	print new_sentence

old_sentence = raw_input("Enter a sentence: ")
reverse_sentence(old_sentence)

split_sentence = old_sentence.split()
print split_sentence
new_sentence = ""
for index in range(0,len(split_sentence)):
	new_sentence = new_sentence + split_sentence[len(split_sentence)-index-1] + " "
print new_sentence
