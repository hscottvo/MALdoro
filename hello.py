import pandas as pd

filename = "genre_list.csv"

df = pd.read_csv(filename,index_col=0)

print(df["Genres"])