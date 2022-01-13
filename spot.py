from spotipy import *
import spotipy
import config

client_ID = config.ID
client_SECRET = config.secret
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_ID, client_secret=client_SECRET))
genres = spotify.recommendation_genre_seeds()['genres']

def getGenreTracks(self, genre):
    result = spotify.recommendations(seed_genres=[genre], limit=50, country='US')
    result = result['tracks']
    l1=[]
    for i in result:
        s = i.get('name') + " - " + i['artists'][0].get('name')
        l1.append(s)

def getSearchTracks(self, search):
    result=spotify.search(search, limit=10)['tracks']['items']
    l1=[]
    for i in result:
        test = i.get('name')
        l1.append(test)
    return l1


    



