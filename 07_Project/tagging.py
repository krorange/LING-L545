# This is a program that runs BookNLP's supersense tagger

from booknlp.booknlp import BookNLP

model_params={
		"pipeline":"supersense,entity", 
		"model":"big"
	}
	
booknlp=BookNLP("en", model_params)

# Input file to process
input_file="/media/secure_volume/output/FILENAME.txt"

# Output directory to store resulting files in
output_directory="/media/secure_volume/output"

# File within this directory will be named ${book_id}.entities, ${book_id}.tokens, etc.
book_id="AUTHOR&YEAR"

booknlp.process(input_file, output_directory, book_id)

