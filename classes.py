class Genres:
    def __init__(self):
        self.stress_genres = ["Dementia","Horror", "Mystery", "Psychological", "Thriller", "Historical", "Military", "Martial Arts", "Samurai", "Drama", "Police", "Seinen", "Shounen", "Space", "Sci-Fi", "Mecha", "Sports", "Supernatural"]
        self.calm_genres = ["Action","Adventure","Comedy", "Ecchi", "Fantasy", "Game", "Harem", "Kids", "Parody", "Slice of Life", "Romance", "Music", "School", "Shoujo", "Shouji Ai", "Shounen Ai", "Yaoi", "Yuri"]
        self.neutral_genres = ["Magic", "Super Power", "Cars", "Demons", "Josei", "Vampire"]

class Anime_Obj:
    def __init__(self, title, stress_counter, calm_counter, neutral_counter, genres):
        self.title = title
        self.stress_counter = stress_counter
        self.calm_counter = calm_counter
        self.neutral_counter = neutral_counter
        self.genres = genres
    def genre_exist(self,genre):
        for i in genre:
            if i in self.genres:
                return True
        return False
