from .World import World

world = World()

class BaseObject:  
  draw_order = 0
  no_render = False
  
  def __init__(self, obj):
    self.image = obj.image
    self.width = obj.properties['width']
    self.height = obj.properties['height']
    self.x = obj.x / obj.properties['width']
    self.y = obj.y / obj.properties['height']
    world.objects.append(self)
  
from .Box import Box
from .Goal import Goal
from .Player import Player
from .Start import Start

objects = {'box': Box, 'goal': Goal, 'player': Player, 'start': Start}

