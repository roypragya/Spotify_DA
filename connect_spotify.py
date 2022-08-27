import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid ="5cf7fd8a74434b4aa2243cd27dc0e490" 
secret = "033870832e60454b8c23e5e7a56b4280"

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
