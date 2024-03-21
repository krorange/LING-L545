import sys

dictionary_file = open('dictionary.txt')
dictionary = [i.strip() for i in dictionary_file.read().split('\n')]

def MaxMatch(sentence, dictionary):
	if sentence == [] or sentence == '':
		return []
	for i in range(len(sentence), 1, -1):
		firstword = sentence[0:i]
		remainder = sentence[i:]
		if firstword in dictionary:
			return [firstword] + MaxMatch(remainder, dictionary)
	# if no word was found, so make a one-character word
	firstword = sentence[0]
	remainder = sentence[1:]
	return [firstword] + MaxMatch(remainder, dictionary)

if __name__ == "__main__":
	for sentence in sys.stdin.read().split('\n'):
		if sentence.strip() != '':
			tokens=MaxMatch(sentence.strip(), dictionary)
			print(' '.join(tokens))