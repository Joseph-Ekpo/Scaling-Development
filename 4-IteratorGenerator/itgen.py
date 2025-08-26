# https://github.com/realpython/materials/blob/master/generators/techcrunch.csv

# Analyze the file to get the total and average of all series A rounds in the dataset.

# Let’s think of a strategy:

# Read every line of the file.
# Split each line into a list of values.
# Extract the column names.
# Use the column names and lists to create a dictionary.
# Filter out the rounds you aren’t interested in.
# Calculate the total and average values for the rounds you are interested in.

# Figure out the average amount raised per company in a series A round.

file_name = "/workspaces/Scaling-Development/4-IteratorGenerator/techcrunch_iterators_generators.csv"

lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)

# for i in range(10):
#     print(next(list_line))

company_dicts = (dict(zip(cols, data)) for data in list_line)

funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}\n")


# Figure out the average amount raised per company in a series A round. 
company_series_a_funding_data = {}
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)

for company_dict in company_dicts:
    if company_dict['company'] not in company_series_a_funding_data and company_dict['round'] == 'a':
        company_series_a_funding_data[company_dict['company']] = int(company_dict['raisedAmt'])

average = sum(company_series_a_funding_data.values()) // len(company_series_a_funding_data)
for company, amount_raised in company_series_a_funding_data.items():
    print(f"Company: {company}\nSeries A Funding: ${amount_raised}\n")

print()
print(f"Average amount raised per company: ${average}")


# Mini Task
# Build a generator even_numbers(n) yielding up to n

class EvenYield:

    def __init__(self):
        pass


    def even_numbers(self, n):
        for i in range(n):
            yield i
            i += 1
            


yielder = EvenYield()
numbers = yielder.even_numbers(10)

for num in numbers:
    print(num)
