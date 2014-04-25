import csv

file_name = 'fp.csv'

data = []

with open(file_name, 'rbU') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row[0])

finger_print = []
tweet = []

for i in range(len(data)):
    if i%2:
        tweet.append(data[i])
    else:
        finger_print.append(data[i])

# remove punctuation
import string
exclude = set(string.punctuation)
for i in range(len(tweet)):
    tweet[i] = ''.join(ch for ch in tweet[i] if ch not in exclude)

from nltk import word_tokenize
from nltk import stem
class LemmaTokenizer(object):
    def __init__(self):
        self.porter = stem.porter.PorterStemmer()
    def __call__(self, doc):
        from nltk.corpus import stopwords
        tmp = [self.porter.stem(t) for t in word_tokenize(doc)]
        return [t for t in tmp if t not in stopwords.words('english')]

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(tokenizer=LemmaTokenizer())
X = vectorizer.fit_transform(tweet).toarray()

output = [[ name.encode('utf-8') for name in vectorizer.get_feature_names() ]]
for x in X:
    output.append(x)


o_file = "bow_tf.csv"
resultFile = open(o_file, 'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerows(output)
