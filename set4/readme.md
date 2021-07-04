Exercise 1 - wordy pyramid
(alternative method using refractor - easier to read visually without having to have double up on the same coding)

pyramid = []

for i in range(3,21,2): (first half > values in the range are the start, stop, step to create the pyramid)
word = get_a_word(i)
pyramid.append(word)

for i in range(20,3,-2): (second half of pyramid)
word = get_a_word(i)
pyramid.append(word)

def get_a_word(i):
url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={}"
response = requests.get(url.format(i))
word = response.text

return word

(Value at end of URL determines the word length - needs to be formatted to change its value in the loop)
