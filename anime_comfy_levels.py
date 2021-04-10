from mal import Anime
import concurrent.futures
import threading
import multiprocessing
import time

start = time.perf_counter()

stress_genres = ["Dementia","Horror", "Mystery", "Psychological", "Thriller", "Historical", "Military", "Martial Arts", "Samurai", "Drama", "Police", "Seinen", "Shounen", "Space", "Sci-Fi", "Mecha", "Sports"]
calm_genres = ["Action","Adventure","Comedy", "Ecchi", "Fantasy", "Game", "Harem", "Kids", "Parody", "Slice of Life", "Romance", "Music", "School", "Shoujo", "Shouji Ai", "Shounen Ai", "Yaoi", "Yuri"]
neutral_genres = ["Magic", "Super Power", "Cars", "Demons", "Josei", "Vampire"]

anime_id = [2251,30,20,28851,9253,14813,2001,37510,2167,4181]
anime_list = []

def anime_levels(id):
    anime = Anime(id)
    show_genres = anime.genres


    stress_counter = 0
    calm_counter = 0
    neutral_counter = 0

    for genre in show_genres:
        if genre in stress_genres:
            stress_counter +=1
        elif genre in calm_genres:
            calm_counter += 1
        elif genre in neutral_genres:
            neutral_counter += 1

    built_level = [anime.title,stress_counter,calm_counter,neutral_counter]
    return built_level

def main():
    # Alpha Future Processing
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(anime_levels,id) for id in anime_id]

        for f in concurrent.futures.as_completed(results):
            anime_list.append(f.result()) 


    
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
    # for id in anime_id:
    #     anime_levels(id)

    end = time.perf_counter()

    for i in anime_list:
        for j in i:
            print(j,end=" ")
        print()

    print(f'finished in {round(end-start,2)} second(s)')
    

if __name__ == '__main__':
    main()