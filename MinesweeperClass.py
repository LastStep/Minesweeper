import pygame as py

class Cell:

  def __init__(self, x, y, size):
    self.x = x
    self.y = y
    self.size = size
    self.mine = False
    self.value = 0
    self.neighbours = []
    self.revealed = False

  def show(self, screen):
    w = self.size
    py.draw.rect(screen, (255,255,255), (w*self.x, w*self.y, w, w), 1)
    center = (w * self.x + w // 2, w * self.y + w // 2)
    if self.revealed:
      if self.mine:
        py.draw.circle(screen, (255, 0, 0), center, w//4)
      else:
        py.draw.rect(screen, (180, 120, 120), (w * self.x, w * self.y, w, w))
        myfont = py.font.SysFont('Ariel', 30)
        if self.value != 0:
          textSurface = myfont.render(str(self.value), True, (0,100,30*self.value))
          screen.blit(textSurface, (w*self.x + w//3, w*self.y + w//4))

  def find_value(self, grid):
    if self.mine:
      return []
    i = self.x
    j = self.y
    for row in [i-1,i,i+1]:
      for col in [j-1,j,j+1]:
        if -1 < row < grid.shape[0] and -1 < col < grid.shape[1]:
          if row != i or col != j:
            self.neighbours.append(grid[row][col])