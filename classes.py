class Genres:
    def __init__(self):
        self.stress_genres = ["Dementia","Horror", "Mystery", "Psychological", "Thriller", "Historical", "Military", "Martial Arts", "Samurai", "Drama", "Police", "Seinen", "Shounen", "Space", "Sci-Fi", "Mecha", "Sports", "Supernatural"]
        self.calm_genres = ["Action","Adventure","Comedy", "Ecchi", "Fantasy", "Game", "Harem", "Kids", "Parody", "Slice of Life", "Romance", "Music", "School", "Shoujo", "Shouji Ai", "Shounen Ai", "Yaoi", "Yuri"]
        self.neutral_genres = ["Magic", "Super Power", "Cars", "Demons", "Josei", "Vampire"]

class Anime:
    def __init__(self, title, links, genres, comfy, stressful, neutral):
        self.title = title
        self.links = links
        self.genres = genres
        self.comfy = comfy
        self.stressful = stressful
        self.neutral = neutral