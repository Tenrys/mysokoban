import pygame, os

sounds = {}
audio_location = os.path.join(os.path.dirname(__file__), 'snd')
for filename in os.listdir(audio_location):
  if filename.lower().endswith(".ogg"):
    sound = pygame.mixer.Sound(os.path.join(audio_location, filename))
    sound.set_volume(0.5)
    sounds[filename[:-4]] = sound

def play_sound(name):
  if name in sounds:
    pygame.mixer.Sound.play(sounds[name])
  else:
    raise Exception("Invalid sound name")
  
print("Playing music")
pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), 'music', 'goofy.ogg'))
pygame.mixer.music.set_volume(0.75)
pygame.mixer.music.play(-1)