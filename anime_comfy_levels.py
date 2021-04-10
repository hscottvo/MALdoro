from mal import Anime

stress_genres = ["Dementia","Horror", "Mystery", "Psychological", "Thriller", "Historical", "Military", "Martial Arts", "Samurai", "Drama", "Police", "Seinen", "Shounen", "Space", "Sci-Fi", "Mecha", "Sports"]
calm_genres = ["Action","Adventure","Comedy", "Ecchi", "Fantasy", "Game", "Harem", "Kids", "Parody", "Slice of Life", "Romance", "Music", "School", "Shoujo", "Shouji Ai", "Shounen Ai", "Yaoi", "Yuri"]
neutral_genres = ["Magic", "Super Power", "Cars", "Demons", "Josei", "Vampire"]

anime = Anime(2251)
print(anime.title)
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
    print(genre)

print("Stress:", stress_counter)
print("Calm:", calm_counter)
print("Neutral:", neutral_counter)

