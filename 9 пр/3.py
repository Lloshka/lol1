def permute_words(words):
    result = []
    for word in words:
        if len(word) <= 1:
            result.append(word)
        else:
            shuffled_word = word[1] + word[0] + word[2:]
            result.append(shuffled_word)
    return result

word_list = ["apple", "banana", "cherry"]
permuted_words = permute_words(word_list)
print(permuted_words)