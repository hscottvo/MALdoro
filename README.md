# MALdoro

## 
The Pomodoro technique is a time management method developed in the 1980s by Francesco Cirillo. The main premise of the technique is to alternate between working and resting, traditionally in blocks of 25 minutes each. The first thing that comes to mind for many computer science students (at least in the MALdoro team) is watching anime. 

## The Problem

The thing is, we're not very good at time management, which is a key concept in the Pomodoro technique. So, we decided to automate it, along with anime recommendations. MALdoro takes a downloaded anime list that users can compile using [MyAnimeList](https://myanimelist.net/), and automatically stores the tags and genres for each anime on the list. The user can then select their desired series and click on the link to their favorite streaming site and watch an episode while the timer ticks down. 

## Optimizing... Anime?

The finest anime connoisseurs know that it's hard to work on a difficult homework assignment right after watching a tear-jerker like <em>Clannad</em> or a psychological thriller like <em>Steins;Gate</em>. We decided to calculate the "intensity levels" of each anime automatically, and sort them depending on the intensity of the user's working sessions. Strenuous work pairs well with lighter shows like <em>K-on!</em> or <em>Yuru Camp</em>, and lighter work pairs with more intense shows like those listed above. 

## How does it work?

Our program first reads into an xml file that is downloaded from the user's MyAnimeList anime list, and is parsed for the relevant information to be stored in a Pandas dataframe. We then interface with an open-source [MAL API](https://github.com/darenliang/mal-api) that acquires additional information about each anime in the list such as genres. The resultant information is displayed in a [TKinter](https://docs.python.org/3/library/tkinter.html) window along with anime genres and intensity level to select, and a timer indicating the time remaining in the current work-break session. Anime are then sorted based on the user's preferences. Upon clicking the desired anime, a set of anime streaming sites is shown using the [JustWatch API](https://pypi.org/project/JustWatch/) for the user to watch in their default browser during their break session. 