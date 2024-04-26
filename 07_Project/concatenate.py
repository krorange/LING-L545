# This is a program that concatenates a supersense-tagged file and a tokens file

dictionary = {}

#start_token	end_token	supersense_category	text
#7	7	noun.location	WORLD

first = True
for line in open('/media/secure_volume/output/FILENAME.supersense').read().split('\n'):
	if line.strip() == '':
		continue
	if first:
		first = False
		continue
	row = line.split('\t')
	# row[0] = start_token
	begin = int(row[0])
	# row[1] = end_token
	end = int(row[1])
	# row[2] = supersense_category
	for i in range(begin, end+1):
		dictionary[i]=row[2]
#print(dictionary)

#paragraph_ID	sentence_ID	token_ID_within_sentence	token_ID_within_document	word	lemma	byte_onset	byte_offset	POS_tag	fine_POS_tag	dependency_relation	syntactic_head_ID	event
#1	0	0	0	*	*	3	4	PUNCT	NFP	meta	4	O

first = True
for token in open('/media/secure_volume/output/FILENAME.tokens').read().split('\n'):
	if token.strip() == '':
		continue
	if first:
		first = False
		header = token.strip() + "\tsupersense_category"
		print(header)
		continue
	row = token.split('\t')
	# row[3] = token_ID_within_document
	token_ID = int(row[3])
	supersense = '_'
	if token_ID in dictionary:
		supersense = dictionary[token_ID]
	row.append(supersense)
	print('\t'.join(row))
