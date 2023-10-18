#This project is about to create a search engine for a given set of words
#the engine will take the words and search for them in a given set of files' titles
#if the word or words are found in the file's title, the engine will return the file name
#but if the word or words are not found in the file's title, the engine will search for the 
#most similar word to the given word or words and return the file name that contains the most similar word

#the code starts here
#first we import the necessary libraries
import os
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

#we define a function to clean the text
def clean_text(text):
    text = text.lower() #lowercase
    text = re.sub(r'\d+', '', text) #remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation)) #remove punctuation
    text = text.strip() #remove whitespaces
    return text

#we define a function to tokenize the text
def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens

#we define a function to remove stopwords
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w in stop_words]
    return filtered_tokens

#we define a function to stem the words
def stem_words(tokens):
    ps = PorterStemmer()
    stemmed_tokens = [ps.stem(w) for w in tokens]
    return stemmed_tokens

#we define a function to calculate the similarity between two words
def similarity(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    word1 = set(word1)
    word2 = set(word2)
    return len(word1 & word2) / len(word1 | word2)

#we define a function to calculate the similarity between a word and a list of words
def similarity_list(word, list):
    word = word.lower()
    word = set(word)
    max = 0
    for i in list:
        i = i.lower()
        i = set(i)
        if len(word & i) / len(word | i) > max:
            max = len(word & i) / len(word | i)
    return max

#we define a function to extract from a csv file the titles of the files
def extract_titles():
    titles = []
    with open('titles.csv', 'r') as f:
        for line in f:
            titles.append(line.strip())
    return titles

