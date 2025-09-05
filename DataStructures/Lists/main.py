# Implement the last_work_experience function. 
# It takes a list of our user's work history (strings) and returns the last place they worked.

# Assume the list is ordered from oldest to most recent.
# If the list is empty, return None.

def last_work_experience(work_experiences):
    last_work_place = None if len(work_experiences) == 0 else work_experiences[-1]
    return last_work_place