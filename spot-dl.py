import os
import subprocess

def download_track(track_url, download_dir='spotify_downloads'):
    try:
        # Create download directory if it does not exist
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        # Construct download command
        command = ['spotdl', 'download', track_url, '--output', os.path.join(download_dir)]
        subprocess.run(command, check=True)

        print(f"Download completed for: {track_url}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading {track_url}: {e}")

def download_playlist(playlist_url, download_dir='spotify_downloads'):
    try:
        # Create download directory if it does not exist
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        # Construct playlist download command
        command = ['spotdl', 'download', playlist_url, '--output', os.path.join(download_dir)]
        subprocess.run(command, check=True)

        print(f"Playlist download completed: {playlist_url}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading playlist {playlist_url}: {e}")

def download_tracks_from_file(file_path, download_dir='spotify_downloads'):
    try:
        # Create download directory if it does not exist
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        with open(file_path, 'r') as file:
            tracks = file.readlines()

        for track_url in tracks:
            track_url = track_url.strip()
            print(f"Downloading: {track_url}")
            download_track(track_url, download_dir)
    except Exception as e:
        print(f"Error downloading tracks from file: {e}")

if __name__ == "__main__":
    while True:
        mode = input("Do you want to download a Spotify playlist (1) or individual tracks (2)? ")

        if mode == '1':
            playlist_url = input("Enter the Spotify playlist URL: ")
            download_playlist(playlist_url)
        elif mode == '2':
            method = input("Do you want to use a text file (1) or enter tracks one by one (2)? ")

            if method == '1':
                file_path = input("Enter the path to the text file with track URLs: ")
                download_tracks_from_file(file_path)
            elif method == '2':
                while True:
                    track_url = input("Enter the track URL (or 'done' to finish): ")
                    if track_url.lower() == 'done':
                        break
                    download_track(track_url)
            else:
                print("Invalid method. Please choose 1 or 2.")
        else:
            print("Invalid mode. Please choose 1 or 2.")

        another = input("Do you want to download something else? (yes/no): ")
        if another.lower() != 'yes':
            break
