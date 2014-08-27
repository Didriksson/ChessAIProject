import pygame

class Spritesheet(object):
	def __init__(self, url):
		try:
			self.sheet = pygame.image.load("pieces.png").convert()
		except pygame.error, message:
			print "Could not load file. Error message: " + message
		
	def imageAt(self, rectangle, colorkey = None):
		rect = pygame.Rect(rectangle)
		image = pygame.Surface(rect.size).convert()
		image.blit(self.sheet, (0,0), rect)
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, pygame.RLEACCEL)
		return image
		
	def getAllSprites(self,rows, cols, spriteWidth, spriteHeight, colorkey):
		sprites = []
		for row in range(rows):
			for col in range(cols):
				rectangle = (col*spriteWidth, row*spriteHeight, spriteWidth,spriteHeight)
				rect = pygame.Rect(rectangle)
				sprites.append(self.imageAt(rect,colorkey))
		return sprites