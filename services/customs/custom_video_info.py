# import spacy
from enum import unique
import pymongo
import os 

# nlp = spacy.load("en_core_web_sm")
myclient = pymongo.MongoClient("mongodb://"+ os.environ['DB_HOST']+":27017/")
mydb = myclient[os.environ['DB_NAME']]
mycol = mydb[os.environ['DB_SUBTITLES_COL']]
        
class VideoInfo():
    def __init__(self, id, views, thumbnail, duration, url_suffix, channel, subtitles, subtitles_available) -> None:
        self.id = id
        self.views = views
        self.thumbnail = thumbnail
        self.duration = duration
        self.url_suffix = url_suffix
        self.channel = channel
        self.subtitles = subtitles
        self.subtitles_available = subtitles_available
        pass
    def classify(self):
        print ("crap")
        self.extract_basic_sentences()
        pass
    def extract_basic_sentences(self):
        # you should add specific rules to this task (for each case)
        # firts case : the actual sentece end with a conjuction
        # second case : the actual sentence doesnt end with a conjunction
        #  |> a. check if the next 
        self.most_simple_case()

    # cases
    def most_simple_case(self):
        count = 0
        for e in self.subtitles:
            # check if tha last word is a stopword 
            last_word =  e['text'].split(" ")[-1]
            last_words =  e['text'].split(" ")
            # if (nlp.vocab[last_word].is_stop and len(last_words)>5):
            if (True):
                inicio = e['start']
                try:
                    fin = self.subtitles[self.subtitles.index(e)+1]['start']
                except:
                    fin = inicio
                duration = round(fin-inicio,3)
                measure = round(self.get_words_vs_secods(e["text"],fin-inicio))
                classified = {
                    "text":e["text"] ,
                    "start": inicio, 
                    "end": fin, 
                    "duration": duration, 
                    "measure":measure 
                }
                # print(classified)
                # print(e['text'], "inicio: ", inicio, "fin: ",fin )
            count+=1

    def get_words_vs_secods(self, list_words, secs):
        return len(str(list_words).split(" "))/secs if secs!=0 else len(str(list_words).split(" ")) 

    def save_on_db(self):
        mycol.create_index('id' ,unique=True)
        temporal = {"id": self.id, "views": self.views, "thumbnail": self.thumbnail, "url_suffix": self.url_suffix, "channel": self.channel, "duration": self.duration, "subtitles": self.subtitles, "subtitles_available": self.subtitles_available}
        try:
            mycol.insert_one(temporal)
        except Exception as e:
            print(e)
