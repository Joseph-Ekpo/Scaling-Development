# https://github.com/realpython/materials/blob/master/generators/techcrunch.csv

# It’s time to do some processing in Python! To demonstrate how to build pipelines with generators, you’re going to analyze this file to get the total and average of all series A rounds in the dataset.

# Let’s think of a strategy:

# Read every line of the file.
# Split each line into a list of values.
# Extract the column names.
# Use the column names and lists to create a dictionary.
# Filter out the rounds you aren’t interested in.
# Calculate the total and average values for the rounds you are interested in.

# To dig even deeper, try figuring out the average amount raised per company in a series A round. This is a bit trickier, so here are some hints:

# Generators exhaust themselves after being iterated over fully.
# You will still need the sum() function.

