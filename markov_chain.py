#!/usr/bin/env python

import markovify

# Read text file, replace new lines with spaces, and save to variable
with open ("ndt.txt", "r") as myfile:
      ndt_text=myfile.read().replace('\n', '')

# Build the model.
text_model = markovify.Text(ndt_text)

# Print ten randomly-generated sentences of no more than 140 characters
for i in range(10):
    print(text_model.make_short_sentence(140))

