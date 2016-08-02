from nltk.tokenize import sent_tokenize
from nltk.tag import StanfordNERTagger
from docParser import DocToText
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

tagger = StanfordNERTagger('/home/krishh/nltk_data/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz','/home/krishh/nltk_data/stanford-ner-2015-12-09/stanford-ner.jar')

def tokenize_sent(string):
	t = sent_tokenize(string)
	#print t
	return t

def get_NER_tags(string):
	return tagger.tag(string)
	
def chunk_NER(NER_tags):
	ner_output = NER_tags
	chunked, pos = [], ""
	try:
		for i, word_pos in enumerate(ner_output):
		    word, pos = word_pos
		    if pos in ['PERSON', 'ORGANIZATION', 'LOCATION'] and pos == prev_tag:
		    	chunked[-1]+=word_pos
		    else:
		    	chunked.append(word_pos)
		    prev_tag = pos
		
		    clean_chunked = [tuple([" ".join(wordpos[::2]), wordpos[-1]]) if len(wordpos)!=2 else wordpos for wordpos in chunked]

		print clean_chunked
		return clean_chunked
	except:
		return

#s = "holla bitches. Sip? imma fine."

s = DocToText('test.doc')
tokens = tokenize_sent(s)
chunked_doc =[]
for x in tokens:
#	print x, type(x)
	a = get_NER_tags(x.split())
	chunked_doc.append(chunk_NER(a))

print chunked_doc
#	print