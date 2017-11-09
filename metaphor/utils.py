from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from collections import defaultdict
import random

def get_language(text):
    score = defaultdict(int)
    words = word_tokenize(text.lower())
    stopwords.ensure_loaded
    stopwords_dict = {lang:stopwords.words(lang) for lang in stopwords.__dict__.get('_fileids')}
    for word in words:
        for lang,stop_list in stopwords_dict.iteritems():
            if word in stop_list:
                score[lang] += 1
    if score:
        max_value = max(score.values())
        if max_value > 1:
            max_keys = [k.capitalize() for k,val in score.iteritems() if val == max_value]
            return (' or ').join(max_keys)
    return 'English'

def get_nouns(text):
    nouns = []
    for word,pos in pos_tag(word_tokenize(str(text))):
        if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
            nouns.append(word)
    return nouns

def get_random_connectors(num):
    connectors = ['and','whereas','on the other hand','yet','likewise','similarly','also','for one thing',
        'for another thing','in addition','furthermore','in other words','meanwhile']
    selection = [connectors[random.randint(1,len(connectors)-1)] for i in range(0,num)]
    return selection