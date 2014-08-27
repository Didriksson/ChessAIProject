import pygame
import Block
import Spritesheet

class ChessGame:
	pygame.init()
	darkBrown = 183,112,0
	lightBrown = 248, 216, 166
	white = 255,255,255
	marginX = 5 
	marginY = 5

	WIDTHBLOCK = 64
	HEIGHTBLOCK = 64
	size = WIDTHBLOCK*8, HEIGHTBLOCK*8

	screen = pygame.display.set_mode(size)
	board = []
	boardGroup = pygame.sprite.Group()
	
	images = {}
	
	def start(self):
		self.loadSprites()
		self.initializeBoard()
		self.mainLoop()
	
	
	def loadSprites(self):
		imageList = Spritesheet.Spritesheet("pieces.png").getAllSprites(2,6, 64,64,-1)
		self.images = {
		'darkKing' : imageList[0],
		'darkQueen' : imageList[1],
		'darkRook' : imageList[2],
		'darkKnight' : imageList[3],
		'darkBishop' : imageList[4],
		'darkPawn' : imageList[5],
		'lightKing' : imageList[6],
		'lightQueen' : imageList[7],
		'lightRook': imageList[8],
		'lightKnight': imageList[9],
		'lightBishop': imageList[10],
		'lightPawn': imageList[11]
		}	

		
	def initializeBoard(self):
		#Initialize board with pieces
		for y in range (8):
			line = []
			for x in range(8):
				line.append("EMPTY")
			self.board.append(line)
		self.board[0][0] = 'darkRook'
		self.board[0][1] = 'darkKnight'
		self.board[0][2] = 'darkBishop'
		self.board[0][3] = 'darkQueen'
		self.board[0][4] = 'darkKing'
		self.board[0][5] = 'darkBishop'
		self.board[0][6] = 'darkKnight'
		self.board[0][7] = 'darkRook'

		self.board[1][0] = 'darkPawn'
		self.board[1][1] = 'darkPawn'
		self.board[1][2] = 'darkPawn'
		self.board[1][3] = 'darkPawn'
		self.board[1][4] = 'darkPawn'
		self.board[1][5] = 'darkPawn'
		self.board[1][6] = 'darkPawn'
		self.board[1][7] = 'darkPawn'

		self.board[7][0] = 'lightRook'
		self.board[7][1] = 'lightKnight'
		self.board[7][2] = 'lightBishop'
		self.board[7][3] = 'lightQueen'
		self.board[7][4] = 'lightKing'
		self.board[7][5] = 'lightBishop'
		self.board[7][6] = 'lightKnight'
		self.board[7][7] = 'lightRook'

		self.board[6][0] = 'lightPawn'
		self.board[6][1] = 'lightPawn'
		self.board[6][2] = 'lightPawn'
		self.board[6][3] = 'lightPawn'
		self.board[6][4] = 'lightPawn'
		self.board[6][5] = 'lightPawn'
		self.board[6][6] = 'lightPawn'
		self.board[6][7] = 'lightPawn'	
	
	
	def mainLoop(self):
		while 1:
			self.paintBoard()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				
	def paintBoard(self):
		#Paint board
		for row in range(len(self.board)):
			line = []
			for col in range(len(self.board[row])):
				if (col+row) % 2 == 0:
					pygame.draw.rect(self.screen,self.lightBrown, ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK),self.WIDTHBLOCK,self.HEIGHTBLOCK))
				else:
					pygame.draw.rect(self.screen,self.darkBrown, ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK),self.WIDTHBLOCK,self.HEIGHTBLOCK))
				if self.board[row][col] != "EMPTY":
					self.screen.blit(self.images.get(self.board[row][col]), ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK)))
			

		pygame.display.flip()

ChessGame().start()	
