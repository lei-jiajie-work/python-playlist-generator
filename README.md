# python-playlist-generator
A playlist generator I made to create playlists for mpd/mpc.


Creates m3u files with or without absolute filepaths.


# Options:


  -f, --folder-path


    Specifies which directory the songs are in for the playlist.
    The directory must be in --music-directory.
    Do not include what is in --music-directory.
    The folder must only have songs.

  
  -m, --music-directory

  
    This is the base directory for all your music,
    if absolute is 'false' this bit won't be included in the music path

  
  -n, --playlist-name

  
    The name of your playlist.

  
  -d, --playlist-directory

  
    The directory that the playlist is written to.


  
  -a, --absolute-paths

  
    Whether or not the --music-directory is included in the final filepaths
    for each song in your playlist.


  
  -h, --help

  
    Display this text.


# Usage:


  ./playlist-gen.py -f 'Silent Hill' -m /home/user/Music -n 'Silent Hill Playlist' -d /home/user/Documents/playlists -a False
