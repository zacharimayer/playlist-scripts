import csv
import getpass
from ytmusicapi import YTMusic

# Authenticate with YouTube Music
email = input("Enter your YouTube Music email address: ")
password = getpass.getpass("Enter your YouTube Music password: ")
ytmusic = YTMusic()
ytmusic.login(email, password)

# Set playlist name and add songs from CSV file
playlist_name = "My Playlist"
with open("songs.csv") as csvfile:
    reader = csv.reader(csvfile)
    song_ids = []
    for row in reader:
        song_title, artist_name = row
        search_results = ytmusic.search(query=f"{song_title} {artist_name}", filter="songs")
        if search_results:
            # Add first result to playlist
            song_id = search_results[0]["videoId"]
            song_ids.append(song_id)

# Create new playlist with the specified name and song IDs
playlist_id = ytmusic.create_playlist(playlist_name)
ytmusic.add_playlist_items(playlist_id, song_ids)

print(f"Playlist '{playlist_name}' created with {len(song_ids)} songs!")
