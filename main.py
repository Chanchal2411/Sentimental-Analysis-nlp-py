import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import matplotlib.pyplot as plt


text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower() 
clean_text = lower_case.translate(str.maketrans('','',string.punctuation))

tokenized_word = word_tokenize(clean_text,"english")
#word_tokenize will take less time then split

final_words = []
for word in tokenized_word:
    if word not in stopwords.words('english'):
        final_words.append(word)

print(final_words)
emotion_list = []

with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter (emotion_list)
print(w)

def sentimental_analysis(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg>pos:
        print("Negative Sentiment")
    elif pos>neg:
        print("Positive Sentiment")
    else:
        print("Neutral Vibe")


sentimental_analysis(clean_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()

