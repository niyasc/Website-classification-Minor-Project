import re
import nltk
from collections import OrderedDict
from nltk import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

def strip_non_ascii(string):
	''' Returns the string without non ASCII characters'''
	stripped = (c for c in string if 0 < ord(c) < 127)
	return ''.join(stripped)

lmtzr = WordNetLemmatizer()
porter_stem = PorterStemmer()
wordnet_tag ={'NN':'n','JJ':'a','VB':'v','RB':'r'}

class DataClean:

    def removeFreqone(self,list):
        new_list={}
        for a in list :
            try:
                new_list[a] += 1
            except:
                new_list[a] = 0
        return [a for a in new_list.keys() if new_list[a] > 0]

    def __init__(self,text):
        text=strip_non_ascii(text)
        data = text.lower()
        tokens = nltk.word_tokenize(data)
        #self.filtered_words ="#4"
        
        tagged = nltk.pos_tag(tokens)
        print (tagged)
        #self.filtered_words ="#4"
        
        
        word_list = []
        for t in tagged:
            try:
                word_list.append(lmtzr.lemmatize(t[0],wordnet_tag[t[1][:2]]))
            except:
                word_list.append(porter_stem.stem_word(t[0]))

        self.filtered_words = [w for w in word_list if not w in stopwords.words('english')]
	
        #Now removal of terms with frequency =1  [ paper mentions about this ]
        self.filtered_words = self.removeFreqone(self.filtered_words)


    def GetData(self):
        return self.filtered_words

text = "Abrahamic religions also Abrahamism are the monotheistic faiths of Middle Eastern origin, emphasizing and tracing their common origin to Abraham or recognizing a spiritual tradition identified with him. They are one of " 
print(DataClean(str(text)).GetData())
