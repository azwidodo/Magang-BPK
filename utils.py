import regex as re
from string import digits, punctuation

stopwords = set()
with open("stopwords_id.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        stopwords.add(line[:-1])


def preprocess_text(text):
    # case folding
    text = text.lower()

    # remove digits
    rem_digits = str.maketrans(digits, " " * len(digits))
    text = text.translate(rem_digits)

    # remove punctuations
    rem_punctuation = str.maketrans(punctuation, " " * len(punctuation))
    text = text.translate(rem_punctuation)
    text = re.sub(r'[^\w\s]', ' ', text)

    # remove stopwords
    text = " ".join([i for i in text.split() if i not in stopwords])

    return text
