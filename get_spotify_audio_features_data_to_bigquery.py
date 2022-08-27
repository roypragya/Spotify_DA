import pandas as pd
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 

# connect to spotify
cid ="5cf7fd8a74434b4aa2243cd27dc0e490" 
secret = "033870832e60454b8c23e5e7a56b4280" 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# retrive data from spotidy web API
artist_name = []
track_name = []
popularity = []
track_id = []
for i in range(0,1000,50): 
    track_results = sp.search(q='year:2018', type='track', limit=50,offset=i) 
    for i, t in enumerate(track_results['tracks']['items']):
           artist_name.append(t['artists'][0]['name']) 
           track_name.append(t['name']) 
           track_id.append(t['id']) 
           popularity.append(t['popularity'])

# creating data set
df_tracks = pd.DataFrame({'popularity':popularity,'artist_name':artist_name,'track_name':track_name,'track_id':track_id})
# df_tracks = df_tracks.sort_values('popularity', ascending=False)
print(df_tracks.shape)
df_tracks.head()

# checking for duplicates
grouped = df_tracks.groupby(['artist_name','track_name'], as_index=True).size()
grouped[grouped > 1].count()

# dropping duplicate tuples
df_tracks.drop_duplicates(subset=['artist_name','track_name'], inplace=True)

# checking for duplicatees again
grouped_after_dropping = df_tracks.groupby(['artist_name','track_name'], as_index=True).size()
grouped_after_dropping[grouped_after_dropping > 1].count()

df_tracks.shape

# loading audio features
rows = []
batchsize = 100
None_counter = 0

for i in range(0,len(df_tracks['track_id']),batchsize):
    batch = df_tracks['track_id'][i:i+batchsize]
    feature_results = sp.audio_features(batch)
    for i, t in enumerate(feature_results):
        if t == None:
            None_counter = None_counter + 1
        else:
            rows.append(t)
            
print('Number of tracks where no audio features were available:',None_counter)

# creating dataframe
df_audio_features = pd.DataFrame.from_dict(rows,orient='columns')
print("Shape of the dataset:", df_audio_features.shape)
df_audio_features.head()

df_audio_features.info()

# dropping some columns
# renaming "id" column to "track_id"
columns_to_drop = ['analysis_url','track_href','type','uri']
df_audio_features.drop(columns_to_drop, axis=1,inplace=True)

df_audio_features.rename(columns={'id': 'track_id'}, inplace=True)

df_audio_features.shape

# merging the datasets
df = pd.merge(df_tracks,df_audio_features,on='track_id',how='inner')
print("Shape of the dataset:", df_audio_features.shape)
df.head()

# checking for duplicates
df[df.duplicated(subset=['artist_name','track_name'],keep=False)]

# csv file
df.to_csv('SpotifyAudioFeatures08082018.csv')