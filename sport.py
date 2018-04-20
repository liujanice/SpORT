#pwd to Documents working directory
'''
pip install pyglet
python3 sport/setup.py install
sport user$ python3 sport.py
'''
import pyglet
song = pyglet.media.load('GroceryScanningSound.wav')
song.play()
pyglet.app.run()

