import pygame, os, inspect
from pytmx import TiledObjectGroup, TiledTileLayer
from pytmx.util_pygame import load_pygame
from objects import objects, world
import events
import audio

map = load_pygame(os.path.join(os.path.dirname(__file__), 'tiled', 'maps', '1.tmx'))

def init_map():
  world.map = map
  world.win = False
  
  for layer in map.layers:  
    if type(layer) is TiledObjectGroup:
      for obj in layer:
        objects[obj.properties.get('type')](obj)
        
def keydown(event):
  if event.key == pygame.K_r:
    world.objects.clear()
    init_map()
    audio.play_sound("reset")
events.add_handler(pygame.KEYDOWN, keydown)  
      
def render_map(screen):
  for layer in map.layers:
    if type(layer) is TiledTileLayer:
      for x, y, image in layer.tiles():
        x *= map.tilewidth
        y *= map.tileheight
        screen.blit(image, (x, y))
        
  for obj in sorted(world.objects, key=lambda x: x.draw_order):
    if obj.no_render: continue
    x, y, image = obj.x, obj.y, obj.image
    x *= obj.width
    y *= obj.height
    screen.blit(image, (x, y))