#!/usr/bin/env python3
from pathlib import Path
import json
import os
import sys

updatedusercontent = []
scriptpath = os.path.dirname(os.path.realpath(__file__))
arguments = sys.argv
cfgpath = scriptpath + '/playlist-cfg.json'
# the mpd music directory, where it starts searching for songs
musicdir = ''
# the folder that you want to create a playlist out of
folderpath = ''
# where you want the playlist to be outputted to
outputdir = ''
# whether or not you want the playlist to have the full path
absolutepaths = False
# name of your playlist
playlistname = 'MyPlaylist'
# used to store data before putting it into your playlist
output = ''
helptext = """
Creates m3u files with or without absolute filepaths.

Options:
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

Usage:
  ./playlist-gen.py -f 'Silent Hill' -m /home/user/Music/ -n 'Silent Hill Playlist' -d /home/user/Documents/playlists -a False
"""


def parse_arguments():
    global folderpath
    global musicdir
    global playlistname
    global outputdir
    global absolutepaths
    global validargs
    global validshorthandargs
    # to get the arguments only
    for argindex in range(1, len(arguments), 2):
        a = arguments[argindex]
        if a == '--folder-path' or a == '-f':
            folderpath = arguments[argindex + 1]
        elif a == '--music-directory' or a == '-m':
            musicdir = arguments[argindex + 1]
        elif a == '--playlist-name' or a == '-n':
            playlistname = arguments[argindex + 1]
        elif a == '--playlist-directory' or a== '-d':
            outputdir = arguments[argindex + 1]
        elif a == '--absolute-paths' or a == '-a':
            absolutepaths = eval(arguments[argindex + 1])
        else:
            print(helptext)


def write_playlist():
    global folderpath
    global musicdir
    global playlistname
    global outputdir
    global absolutepaths
    global output
    if Path(outputdir).exists() and Path(musicdir + '/' + folderpath).exists():
        songnames = os.listdir(musicdir + '/' + folderpath)
        if absolutepaths:
            folderpath = musicdir + '/' + folderpath
        else:
            pass
        for song in songnames:
            output = output + folderpath + '/' + song + '\n'
        with open(outputdir + '/' + playlistname + ".m3u", 'wt') as playlist:
            playlist.write(output.rstrip())
            playlist.close()
    

if Path(cfgpath).exists():
    with open(cfgpath, 'rt') as cfg:
        cfgdata = json.load(cfg)
        musicdir = cfgdata['music_directory']
        outputdir = cfgdata['output_directory']
        absolutepaths = cfgdata['absolute_paths']
        cfg.close()
else:
    print('Cfg not found')

parse_arguments()
write_playlist()
