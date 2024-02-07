import pylast
from functions.config import *

network = pylast.LastFMNetwork(
    api_key=key,
    api_secret=secret,
    username=username,
    password_hash=pylast.md5(password),
)