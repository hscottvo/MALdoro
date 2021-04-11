from anime_comfy_levels import anime_levels
from justwatch_query import get_links
from classes import *
from mal import *
from converter import *
import csv
import concurrent.futures
import threading
import multiprocessing
import time

genres_list = Genres()
anime_id_new = []
anime_id_completed = []

FILENAME = "output.csv"
with open(FILENAME, newline = "") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[4] == "Plan to Watch":
            anime_id_new.append(row[5])
        elif row[4] == "Completed":
            anime_id_completed.append(row[5])

anime_list = []

def main():
    xmlinput = input("enter xml file name: ")
    parse_xml(xmlinput)
    choice = input("new or completed? (n/c): ")
    curr_id = []
    if choice.lower() == "n":
        curr_id = anime_id_new
    else:
        curr_id = anime_id_completed
    mid = int(len(curr_id) / 2)
    left = int(mid/2)
    right = int(mid + left)

    process1 = curr_id[:left]
    process2 = curr_id[left:mid]
    process3 = curr_id[mid:right]
    process4 = curr_id[right:]


    start = time.perf_counter()
    # Alpha Future Processing
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(anime_levels,process1)
        for result in results:
            anime_list.append(result)
    print("Process 1 complete")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(anime_levels,process2)
        for result in results:
            anime_list.append(result)
    print("Process 2 complete")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(anime_levels,process3)
        for result in results:
            anime_list.append(result)
    print("Process 3 complete")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(anime_levels,process4)
        for result in results:
            anime_list.append(result)
    print("Process 4 complete")

    end = time.perf_counter()

    print(anime_list[0].title, get_links(anime_list[0].title))
    
    genre_specific = []
    specified_genres = ["Slice of Life","Romance", "Harem"]
    for show in anime_list:
        if(show.genre_exist(specified_genres)):
            genre_specific.append(show)
    
    for show in genre_specific:
        print(show.title)
    

    print(f'finished in {round(end-start,2)} second(s)')

if __name__ == "__main__":
    main()