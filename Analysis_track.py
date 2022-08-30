import pandas as pd
import seaborn
import matplotlib.pyplot as plt
tracks_analysis = pd.read_csv("SpotifyAudioFeatures2022.csv")
tracks_analysis.head()

# checking for null values
pd.isnull(tracks_analysis).sum()

# most popular tracks
sorted_df=tracks_analysis.sort_values('popularity', ascending=False).head()
sorted_df

tracks_analysis.describe()

#  set index to track names
tracks_analysis.set_index("track_name", inplace=True)
tracks_analysis.head()

#  dropping the serial no. column of csv
tracks_analysis.drop(['Unnamed: 0'], axis=1, inplace=True)
tracks_analysis.head()

# artist name at the 32nd position
tracks_analysis[["artist_name"]].iloc[32]

# changing track duration in miliseconds to minutes
tracks_analysis["duration_min"]=tracks_analysis["duration_ms"].apply(lambda x:round((x/1000)/60))
tracks_analysis.drop("duration_ms", inplace=True, axis=1)
tracks_analysis.duration_min.head()

# finding the correlation of the dataframe
tracks_analysis.corr()

#  creating a heatmap of pearson correlation of the dataframe 
plt.figure(figsize=(14,14))
seaborn.heatmap(tracks_analysis.corr(), annot=True, cmap="coolwarm").set_title("Pearson Correlation Heatmap using Seaborn")

# linear regression scatter plot of Loudness vs Energy
plt.figure(figsize=(14,14))
seaborn.regplot(data=tracks_analysis, y = "loudness", x="energy", color = "c").set_title("Loudness vs Energy Linear Regression")

# linear regression scatter plot of Popularity vs Danceability
plt.figure(figsize=(14,14))
seaborn.regplot(data=tracks_analysis, y = "popularity", x="danceability", color = "c").set_title("Popularity vs Danceability Linear Regression")

# linear regression scatter plot of Instrumentalness vs Acousticness
plt.figure(figsize=(14,14))
seaborn.regplot(data=tracks_analysis, y = "instrumentalness", x="acousticness", color = "c").set_title("Instrumentalness vs Acousticness Linear Regression")