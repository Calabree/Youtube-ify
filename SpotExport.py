import configparser
import os
import spotipy
import spotipy.oauth2 as oauth2

class SpotExport:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')
        client_id = config.get('SPOTIFY', 'CLIENT_ID')
        client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
        #REDIRECT_URI = config.get('SPOTIFY', 'REDIRECT_URI')

        auth = oauth2.SpotifyClientCredentials(
            client_id=client_id,
            client_secret=client_secret
        )
        self.token = auth.get_access_token()

    def writeToFile(self, i):
        #TODO: create file name based on playlist export name.
        script_dir = os.path.dirname(__file__) 
        rel_path = "ExportedPlaylists/songs.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        f=open(abs_file_path,"a")
        f.write(str(self.list[i])+"\n")

    def songGrab(self,list):
        self.list = list
        counter = 1
        spotifyObject = spotipy.Spotify(auth=self.token)
        uri = input('Please provide the URI of the playlist you wish to export: ')
        #offset allows for paging through playlists with mroe than 100 songs
        offset = spotifyObject.playlist_items(uri,fields='total')
        roundedOffset = int(offset['total']) +100 ##change to round up to nearest whole 100. Ex 212 -> 300
        loopCount = (roundedOffset/100)
        print (loopCount)
        
        for i in range(int(loopCount)):
            playlists = spotifyObject.playlist_tracks(uri,fields='items', market='us', limit = 100, offset=i*100)
            for i, item in enumerate(playlists['items']):
                if item['track'] is not None:
                    list.append({
                        'artist': ','.join([artist['name'] for artist in item['track']['artists']]),
                        'name': item['track']['name'],
                        'album': item['track']['album']['name'],
                        'duration': item['track']['duration_ms']/1000
                        })
                    self.writeToFile(i)
                print(counter,self.list)
                counter+=1  