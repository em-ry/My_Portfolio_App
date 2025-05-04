import pandas as pd


df = pd.read_csv("data.csv", sep=";")
df["url"] = df["url"].replace("https://pythonhow.com", "https://github.com/em-ry")

df.to_csv("new_data.csv")
