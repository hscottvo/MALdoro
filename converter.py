# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd
from classes import *



def parse_xml(filename):  
    cols = ["series_title","series_episodes","my_watched_episodes","my_status","series_animedb_id","series_type"]
    rows = []
    
    # Parsing the XML file
    xmlparse = Xet.parse(filename)
    root = xmlparse.getroot()
    for i in root:
        series_title = getattr(i.find('series_title'), 'text', None)
        # print('Found Series Title: ' + series_title)   
        series_episodes = getattr(i.find('series_episodes'), 'text', None)
        print('Found Series Episodes: ' + str(series_episodes))
        my_watched_episodes = getattr(i.find('my_watched_episodes'), 'text', None)
        print('Found My Watched Episodes: ' + str(my_watched_episodes))
        my_status = getattr(i.find('my_status'), 'text', None)
        print('Found My Status: ' + str(my_status))
        series_animedb_id = getattr(i.find('series_animedb_id'), 'text', None)
        print('Found Series Animedb ID: ' + str(series_animedb_id))
        series_type = getattr(i.find('series_type'), 'text', None)
        print('Found Series Type: ' + str(series_type))
        print('')
    
        rows.append({"series_title": series_title,
                     "series_episodes": series_episodes,
                     "my_watched_episodes": my_watched_episodes,
                     "my_status": my_status,
                     "series_animedb_id": series_animedb_id,
                     "series_type": series_type})


    
    df = pd.DataFrame(rows, columns=cols)



    # Writing dataframe to csv
    df.to_csv('output.csv')

def load_file(filename):
    df = pd.read_csv(filename,index_col=0)
    loaded_animes = []
    for row in df.iterrows():
        obj = Anime_Obj(row[1]["Title"],row[1]["Stress Level"],row[1]["Calm Level"],row[1]["Neutral Level"],row[1]["Genres"])
        loaded_animes.append(obj)
    return loaded_animes