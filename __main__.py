import pygame, os, pygame.freetype

pygame.init()

screen = pygame.display.set_mode((640, 480))

from maps import render_map, init_map, world

done = False

init_map()

import events

font = pygame.freetype.Font(os.path.join(os.path.dirname(__file__), "fonts", "game.ttf"), 32)
# font = pygame.freetype.SysFont(None, 24)

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
      continue
    events.handle(event)
      
  screen.fill((0, 0, 0))
  
  render_map(screen)
  
  (scrW, scrH) = pygame.display.get_window_size()
  
  text = """Controls:
R - Reset
Backspace - Undo
Arrow keys - Move"""
  
  x = scrW - 8
  y = scrH - 8
  lines = text.split("\n")
  lines.reverse()
  spacing = 4
  for line in lines:
    (img, rect) = font.render(line, (255, 255, 255))
    w, h = img.get_width(), img.get_height()
    screen.blit(img, (x - w, y - (h + spacing)))
    y -= (h + spacing)
    
  if world.win:
    text = """You win!"""
    (img, rect) = font.render(text, (127, 255, 127))
    w, h = img.get_width(), img.get_height()
    screen.blit(img, (8, scrH - 8 - h))
    
  pygame.display.flip()

