from objects import BaseObject, Player, world

class Start(BaseObject):
  draw_order = 1
  no_render = True

  def __init__(self, obj):
    BaseObject.__init__(self, obj)
    for ply in world.objects:
      if type(ply) is Player:
        print("Player already exists")
        return
    Player(obj)
    