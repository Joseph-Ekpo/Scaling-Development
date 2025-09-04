# merge_sort() pseudocode
# Input: A, an unsorted list of integers

# 1. If the length of A is less than 2, it's already sorted so return it
# 2. Split the input array into two halves down the middle
# 3. Call merge_sort() twice, once on each half
# 4. Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    
    left, right = merge_sort(nums[:len(nums) // 2]), merge_sort(nums[(len(nums) // 2):])
    return merge(left, right)


# merge() pseudocode
# Inputs: A and B. Two sorted lists of integers

# 1. Create a new final list of integers.
# 2. Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
# 3. Use a loop to compare the current elements of A and B. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. 
#    Otherwise, add the item in B to the final list and increment j. Continue until all items from one of the lists have been added.
# 4. After comparing all the items, there may be some items left over in either A or B. Add those extra items to the final list.
# 5. Return the final list.

def merge(first, second):

    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final
