import re
import operator

# Open STOPWORDS.txt and PRIDPREJ.txt, bind their contents to variables, then close the files
stopwords_file = open("Resources/STOPWORDS.txt")
stopwords = stopwords_file.read().lower().split("\n")
stopwords_file.close()

pride_file = open("Resources/PRIDPREJ.txt")
pride_n_prejudice = pride_file.read()
pride_file.close()

# Remove useless characters from the book's text
banned_chars = "=?;:`_.,!+|()\""
for c in banned_chars:
    pride_n_prejudice = pride_n_prejudice.replace(c, '')

# Replace newlines with spaces
# This may cause sequences of multiple spaces
pride_n_prejudice = pride_n_prejudice.replace('\n', ' ')

# Remove content enclosed in brackets, or sequences of multiple single quotes or hyphens
pride_n_prejudice = re.sub(r"\[.*?\]|\'\'|-{2,}", '', pride_n_prejudice)

# Replace sequences of multiple spaces with a single space
pride_n_prejudice = re.sub(r" +", ' ', pride_n_prejudice)

# Create a list of the words in the book, removing those that are stop words
pride_n_prejudice = [word for word in pride_n_prejudice.lower().split(' ') if word not in stopwords]

# Create a dictionary with each unique word as a key
# If the word has not been seen, make it a key and initialize value as 1
# If the word has been seen, increase the key's value by 1
wordDict = {}

for word in pride_n_prejudice:
    if word in wordDict:
        wordDict[word] += 1
    else:
        wordDict[word] = 1

# Sort the (key, value) pairs by value in descending order, taking the first 10 entries
topten = dict(sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)[:10])

# Print the (key, value) pairs in topten
# These are the top ten most used words in the book
i = 1
for key, value in topten.items():
    print("%d. %s: %d" % (i, key, value))
    i += 1