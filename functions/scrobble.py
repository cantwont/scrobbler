from functions.misc import split_artist_track
from functions.network import network
from functions.config import delay
import time, datetime, json

SCROBBLES = 1

def scrobble_(track):
    global SCROBBLES
    (artist, track) = split_artist_track(track)

    network.scrobble(artist=artist, title=track, timestamp=int(time.mktime(datetime.datetime.now().timetuple())))
    SCROBBLES += 1

def scrobble(*playlist_names, debug=False):
    with open('configuration/playlists.json', 'r') as playlists_file:
        playlists = json.load(playlists_file)
    
    for playlist_name in playlist_names:
        if isinstance(playlist_name, list):
            for p_name in playlist_name:
                scrobble(p_name, debug=debug)
                time.sleep(delay)
        elif playlist_name in playlists:
            songs = playlists[playlist_name]
            for song in songs:
                if debug:
                    print(f'Scrobbling {song} | {str(SCROBBLES)} scrobbles this session')
                scrobble_(str(song))
                time.sleep(delay)
        else:
            print("Playlist '{}' not found.".format(playlist_name))