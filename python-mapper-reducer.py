#!/usr/bin/env python
import sys
 
# Get input lines from stdin
for line in sys.stdin:
    # Remove spaces from beginning and end of the line
    line = line.strip()

    # Split it into words
    words = line.split()

    # Output tuples on stdout
    for word in words:
        print '%s\t%s' % (word, "1")


#!/usr/bin/env python
import sys
 
# Create a dictionary to map words to counts
wordcount = {}
 
# Get input from stdin
for line in sys.stdin:
    #Remove spaces from beginning and end of the line
    line = line.strip()
 
    # parse the input from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        wordcount[word] = wordcount[word]+count
    except:
        wordcount[word] = count
 
# Write the tuples to stdout
# Currently tuples are unsorted
for word in wordcount.keys():
    print '%s\t%s'% ( word, wordcount[word] )

