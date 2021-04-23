import audio
from objects import BaseObject, world

def check_win():
  win = True
  for obj in world.objects:
    if type(obj).__name__ == "Goal":
      if not world.get_box_at(obj.x, obj.y):
        win = False
        break
  world.win = win
  return win

class Box(BaseObject):
  draw_order = 3
  
  def move(self, deltaX, deltaY):
    x = self.x + deltaX
    y = self.y + deltaY 
      
    if world.is_floor(x, y) and not world.get_box_at(x, y):
      if world.get_goal_at(self.x, self.y) and (self.x != x or self.y != y):
        audio.play_sound("cancel")
        
      self.x = x
      self.y = y
      audio.play_sound("box_move")
      
      if check_win():
        audio.play_sound("end_1")
      elif world.get_goal_at(x, y):
        audio.play_sound("end_2")
      return True
    else:
      return False
