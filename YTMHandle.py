from ytmusicapi import YTMusic
import json
from json.decoder import JSONDecodeError

class YTMusicHandle:

    def __init__(self):
        self.ytm=YTMusic('headers_auth.json') #passes the cookie from headers_auth,json
    
    def MakePlaylist(self):
        self.ytm.create_playlist("is this private?", "this is a test ", "PUBLIC")
    
    def timeConvert(self,seconds):
        self.minutes = seconds //60
        seconds = seconds %(24*3600)
        seconds %= 60
        return "%02d:%02d" % (self.minutes, seconds) 
        
    def FindSong(self, list):
        f = open('test.json','w')
        for i,item in enumerate(list):
            second = item['duration']
            time = self.timeConvert(second)
            print(time)
            #query = item['artist']+" "+item['name']
            #song = self.ytm.search(query, "songs", 1, False)
            #f.write(json.dumps(song, sort_keys=True, indent=4))