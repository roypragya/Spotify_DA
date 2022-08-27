import pandas as pd
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 

# connect to spotify
cid ="5cf7fd8a74434b4aa2243cd27dc0e490" 
secret = "033870832e60454b8c23e5e7a56b4280" 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# retrive data from spotidy web API
followers = []
genres = []
artist_name = []
artist_id = []
popularity = []
for i in range(0,1000,50): 
    artist_results = sp.search(q='year:2022', type='artist', limit=50,offset=i) 
    for i, t in enumerate(artist_results['artists']['items']):
           artist_name.append(t['name']) 
           followers.append(t['followers']) 
           artist_id.append(t['id']) 
           popularity.append(t['popularity'])
           genres.append(t['genres'])

# creating data set
df_artists = pd.DataFrame({'popularity':popularity,'artist_name':artist_name,'genres':genres,'artist_id':artist_id,'followers':followers})

print(df_artists.shape)
df_artists.head()

# checking for duplicates
grouped = df_artists.groupby(['artist_name'], as_index=True).size()
grouped[grouped > 1].count()

# dropping duplicate tuples
df_artists.drop_duplicates(subset=['artist_name'], inplace=True)

# checking for duplicatees again
grouped = df_artists.groupby(['artist_name'], as_index=True).size()
grouped[grouped > 1].count()

df_artists.shape

# csv file
df_artists.to_csv('SpotifyArtists2022.csv')