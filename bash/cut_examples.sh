# Display the third character from each line of text
cat - | cut -c3
# Display the second and seventh character from each line of text
cat - | cut -c2,7
# Display a range of characters starting at the second position of a string and ending at the seventh position (both positions included)
cat - | cut -c2-7
# Display the first four characters from each line of text
cat - | cut -c-4
# Given a tab delimited file with several columns (tsv format) print the first three fields
cat - | cut -f-3
# Print the characters from thirteenth position to the end
cat - | cut -c13-
# Given a sentence, identify and display its fourth word. Assume that the space (' ') is the only delimiter between words
cat - | cut -d' ' -f4
# first three words
cat - | cut -d' ' -f-3
# second field to last field
cat - | cut -f2-
