import parser
import vlc
from time import sleep

def play_url(url):
    #media = vlc.MediaPlayer("MEDIA FILE HERE")
    i = vlc.Instance()
    media_player = i.media_player_new()
    media_player.set_mrl('https://www.youtube.com/watch?v=tVwl0iBhfIU')
    media_player.play()
    while True:
        pass
    '''
    sleep(10)
    while player.is_playing():
        sleep(1)
    '''
    return None

'''
link = input()
artist, songs = parser.get_info(link)
print(artist)
print(songs)

songs_links = parser.songs_links(artist, songs)
print(songs_links['Ludens'])
'''
playthis = '/watch?v=B9wvTuDC-H0'
play_url(playthis)
