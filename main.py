from anime_comfy_levels import anime_levels
from justwatch_query import get_links
from classes import *
from mal import *
import csv
import concurrent.futures
import threading
import multiprocessing
import time

genres_list = Genres()

start = time.perf_counter()


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
    choice = input("new or completed? (n/c): ")
    curr_id = []
    if choice.lower() == "n":
        curr_id = anime_id_new
    else:
        curr_id = anime_id_completed


    # Alpha Future Processing
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(anime_levels,id, genres_list) for id in curr_id]

        for f in concurrent.futures.as_completed(results):
            anime_list.append(f.result()) 

    end = time.perf_counter()

    # print(anime_list[0][0],get_links(anime_list[0][0]))

    print(f'finished in {round(end-start,2)} second(s)')

if __name__ == "__main__":
    main()