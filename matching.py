perfect_answer = "Data science is a multi-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from data in various forms, both structured and unstructured, similar to data mining. Data science is a concept to unify statistics, data analysis, machine learning and their related methods in order to understand and analyze actual phenomena with data. It employs techniques and theories drawn from many fields within the context of mathematics, statistics, information science, and computer science."

recorded_answer = "Data science is the field of study that combines domain expertise, programming skills, and knowledge of math and statistics to extract meaningful insights from data. Data science practitioners apply machine learning algorithms to numbers, text, images, video, audio, and more to produce artificial intelligence (AI) systems that perform tasks which ordinarily require human intelligence. In turn, these systems generate insights that analysts and business users translate into tangible business value."

      
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

#############################################################

p_ans = re.sub('[^a-zA-Z]', ' ', perfect_answer)
p_ans = p_ans.lower()
p_ans = p_ans.split()
ps = PorterStemmer()
p_ans = [ps.stem(word) for word in p_ans if not word in set(stopwords.words('english'))]
p_ans = ' '.join(p_ans)

r_ans = re.sub('[^a-zA-Z]', ' ', recorded_answer)
r_ans = r_ans.lower()
r_ans = r_ans.split()
# ps = PorterStemmer()
r_ans = [ps.stem(word) for word in r_ans if not word in set(stopwords.words('english'))]
r_ans = ' '.join(r_ans)

############################################################

from gensim import corpora
p_ans_dictionary = corpora.Dictionary([p_ans.split()])
p_ans_dictionary.save('/tmp/perfect_answer.dict')  # store the dictionary, for future reference
print(p_ans_dictionary)


###########################################################

print(p_ans_dictionary.token2id)

###########################################################

corpus = p_ans_dictionary.doc2bow(recorded_answer.lower().split())

corpora.MmCorpus.serialize('/tmp/p_ans.mm', [corpus])

##############################################################

from gensim import models
lsi = models.LsiModel([corpus], id2word=p_ans_dictionary, num_topics=2)

vec_bow = p_ans_dictionary.doc2bow(r_ans.lower().split())
vec_lsi = lsi[vec_bow]

from gensim import similarities
index = similarities.MatrixSimilarity(lsi[[corpus]])  # transform corpus to LSI space and index it

###############################################################

sims = index[vec_lsi]

print(list(enumerate(sims)))  # print (document_number, document_similarity) 2-tuples
