from functions.misc import split_artist_track
from functions.network import network
from functions.config import delay, webhook
from discord_webhook import DiscordWebhook
import time, datetime, json, random

SCROBBLES = 1
START_TIME = time.time()

notification = DiscordWebhook(url=webhook, content=f'Started scrobbling @ <t:{str(int(START_TIME))}:T>')
notification.execute()

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
                time.sleep(delay + random.randrange(1, 3))
        elif playlist_name in playlists:
            songs = playlists[playlist_name]
            for song in songs:
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")

                if debug:
                    print(f'Scrobbling {song} | {str(SCROBBLES)} scrobbles this session ({current_time})')
                if webhook != False:
                    if SCROBBLES == 1 and webhook != False:
                        notification.content = f'1 scrobble this session\nLast scrobbled @ <t:{str(int(time.time()))}:T>'
                        notification.edit()
                    elif SCROBBLES > 1 and webhook != False:
                        notification.content = f'{str(SCROBBLES)} scrobbles this session\nLast scrobbled @ <t:{str(int(time.time()))}:T>\nLast song: {song}'
                        notification.edit()
                scrobble_(str(song))
                time.sleep(delay + random.randrange(1, 3))
        else:
            print("Playlist '{}' not found.".format(playlist_name))