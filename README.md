University Text Processing System

Overview
This project implements a Natural Language Processing (NLP) system that analyzes and processes textual data. The system loads text data from a CSV file, performs various NLP tasks (tokenization, stopword removal, stemming, lemmatization, part-of-speech tagging), and produces a frequency analysis of the most commonly used words. A bar graph is plotted to visualize the 15 most frequent words in the text data.

Features--
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The system includes the following NLP tasks:

Tokenization:
Each sentence is split into individual words (tokens) using the word_tokenize() function.

Stopword Removal:
Common words that don't add much meaning to sentences (e.g., "the", "is") are filtered out using NLTK's stopwords.

Stemming:
Words are reduced to their root form using the Porter Stemmer. For example, "running" becomes "run".

Lemmatization:
Words are converted to their dictionary form using WordNetLemmatizer. This is similar to stemming but more accurate as it considers the meaning of the word.

Part-of-Speech (POS) Tagging:
Each word is assigned a part of speech (noun, verb, adjective, etc.), which helps in understanding the role of the word in a sentence.

Word Frequency Analysis:
A frequency dictionary is created, counting the occurrences of each word after preprocessing. The most frequent words are displayed in a sorted list.

Data Visualization
The 15 most frequent words are visualized using a bar graph.

How to Run--
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Clone or Download the Repository: Ensure you have the CSV file nlp_data.csv containing the text data in the same directory as the Python script.

Install Dependencies: Install the required libraries using pip:
pip install pandas nltk matplotlib

Run the Script: Run the Python script that contains the code using the following command:
python nlp_script.py

Output:
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1)The script will display word-tokenized sentences, lists of words after stopword removal, stemming, lemmatization, and POS tagging.
2)It will also print a list of the 30 most frequent words and their frequencies.
3)Finally, a bar graph showing the 15 most frequent words will be displayed.
