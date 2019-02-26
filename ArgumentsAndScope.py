def shout_echo(word1, echo = 1, intense = False):
    shout_word = word1 * echo

    if intense:
        new_shout_word = shout_word.upper() + '!!!'
    else:
        new_shout_word = shout_word + '!!!'
    return new_shout_word

print(shout_echo('Hey', echo=5, intense=True))
print(shout_echo('Hey', intense=True))

# def funcname (arg1, default=[]):
# def funcname(*args):
# def funcname (**kwargs):
