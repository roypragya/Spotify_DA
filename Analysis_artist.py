import seaborn
import pandas as pd
import matplotlib.pyplot as plt
artists_analysis = pd.read_csv("SpotifyArtists2022.csv")
artists_analysis.head()

# checking for null values
pd.isnull(artists_analysis).sum()

# most popular artists
sorted_df=artists_analysis.sort_values('popularity', ascending=False).head()
sorted_df

#  set index to artist names
artists_analysis.set_index("artist_name", inplace=True)
artists_analysis.head()

#  dropping the serial no. column of csv
artists_analysis.drop(['Unnamed: 0'], axis=1, inplace=True)
artists_analysis.head()

artists_analysis.describe()

# finding the correlation of the dataframe
artists_analysis.corr()

#  creating a heatmap of pearson correlation of the dataframe 
plt.figure(figsize=(2,2))
seaborn.heatmap(artists_analysis.corr(), annot=True, cmap="coolwarm").set_title("Pearson Correlation Heatmap using Seaborn")

# linear regression scatter plot of Popularity vs Followers
plt.figure(figsize=(14,14))
seaborn.regplot(data=artists_analysis, y = "popularity", x="followers", color = "c").set_title("Popularity vs Followers Linear Regression")