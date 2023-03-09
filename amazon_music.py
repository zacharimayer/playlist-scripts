import csv
import getpass
from amazon_music.amazon_music import AmazonMusic
from amazon_music.amazon_music import Device

# Get Amazon Music credentials from user input
email = input("Enter your Amazon Music email address: ")
password = getpass.getpass("Enter your Amazon Music password: ")

# Create AmazonMusic object with user credentials
am = AmazonMusic(email=email, password=password, device=Device.WEB_PLAYER)

# Set playlist name and add songs from CSV file
playlist_name = "My Playlist"
with open("songs.csv") as csvfile:
    reader = csv.reader(csvfile)
    song_ids = []
    for row in reader:
        song_title, artist_name = row
        search_results = am.search_for_songs(song_title, artist_name)
        if search_results:
            # Add first result to playlist
            song_id = search_results[0]["id"]
            song_ids.append(song_id)

# Create new playlist with the specified name and song IDs
playlist_id = am.create_playlist(playlist_name)
am.add_songs_to_playlist(playlist_id, song_ids)

print(f"Playlist '{playlist_name}' created with {len(song_ids)} songs!")
