def is_pangram(sentence):
    # check if sentence is a pangram or not
    # create a list of size 26 with 0s, for each alphabet letter
    alphabet_counters = [0] * 26

    # convert the sentence to lower case
    lower_case_sentence = sentence.lower()

    # go through the sentence character by character
    # and increment that character in the counters list

    for i in range(len(lower_case_sentence)):
        character_i = lower_case_sentence[i]

        char_value = ord(character_i) - ord('a')
        if char_value >= 0 and char_value <= 25:        # if the character is a letter
            alphabet_counters[char_value] += 1

    # now go through the counters list
    # If any of the counters list is zero, then that character is not
    # in the sentence and therefore, that sentence is not a pangram, so return False

    for j in range(len(alphabet_counters)):
        if alphabet_counters[j] == 0:
            return False

    # if we fall out of the loop above, return True, since all characters are in the sentence
    return True


# print(is_pangram("az the quick brown fox jumps over the Lazy Dog"))
# print(is_pangram("abcde"))
