import csv
from getpass import getpass
from tidalapi import TidalAPI

# Get Tidal credentials from user input
username = input("Enter your Tidal username/email: ")
password = getpass("Enter your Tidal password: ")

# Create TidalAPI object with user credentials
api = TidalAPI(username, password)

# Set playlist name and add songs from CSV file
playlist_name = "My Playlist"
with open("songs.csv") as csvfile:
    reader = csv.reader(csvfile)
    song_ids = []
    for row in reader:
        song_title, artist_name = row
        search_results = api.search(song_title, artist_name)
        if search_results:
            # Add first result to playlist
            song_id = search_results[0]["id"]
            song_ids.append(song_id)

# Create new playlist with the specified name and song IDs
playlist_id = api.create_playlist(playlist_name)
api.add_tracks_to_playlist(playlist_id, song_ids)

print(f"Playlist '{playlist_name}' created with {len(song_ids)} songs!")
