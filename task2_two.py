from collections import Counter
paragraph="Hey! how u doing?"
words=paragraph.split()
words_counter=Counter(words)
top_three=words_counter.most_common(3)
print(top_three)