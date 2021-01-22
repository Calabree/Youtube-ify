import SpotExport as se
import YTMHandle as ytm

print('''
--------------------------------------------
-                 Welcome!                 -
-      This is a script to export your     -
-       spotify songs from a specified     -
-          and write them to a file.       -
--------------------------------------------
''')

songs=[]

se.SpotExport().songGrab(songs)
ytm.YTMusicHandle().FindSong(songs)