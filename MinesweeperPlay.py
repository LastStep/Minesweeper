import pygame as py
from random import randint
import numpy as np
import Minesweeper.MinesweeperClass as Mine
py.init()

width, height = 800, 600
size = 30
rows, cols = width//size, height//size
screen = py.display.set_mode((width - width%size,height + 100))

grid = np.empty([rows, cols], dtype = object)
def setup():
  for row in range(rows):
    for col in range(cols):
      grid[row][col] = Mine.Cell(row, col, size)
      if randint(0,500) % 7 == 0:
        grid[row][col].mine = True

  for row in range(rows):
    for col in range(cols):
      grid[row][col].find_value(grid)
      for cell in grid[row][col].neighbours:
        if cell.mine:
          grid[row][col].value += 1

def mouse_input(click):
  global stack, flag
  try:
    cell = grid[int(click[0]) // size][int(click[1]) // size]
    if flag:
      cell.revealed = True
      cell.show(screen)
      if cell.mine:
        gameover.play()
        for row in range(rows):
          for col in range(cols):
            if grid[row][col].mine:
              grid[row][col].revealed = True
              grid[row][col].show(screen)
              py.display.update()
              clock.tick(60)
        flag = False
      elif cell.value == 0:
        flow.play()
        flood_fill(cell)
        stack.clear()
      else:
        reveal.play()
  except IndexError:
    flag = True
    setup()

stack = []
def flood_fill(cell):
  global stack
  for cell in cell.neighbours:
    cell.revealed = True
    cell.show(screen)
    if cell.value == 0 and not cell.mine and cell not in stack:
      stack.append(cell)
      flood_fill(cell)

setup()
clock = py.time.Clock()
reveal = py.mixer.Sound(r'C:\Users\Gray\Random\Minesweeper\reveal.wav')
gameover = py.mixer.Sound(r'C:\Users\Gray\Random\Minesweeper\gameover.wav')
flow = py.mixer.Sound(r'C:\Users\Gray\Random\Minesweeper\flow.wav')
game = True
flag = True
while game:
  for event in py.event.get():
    if event.type == py.QUIT:
      game = False
    if event.type == py.MOUSEBUTTONDOWN:
      mouse_input(py.mouse.get_pos())

  screen.fill((0,0,0))
  myfont = py.font.SysFont('Ariel', 70)
  textSurface = myfont.render('RESTART', True, (0, 255, 0))
  screen.blit(textSurface, (width//2 - 100, height + 20))

  for row in range(rows):
    for col in range(cols):
      grid[row][col].show(screen)
  py.display.update()


