
# Scrobbler

## About
Ever wanted to have hundreds of thousands of scrobbles on Last.fm? Well here's a tool for that. No, this does NOT play the full song, you input a delay in ``configuration/config.json`` and every time it goes past that, as long as there is a song inside a playlist *(see below)* it will automatically register.

## Features
- Automatically register a scrobble for almost any song
- Discord Webhook support
- Custom playlists in a .json (will loop over to next playlist if you choose to in ``main.py``)
- Customizable delay (30 recommended)
- More coming soon

## Instructions
First you need to go to [this website](https://www.last.fm/api/account/create) and make an account. Input literally anything for the text fields, click create and it will give you everything you need in the configuration. Your ``config.json`` should look like this: 

```json
{
    "key": "LASTFM_API_KEY",
    "secret": "LASTFM_API_SHARED_SECRET",

    "username": "LASTFM_USERNAME",
    "password": "LASTFM_PASSWORD",

    "delay": 30,

    "debug": false,

    "webhook": "https://discord.com/api/webhooks/"
}
```

Once you have this part of the process completed, you're able to go and make a playlist. The playlists file is stored in ``configuration/playlists.json``. A basic example of this would be this:

```json
{
	"playlist1": [
		"Lil Uzi Vert - Paradise",
		"Deftones - Xerces"
	],
	"playlist2": [
		"Playboi Carti - Kelly K",
		"Tenkay - Banned"
	]
}
```

### Before running make sure you have at least [Python 3.11](https://www.python.org/downloads/release/python-3110/) (this is the version I am running locally) and you install the required packages below:

```
pip install pylast
pip install datetime
```

## Notes:
You do NOT need to have several playlists or several songs, just as long as it follows that format it should be fine. Make sure the artist name is going FIRST and song name SECOND. You also do not need to use debug mode or have a webhook enabled. To disable webhook just set the value to "false" without parantheses. Please open an issue if an error occurs or feel free to contact me on Discord @me_and_the_birds

## Showcase:
![Showcase](https://cdn.discordapp.com/attachments/1204196242020900936/1204624781551472690/image.png?ex=65d56940&is=65c2f440&hm=5fd9d98e20480a3fa18cb9719eec86d3a5ca2f59dc32e1ff67e576f6de1dcb77&)
![Showcase2](https://cdn.discordapp.com/attachments/1204970159102500864/1205038666980790312/image.png?ex=65d6eab6&is=65c475b6&hm=cae99105e31e89278fd43aef769826a2758acc77f2ff8cf7f5c8e2cf95f028d3&)
