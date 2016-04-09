#!/usr/bin/env python

import markovify

class markov:
	# Read text file, replace new lines with spaces, and save to variable
	with open ("ndt.txt", "r") as myfile:
		ndt_text = myfile.read().replace('\n', ' ')

	# Build the model.
	text_model = markovify.Text(ndt_text)
	# Make a tweet
	tweet =  text_model.make_short_sentence(140)


