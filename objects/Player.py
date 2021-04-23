import pygame
from objects import BaseObject, world
import events
import audio


def keydown(event):
  if event.key == pygame.K_BACKSPACE:
    world.get_player().undo()
    return

  x, y = 0, 0
  if event.key == pygame.K_RIGHT:
    x = 1
  if event.key == pygame.K_LEFT:
    x = -1
  if event.key == pygame.K_DOWN:
    y = 1
  if event.key == pygame.K_UP:
    y = -1
  if x != 0 or y != 0:
    world.get_player().move(x, y)
    return
events.add_handler(pygame.KEYDOWN, keydown)

class Player(BaseObject):
  draw_order = 2
  
  def __init__(self, obj):
    BaseObject.__init__(self, obj)
    self.last_action = (None, None)
    
  def move(self, deltaX, deltaY):  
    x = self.x + deltaX
    y = self.y + deltaY 
      
    box = world.get_box_at(x, y)
    
    success = None
    if box:
      success = box.move(deltaX, deltaY)
      
    if world.is_floor(x, y) and (success == True or success == None):
      self.x = x
      self.y = y
      # if success == None: # Annoying
      #   audio.play_sound('move')
      self.last_action = (deltaX, deltaY)
    else:
      audio.play_sound('buzzer')
      
  def undo(self):
    if not self.last_action: return audio.play_sound('buzzer')
    
    (deltaX, deltaY) = self.last_action    
    x = self.x + deltaX
    y = self.y + deltaY 
      
    box = world.get_box_at(x, y)
    
    if box:
      box.move(-deltaX, -deltaY)
      
    self.x = self.x - deltaX
    self.y = self.y - deltaY
    audio.play_sound('cancel')
    
    self.last_action = None
