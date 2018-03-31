import re
import json
from os import path
from nltk.tokenize import word_tokenize as tokenize
import nltk
import itertools
import numpy as np
# import cPickle as pickle
from nltk.corpus import movie_reviews, stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

WHITELIST = '0123456789abcdefghijklmnopqrstuvwxyz '

NEG_CONTRACTIONS = [
    (r'aren\'t', 'are not'),
    (r'can\'t', 'can not'),
    (r'couldn\'t', 'could not'),
    (r'daren\'t', 'dare not'),
    (r'didn\'t', 'did not'),
    (r'doesn\'t', 'does not'),
    (r'don\'t', 'do not'),
    (r'isn\'t', 'is not'),
    (r'hasn\'t', 'has not'),
    (r'haven\'t', 'have not'),
    (r'hadn\'t', 'had not'),
    (r'mayn\'t', 'may not'),
    (r'mightn\'t', 'might not'),
    (r'mustn\'t', 'must not'),
    (r'needn\'t', 'need not'),
    (r'oughtn\'t', 'ought not'),
    (r'shan\'t', 'shall not'),
    (r'shouldn\'t', 'should not'),
    (r'wasn\'t', 'was not'),
    (r'weren\'t', 'were not'),
    (r'won\'t', 'will not'),
    (r'wouldn\'t', 'would not'),
    (r'ain\'t', 'am not') # not only but stopword anyway
]

OTHER_CONTRACTIONS = {
    "'m": 'am',
    "'ll": 'will',
    "'s": 'has', # or 'is' but both are stopwords
    "'d": 'had'  # or 'would' but both are stopwords
}

BLACKLIST_STOPWORDS = ['over','only','very','not','no']

def clean_data(text, entry):
	sentences = texts
	# Converting all the text to lower cases
	text = sentences.lower()

	# Converting all negative contractions words
	for t in NEG_CONTRACTIONS:
		sentences = re.sub(t[0], t[1], text)

	# Converting the sentences into specific tokens
	tokens = tokenize(sentences)
	
	# converting some other contractions such as 'm as m
	tokens = [OTHER_CONTRACTIONS[token] if OTHER_CONTRACTIONS.get(token) else token for token in tokens]

	
	ENGLISH_STOPWORDS = set(stopwords.words('english'))
	remove_punc = r'[a-z]+'
	# Removing all the punctuations from the tokens
	tokens = [word for word in tokens if re.search(remove_punc, word)]
	
	# Removing all the English Stop words
	tokens = [token for token in tokens if token not in ENGLISH_STOPWORDS]

	# Stemming the Tokens
	stemmer = nltk.PorterStemmer()
	tokens = [stemmer.stem(word) for word in tokens]

	# Lemming the tokens
	wordnet_lemmatizer = WordNetLemmatizer()
	tokens = [ wordnet_lemmatizer.lemmatize(word) for word in tokens]

	return tokens