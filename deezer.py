import csv
import deezpy
from getpass import getpass

# Get Deezer credentials from user input
app_id = input("Enter your Deezer application ID: ")
app_secret = getpass("Enter your Deezer application secret: ")
access_token = getpass("Enter your Deezer access token: ")

# Create Deezpy client with app ID, app secret, and access token
client = deezpy.Client(app_id, app_secret, access_token)

# Set playlist name and add songs from CSV file
playlist_name = "My Playlist"
with open("songs.csv") as csvfile:
    reader = csv.reader(csvfile)
    song_ids = []
    for row in reader:
        song_title, artist_name = row
        search_results = client.search(song_title, artist_name, type="track")
        if search_results:
            # Add first result to playlist
            song_id = search_results[0]["id"]
            song_ids.append(song_id)

# Create new playlist with the specified name and song IDs
playlist = client.user.create_playlist(playlist_name)
playlist.add_tracks(song_ids)

print(f"Playlist '{playlist_name}' created with {len(song_ids)} songs!")
