class World:
  def __init__(self):
    self.world = None
    self.objects = []
    self.floor = []
    self.win = False
    
  def get_player(self):
    for obj in self.objects:
      if type(obj).__name__ == "Player":
        return obj
        
  def get_box_at(self, x, y):
    for obj in self.objects:
      if type(obj).__name__ == "Box" and obj.x == x and obj.y == y:
        return obj        
  
  def get_goal_at(self, x, y):
    for obj in self.objects:
      if type(obj).__name__ == "Goal" and obj.x == x and obj.y == y:
        return obj        

  def is_floor(self, x, y):
    layerId = None
    for id, layer in enumerate(self.map.layers):
      if layer.name == "Floor":
        layerId = id
        break
    if not layerId: 
      raise Exception("Could not find floor")
  
    tile = self.map.get_tile_properties(x, y, layerId)
    return tile and tile['type'] == "floor"