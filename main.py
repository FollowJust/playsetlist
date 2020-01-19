import parser
import vlc
import os

def play_urls(urls):
    os.system(f"vlc -q {' '.join(songs_links.values())}")
    print('Goodbye!')
    return None
print('Hello! Welcome to setlist player. Enter the link to the setlist on setlist.fm, please.')
link = input()
artist, songs = parser.get_info(link)
print(f'Ok, we are listening to {artist}. The setlist is:\n')
for i in songs:
    print(i)
print('\nPlease, wait a little bit...')
songs_links = parser.songs_links(artist, songs)
print('Have a nice listen!')
play_urls(songs_links.values)
