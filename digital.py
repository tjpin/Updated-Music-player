from pprint import pprint

from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineListItem, TwoLineIconListItem, IconLeftWidget, OneLineIconListItem
from kivy.core.audio import SoundLoader
from audio_android import SoundAndroid
from collections import defaultdict
import os

SoundLoader.register(SoundAndroid)


class PlayerWindow(BoxLayout):
    music_list = []
    music_list2 = []
    full = {}
    playing = ''
    directory = r'\Users\lazar\Desktop\statics'

    def __init__(self, **kwargs):
        super(PlayerWindow, self).__init__(**kwargs)

        self.get_music(self.directory)

        self.load_music()

    def get_music(self, path):
        for roots, directory, file in os.walk(path):
            for mp3 in file:
                if mp3.endswith('.mp3') or mp3.endswith('.m4a'):
                    self.music_list.append(mp3)
                    self.music_list2.append(roots+'\\'+mp3)
        # pprint(self.music_list2)

    def load_music(self):
        self.music_list.sort()
        for track in self.music_list2:
            icon_list = OneLineListItem(
                text=track,
                theme_text_color='Custom',
                text_color=[1, 1, 1, 1],
                on_release=self.mplay)
            self.ids.selected.text = track
            self.ids.playlist.add_widget(icon_list)

    def mplay(self, instance):
        try:
            self.playing.stop()
        except:
            pass
        self.playing = SoundLoader.load(instance.text)
        # print(self.directory + '\\' + instance.text)
        self.ids.selected.text = instance.text
        self.playing.play()


class DigitalApp(MDApp):
    def build(self):
        return PlayerWindow()


DigitalApp().run()
