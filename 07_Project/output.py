# This is a program that outputs the number of animal/plant/human agents (nsubj)

#paragraph_ID	sentence_ID	token_ID_within_sentence	token_ID_within_document	word	lemma	byte_onset	byte_offset	POS_tag	fine_POS_tag	dependency_relation	syntactic_head_ID	event	supersense_category
#1	0	0	0	*	*	3	4	PUNCT	NFP	meta	4	O	_

first = True
current_sentence_id = 0
current_sentence = []
fd = open('/media/secure_volume/supersense/FILENAME.complete')
line = fd.readline()

num_ani = 0
num_pla = 0
num_hum = 0
sum_ani = 0
sum_pla = 0
sum_hum = 0

while line:
	if first:
		first = False
		line = fd.readline()
	row = line.strip().split('\t')

	if int(row[1]) != current_sentence_id:
		for sentence_row in current_sentence:
			#print(sentence_row)
			if sentence_row[13] in ['noun.animal'] and sentence_row[10] in ['nsubj']:
				#print(current_sentence_id,':::',' '.join([i[4] for i in current_sentence]))
				num_ani += 1
				sum_ani = str(num_ani)
			if sentence_row[13] in ['noun.plant'] and sentence_row[10] in ['nsubj']:
				#print(current_sentence_id,';;;',' '.join([i[4] for i in current_sentence]))
				num_pla += 1
				sum_pla = str(num_ani)
			if sentence_row[13] in ['noun.person'] and sentence_row[10] in ['nsubj']:
				#print(current_sentence_id,'!!!',' '.join([i[4] for i in current_sentence]))
				num_hum += 1
				sum_hum = str(num_ani)
				break
		current_sentence_id = int(row[1])
		current_sentence = []
	else:	
		current_sentence.append(row)
		
	line = fd.readline()

print(sum_ani)
print(sum_pla)
print(sum_hum)