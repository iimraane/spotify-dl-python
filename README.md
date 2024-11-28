# Spotify Downloader

This project allows you to download Spotify playlists or individual tracks using the `spotdl` library. The downloads are sourced from YouTube to avoid any issues related to downloading music directly from Spotify.

## Requirements

- Python 3.x
- `spotdl` library
- FFmpeg

## Installation

1. Install `spotdl`:
    ```bash
    pip install spotdl
    ```

2. Install FFmpeg:
    ```bash
    spotdl --download-ffmpeg
    ```

## Usage

1. Run the script:
    ```bash
    python spot-dl.py
    ```

2. Choose your mode:
    - **Download a Spotify playlist**
    - **Download individual tracks**: Choose between using a text file or entering the track URLs one by one.

### Example Usage

#### Download Individual Track

1. Run the script:
    ```bash
    python spot-dl.py
    ```
2. Choose the mode:
    ```plaintext
    Do you want to download a Spotify playlist (1) or individual tracks (2)?
    ```
    Enter `2`.
3. Choose the method:
    ```plaintext
    Do you want to use a text file (1) or enter tracks one by one (2)?
    ```
    Enter `2`.
4. Enter the track URL:
    ```plaintext
    Enter the track URL (or 'done' to finish):
    ```

#### Download Playlist

1. Run the script:
    ```bash
    python spot-dl.py
    ```
2. Choose the mode:
    ```plaintext
    Do you want to download a Spotify playlist (1) or individual tracks (2)?
    ```
    Enter `1`.
3. Enter the playlist URL:
    ```plaintext
    Enter the Spotify playlist URL:
    ```

## Functionalities

- **Download Individual Tracks**: You can enter the URL of a Spotify track and download it.
- **Download Playlist**: You can provide the URL of a Spotify playlist and download all tracks in it.
- **Download Tracks from File**: You can provide a text file containing multiple Spotify track URLs and download each track.

## Note

- `spotDL` downloads music from YouTube and is designed to always download the highest possible bitrate available.
- Ensure FFmpeg is installed as it is required by `spotDL`.

## License

Please just don't steal my code...

