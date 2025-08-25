# Task: Write count_letters(word) using a dictionary and return the number of letters in the given word.

class CountLetters:

    def __init__(self):
        pass

    def count_letters(self, word):
        unique_letter_count = {}
        for letter in word:
            if not letter.isalpha():
                continue
            else:
                letter = letter.lower()
            
                if letter not in unique_letter_count:
                    unique_letter_count[letter] = 1
                else:
                    unique_letter_count[letter] += 1
                
        # print(unique_letter_count)

        return len(unique_letter_count)
    

media_tool1 = CountLetters()
# print(media_tool1.count_letters("Joseph Ekpo"))
media_tool1 = CountLetters()

print(f"String: k+.6hH,98D\"Mk., My count: {media_tool1.count_letters('k+.6hH,98D\"Mk.')}\nCorrectAnswer: 3\n")
print(f"String: {{+@^\", My count: {media_tool1.count_letters('{+@^\"')}\nCorrectAnswer: 0\n")
print(f"String: 0N:#pj*, My count: {media_tool1.count_letters('0N:#pj*')}\nCorrectAnswer: 3\n")
print(f"String: [jj%ne<(, My count: {media_tool1.count_letters('[jj%ne<(')}\nCorrectAnswer: 4\n")
print(f"String: G}}r)^aJf`/4Q, My count: {media_tool1.count_letters('G}r)^aJf`/4Q')}\nCorrectAnswer: 6\n")
print(f"String: %h a+, My count: {media_tool1.count_letters('%h a+')}\nCorrectAnswer: 2\n")
print(f"String: 5)?MW, My count: {media_tool1.count_letters('5)?MW')}\nCorrectAnswer: 2\n")
print(f"String: q`(z|IB2Vci, My count: {media_tool1.count_letters('q`(z|IB2Vci')}\nCorrectAnswer: 6\n")


