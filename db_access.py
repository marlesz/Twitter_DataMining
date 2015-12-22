__author__ = 'ML'
from pymongo import MongoClient
import json
import pandas as pd
import matplotlib.pyplot as plt
import re

#ustanowienie klienta bazy MongoDB
client = MongoClient('localhost', 27017)

#dostep do bazy danych
mydb = client.Twitter

#dostep do kolekcji
myCollection = mydb.collect1

#Zliczenie twittow w bazie
twitterCount = myCollection.find().count()
print twitterCount

#Analizy statystyczne
tweets_data = myCollection.find()
tweets = pd.DataFrame()
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets_by_lang = tweets['lang'].value_counts()
#print 'Languages of tweets'
#print tweets_by_lang


#Wykres Top languages
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Top languages', fontsize=15, fontweight='bold')
tweets_by_lang[:7].plot(ax=ax, kind='bar', color='red')
#plt.show()

#slowa kluczowe
keywordsCount = []
dict = []
hospital = myCollection.find({'text': {'$regex': 'hospital', '$options': 'i'}}).count()
surgery = myCollection.find({'text': {'$regex': 'surgery', '$options': 'i'}}).count()


keyWordsCount = [hospital, surgery]
print 'stadium, sportCenter, volleyball'
print keyWordsCount

#dodaje kolekcje do tablicy
keyWords = []

for item in myCollection.find({'$or':[{'text': {'$regex': 'hospital', '$options': 'i'}} , {'text': {'$regex': 'surgery', '$options': 'i'}}]}):
    keyWords.append(item)
print 'keyWords:', len(keyWords)

#zapisuje wspolrzedne do pliku txt

#hospFile = open('hosp_wsp.txt', 'w')
#for i in range(0, len(keyWords)):
#    keyWords2 = str(keyWords[i]['geo']['coordinates']) + '\n'
#    hospFile.writelines(keyWords2)

#hospFile.close()

client.close()