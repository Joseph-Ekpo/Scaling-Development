# Implement the count_marketers function. 
# It should accept a list of strings (job titles) and return: 
# the number of users who've set their title to "marketer". 

# * LockedIn users sometimes use different casing in their titles, so make sure to account for that.
def count_marketers(job_titles):
    count = sum(1 for title in job_titles if title.casefold() == "marketer")
    return count
