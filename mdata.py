import os
from pprint import pprint
from collections import defaultdict

path = r'\Users\music-path'
music_list = []
music_list2 = []

all_ = {}


for roots, directory, file in os.walk(path):
    for mp3 in file:
        if mp3.endswith('.mp3') or mp3.endswith('.m4a'):
            music_list.append(mp3)
            music_list2.append(roots)

d = defaultdict(list)
for k, v in zip(music_list2, music_list):
    d[k].append(v)
pprint(d.keys())
