from anime_comfy_levels import *
from justwatch_query import get_links
from classes import *
from mal import *
from converter import *
from video import *
import csv
import concurrent.futures
import threading
import multiprocessing
import time
import UI

genres_list = Genres()
anime_id_new = []
anime_id_completed = []



# self.title = title
# self.stress_counter = stress_counter
# self.calm_counter = calm_counter
# self.neutral_counter = neutral_counter
# self.genres = genres

def save_list(anime_list):
    titles = []
    stress = []
    calm = []
    neutral = []
    genres = []
    ratio = []
    for anime in anime_list: 
        titles.append(anime.title)
        stress.append(anime.stress_counter)
        calm.append(anime.calm_counter)
        neutral.append(anime.neutral_counter)
        genres.append(anime.genres)
        ratio.append(anime.ratio())

    title_series = pd.Series(titles)
    stress_series = pd.Series(stress)
    calm_series = pd.Series(calm)
    neutral_series = pd.Series(neutral)
    genres_series = pd.Series(genres)
    ratio_series = pd.Series(ratio)

    frame = {"Title":  title_series, "Genres": genres_series, "Stress Level": stress_series, "Calm Level": calm_series, "Neutral Level": neutral_series, "Ratio": ratio_series}

    result = pd.DataFrame(frame)

    result.to_csv("saved.csv")
    return result



def main():
    anime_list = []
    xmlinput = input("enter xml file name: ") # button input
    parse_xml(xmlinput)

    FILENAME = "output.csv"
    with open(FILENAME, newline = "") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[4] == "Plan to Watch":
                anime_id_new.append(row[5])
            elif row[4] == "Completed":
                anime_id_completed.append(row[5])

    choice = input("new or completed? (n/c): ") # button input
    curr_id = []
    if choice.lower() == "n":
        curr_id = anime_id_new
    else:
        curr_id = anime_id_completed
    print("If Create List does not work, check MAL Site")
    choice = input("load anime or create new list? (l/c): ")
    if choice.lower() == "c":
        # mid = int(len(curr_id) / 2)
        # left = int(mid/2)
        # right = int(mid + left)

        # process1 = curr_id[:left]
        # process2 = curr_id[left:mid]
        # process3 = curr_id[mid:right]
        # process4 = curr_id[right:]
        
        # Alpha Future Processing
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.map(anime_levels,curr_id)
            for result in results:
                anime_list.append(result)
        print("\nProcess complete")
        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     results = executor.map(anime_levels,process2)
        #     for result in results:
        #         anime_list.append(result)
        # print("\nProcess 2 complete")
        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     results = executor.map(anime_levels,process3)
        #     for result in results:
        #         anime_list.append(result)
        # print("\nProcess 3 complete")
        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     results = executor.map(anime_levels,process4)
        #     for result in results:
        #         anime_list.append(result)
        # print("\nProcess 4 complete")
    else:
        anime_list = load_file("saved.csv")

    # print(anime_list[0].title, get_links(anime_list[0].title))
    
    main_genre_list = ["Dementia","Horror", "Mystery", "Psychological", "Thriller", "Historical", "Military", "Martial Arts", "Samurai", "Drama", "Police", "Seinen", "Shounen", "Space", "Sci-Fi", "Mecha", "Sports", "Supernatural","Action","Adventure","Comedy", "Ecchi", "Fantasy", "Game", "Harem", "Kids", "Parody", "Slice of Life", "Romance", "Music", "School", "Shoujo", "Shouji Ai", "Shounen Ai", "Yaoi", "Yuri","Magic", "Super Power", "Cars", "Demons", "Josei", "Vampire"]
    for i in main_genre_list:
        print(i,end=" - ")

    specified_genres = []

    while True:
        user_genre = input("\nEnter a Genre (type done when done): ")
        if user_genre in main_genre_list:
            specified_genres.append(user_genre)
        elif user_genre.lower() == "done":
            break
        else:
            print("Not a genre")

    while True:
        user_level = input("How intense is your work (1-10)?")
        if user_level.isdigit():
            user_level = int(user_level)
            if (user_level > 0 and user_level < 11):
                break
        print("Incorrect input") 
    
    genre_specific = []
    genre_specific = genre_finder(anime_list,specified_genres)

    intensity_level = 10 - user_level
    lower_bound = intensity_level - 1
    upper_bound = intensity_level + 1
    final_list = []
    for i in genre_specific:
        show_level = i.ratio()
        if (show_level >= lower_bound and show_level <= upper_bound):
            final_list.append(i)

    if len(final_list) == 0:
        print("No Show Selected - Try other parameters")
    else:
        for show in final_list:
            print(show.title,show.ratio())
    
    # print(genre_specific[0].title, get_links(genre_specific[0].title))
    # save_list(anime_list)


if __name__ == "__main__":
    main()
    