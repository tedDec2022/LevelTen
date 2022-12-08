import sys
import logging

logging.basicConfig(filename='find_max_substring.log', encoding='utf-8', level=logging.DEBUG)

def find_max_substring(text):
	"""
	Function to find thelLongest substring(s) without repeating characters in a text input
	"""

	if not type(text) == str:
		if 'logging' in globals():
			try:
				logging.exception(f"Bad input provided: {text}")
			except:
				pass
		raise Exception('`text` input must be a string')

	# Identify the length of the string, used to iterate over the characters
	num_characters = len(text)

	# Storage of largest terms found before a character repeats
	found_max_terms = {}
	
	# Starting at each character in the string, see how far you can read until
	# you find a character you've seen before
	for starting_idx in range(num_characters): 
		# Record a list of characeters we've seen
		seen_characters = []
		
		# Set an idx to increment as we read the characters in the string subset
		idx = 0
		
		# Read the characters in order until the end of the text subset, or we
		# find a character we've already seen
		while idx < (num_characters - starting_idx):
			# Read the next character
			character = text[starting_idx + idx]

			# Add the character to a temporary list of seen characters and
			# increment the reader index
			if character not in seen_characters:
				seen_characters.append(character)
				idx += 1
			# If we've seen the character before break out of reading the string
			else:
				break

		# Turn the list of characters we've already seen back into a single text term
		term = ''.join(seen_characters)
		
		# Count the length of this term, we'll add the term to a list with other
		# terms found of the same length
		len_term = len(term)
		
		# If we haven't seen a term this long before add a key for the length to the storage dict and 
		# create a set with the term found as an entry
		if len_term not in found_max_terms.keys():
			found_max_terms[len_term] = set([term])
		# If we have seen the length before add the term to the set of seen terms, using sets to avoid 
		# duplicate entries
		else:
			found_max_terms[len_term] = found_max_terms[len_term] | set([term])
	
	#Handle empty string inputs
	if len(found_max_terms.keys()) == 0:
		max_length = 0
		found_max_terms[0] = {''}
	else:
		max_length = max(found_max_terms.keys())
	
	return(found_max_terms[max_length], max_length)

def print_results(max_term_set, length):
	msg = f"{max_term_set} with the length of {length}."
	print(msg)
	return msg

if __name__ == "__main__":
	if len(sys.argv) > 1:
		print_results(*find_max_substring(sys.argv[1]))
	else:
		print('Please provide a text term to evaluate and a command line arg (i.e. python main.py LEVeL103NRGY )')