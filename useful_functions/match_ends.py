def match_ends(words):
    # BEGIN SOLUTION
    count = 0
    for word in words:
        if (len(word) > 1) & (word[-1] == word[0]):
            count += 1
    # END SOLUTION
    return count


print(match_ends(['abcdea', 'abcxa']) == 2)
print(match_ends(['tallest', 'lovely', 'julsfsj']) == 2)
print(match_ends(['python', 'civic']) == 1)
print(match_ends(['ww', 'tt', 'sn', 'bt', 'tt']) == 3)
