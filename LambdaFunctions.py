# Simple lambda example
add_bangs = lambda x: x + '!!!'
print(add_bangs('Hello'))

"""
def echo_word(word1, echo):
    Concatenate echo copies of word1.
    words = word1 * echo
    return words
"""
echo_word = lambda x, y: x * y
print(echo_word('Hello', 5))

# Map
# Filter
# Reduce