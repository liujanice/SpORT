#pwd to Documents working directory
#!/usr/bin/env python
'''
pip install pyglet
python3 sport/setup.py install
you will also need FFmpeg.
sport user$ python3 sport.py
'''
import pyglet
song = pyglet.media.load('GroceryScanningSound.wav')
song.play()
pyglet.app.run()

