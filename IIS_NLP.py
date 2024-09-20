import pandas as pd
import nltk
import matplotlib.pyplot as plt

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')



stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

df = pd.read_csv('nlp_data.csv')
text_field = df['text']
text_field=text_field[1:]
def myfn(tuple):
    return tuple[1]

sentences=[]
for i in range(1,41152):
    sentences.append(text_field[i])
print("The output in sentence seperated list: ", end="\n")

print(sentences[0:10])
print()

# A) WORD TOKENIZED SENTENCES
word_tokenized=[]

for i in sentences:
    word=word_tokenize(i)
    word_tokenized.append(word)
print("The output in word seperated sublists: ", end="\n")

print(word_tokenized[0:10])
print()
# B) REMOVING THE STOPWORDS FROM A PART
stopword_final=[]
for i in word_tokenized:
    partial=[]
    for j in i:
        if j.lower() not in stop_words:

            partial.append(j)

    stopword_final.append(partial)
print("The output in word seperated sublists after removing the stopwords: ", end="\n")

print(stopword_final[0:10])
print()
# C) STEMMING THE STOPWORD LIST
stem_list=[]
for i in stopword_final:
    partial=[]
    for j in i:
        words=stemmer.stem(j)
        partial.append(words)
    stem_list.append(partial)
print("The output in word seperated sublists after stemming: ", end="\n")
print(stem_list[0:10])
print()
# D) LEMMITIZING THE STOPWORD LIST
lemm_list=[]
for i in stopword_final:
    partial2=[]
    for j in i:
        words=lemmatizer.lemmatize(j)
        partial2.append(words)
    lemm_list.append(partial2)
print("The output in word seperated sublists after lemmitizing: ", end="\n")
print(lemm_list[0:10])
print()
# E) POS TAGGING
pos_list=[]
for i in stopword_final:

    pos_words=pos_tag(i)
    pos_list.append(pos_words)
    
print("The output in word seperated sublists with each word after pos tagging: ", end="\n")
print(pos_list[0:10])
print()

stopword_words=[]
# F) CREATING A DICTIONARY TO FIND THE FREQUENCY OF EACH WORD INDIVIDUALLY

dict1={}
for i in stopword_final:
    partial=[]
    for j in i:
        if j.isalpha():
            partial.append(j)
        else:
            continue
    stopword_words.append(partial)




for i in stopword_words:

    for j in i:
        if j in dict1:
            dict1[j]=dict1[j]+1
        else:
            dict1[j]=1

print("The output showing the frequency of words in list format in descending order: ", end="\n")


words_list = sorted(dict1.items(), key=myfn, reverse=True)
print(words_list[0:30])
print()
# G) PLOTTING THE GRAPH OF 15MOST USED WORDS IN THE DATA
frequent_words = words_list[:15]

print("The output showing the frequency of 15 most popular words: ", end="\n")
print(frequent_words)
print()

phrases, frequency = zip(*frequent_words)


plt.figure(figsize=(1000, 8))
plt.bar(phrases, frequency,color='black')
plt.xlabel('Phrase')
plt.ylabel('Frequency')
plt.title('15 Most Frequent Words')
plt.xticks(rotation=30)
# the graph output command
plt.show()











