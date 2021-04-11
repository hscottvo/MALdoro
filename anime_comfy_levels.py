from mal import *
from classes import *
import csv
import concurrent.futures
import threading
import multiprocessing
import time

genres_list = Genres()

def anime_levels(id, genres = genres_list):
    anime = Anime(id)
    show_genres = anime.genres

    stress_counter = 0
    calm_counter = 0
    neutral_counter = 0

    for genre in show_genres:
        if genre in genres.stress_genres:
            stress_counter +=1
        elif genre in genres.calm_genres:
            calm_counter += 1
        elif genre in genres.neutral_genres:
            neutral_counter += 1

    obj = Anime_Obj(anime.title,stress_counter,calm_counter,neutral_counter,show_genres)
    print("#",end="")
    return obj

def main():
    choice = input("new or completed? (n/c): ")
    curr_id = []
    if choice.lower() == "n":
        curr_id = anime_id_new
    else:
        curr_id = anime_id_completed


    # Alpha Future Processing
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(anime_levels,id) for id in curr_id]

        for f in concurrent.futures.as_completed(results):
            anime_list.append(f.result()) 

def genre_finder(anime_list,specified_genres):
    genre_specific = []

    for show in anime_list:
        if(show.genre_exist(specified_genres)):
            genre_specific.append(show)
    
    return genre_specific
    
    # # Chad processing
    # processes = []
    # for id in anime_id:
    #     p = multiprocessing.Process(target=anime_levels,args=[id])
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()

    # # Beta Threading
    # threads = []

    # for id in anime_id:
    #     t = threading.Thread(target=anime_levels, args=[id])
    #     t.start()
    #     threads.append(t)

    # for thread in threads:
    #     thread.join()

    # # Regular shitty way
    # for id in curr_id:
    #     anime_list.append(anime_levels(id))

    end = time.perf_counter()

    for i in anime_list:
        for j in i:
            print(j,end=" ")
        print()

    print(f'finished in {round(end-start,2)} second(s)')
    

if __name__ == '__main__':
    main()