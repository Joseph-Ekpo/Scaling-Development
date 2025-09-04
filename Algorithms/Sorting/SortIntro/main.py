class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line

# The vanity function accepts an instance of an Influencer and returns their vanity score.
# The vanity score should be:
#   the number of links in their bio multiplied by 5, plus their number of selfies. (Links in bio are weighted more heavily)
def vanity(influencer):
    vanity_score = influencer.num_bio_links * 5 + influencer.num_selfies
    return vanity_score


# The vanity_sort function should return a list of influencers, ordered by their vanity from least to greatest.
# You can pass a function as a named parameter called key to sorted to control the metric the sorting algorithm will use for comparisons.
def vanity_sort(influencers):
    influencer_by_vanity = sorted(influencers, key=vanity)
    return influencer_by_vanity

celeb1 = Influencer(0, 200)
celeb2 = Influencer(100, 1)

print(vanity_sort([celeb1, celeb2]))