"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think it will declare a variable called some_words and it'll put a list of strings into it.
some_words = ["what", "does", "this", "line", "do", "?"]

# I think it will print individual words from some_words list in order.
for word in some_words:
    print(word)  # Prints every word on a new line in order till exhausted.

# I think it will print the same as above just the variable is now called x
for x in some_words:  # it printed the same results as above
    print(x)

# It will print the list of the variable some_words
print(some_words)  # Prints the list of some_words

if len(some_words) > 3:  # prints some_words contains more than 3 words
    print(
        "some_words contains more than 3 words"
    )  # printed some_words contains more than 3 words.


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())  # I think this will print the systems attributes


usefulFunction()
