import requests
from bs4 import BeautifulSoup


def get_info(link_to_setlist):
    html_data = requests.get(link_to_setlist)
    setlist_soup = BeautifulSoup(html_data.text, 'html.parser')
    artist_name = setlist_soup.find(property='qc:artist')['content']
    all_songs = setlist_soup.find_all(class_='songLabel')
    song_names = list(map(lambda songLabel: songLabel.string, all_songs))
    return artist_name, song_names


def get_link(artist, song):
    artist, song = correct_search(artist, song)
    search = f'https://www.youtube.com/results?search_query={artist}+{song}'
    search_results = requests.get(search)
    search_soup = BeautifulSoup(search_results.text, 'html.parser')
    return search_soup.select('.yt-uix-tile-link')[0]['href']


def songs_links(artist, songs):
    songs_links = {}
    for song in songs:
        songs_links[song] = 'https://www.youtube.com' + get_link(artist, song)
    return songs_links


def correct_search(artist, song):
    return artist.replace(' ', '+'), song.replace(' ', '+')
