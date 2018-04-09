#pwd to Documents working directory
#!/usr/bin/env python
'''
pip install pyglet
python3 sport/pyglet-pyglet/setup.py install
you will also need FFmpeg.
sport janicel$ python3 sport.py
'''
import pyglet
song = pyglet.media.load('GroceryScanningSound.wav')
song.play()
pyglet.app.run()
'''
from pygame import mixer # Load the required library

mixer.init()
#mixer.music.load('GroceryScanning.mp3')
mixer.music.load('GroceryScanningSound.wav')
mixer.music.play()
'''
