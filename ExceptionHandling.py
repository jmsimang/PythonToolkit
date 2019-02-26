            # Error Handling by TRY-EXCEPT
# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Initialize empty strings: echo_word, shout_words
    echo_word = ''
    shout_words = ''
    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1 * echo
        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word + '!!!'
    except:
        # Print error message
        print("Error: word1 must be a string and echo must be an integer.")
    # Return shout_words
    return shout_words
# Call shout_echo
shout_echo("particle", echo="accelerator")
print()

            # Exception Handling by RAISING an Error
# Define shout_echo2
def shout_echo2(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    #Initialize empty strings
    echo_word = ''
    shout_words = ''
# Add exception handling
# try:
# Raise exception when echo less than 0
    if echo < 0:
        raise ValueError('echo must be greater than 0')
# Concatenate echo copies of word1 using *
    echo_word = word1 * echo
# Concatenate '!!!' to echo_word
    shout_words = echo_word + '!!!'
# except:
# Print error message
# print('Error: word1 must be a string and echo must be a positive integer.')
    return shout_words
shout_echo2('particle', echo=-1)
print()
