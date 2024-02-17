import nltk
from nltk.corpus import stopwords
# from gensim.models import Word2Vec#����ʧ��

# �ִʺ�ȥ��ͣ�ô�
nltk.download('punkt')
nltk.download('stopwords')

corpus=["I come to China to travel",
        "This is a car popular in China",
        "I love tea and Apple",
        "The work is to write some papers in science"]

stop_words = set(stopwords.words('english'))
preprocessed_corpus = []

for sentence in corpus:
  words = nltk.word_tokenize(sentence.lower())
  words = [word for word in words if word.isalnum() and word not in stop_words]
  preprocessed_corpus.append(words)
# ѵ��Word2Vecģ��
model = Word2Vec(preprocessed_corpus, size=100, window=5, min_count=1, workers=4)

# ��ȡ������
word_vectors = model.wv
for word in word_vectors.vocab:
    print("��:", word)
    print("������:", word_vectors[word])
    print()
