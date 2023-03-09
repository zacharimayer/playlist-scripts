import csv
import os
import spotipy
import spotipy.util as util

# Set up Spotify API credentials
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIPY_REDIRECT_URI")
username = input("Enter your Spotify username: ")
scope = "playlist-modify-public"

# Authenticate with Spotify API
token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
sp = spotipy.Spotify(auth=token)

# Set playlist name and add songs from CSV file
playlist_name = "My Playlist"
with open("songs.csv") as csvfile:
    reader = csv.reader(csvfile)
    song_ids = []
    for row in reader:
        song_title, artist_name = row
        results = sp.search(q=f"track:{song_title} artist:{artist_name}", type="track")
        if results["tracks"]["items"]:
            # Add first result to playlist
            song_id = results["tracks"]["items"][0]["uri"]
            song_ids.append(song_id)

# Create new playlist with the specified name and song IDs
playlist = sp.user_playlist_create(username, playlist_name)
sp.user_playlist_add_tracks(username, playlist["id"], song_ids)

print(f"Playlist '{playlist_name}' created with {len(song_ids)} songs!")
