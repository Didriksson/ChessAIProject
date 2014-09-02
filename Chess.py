import pygame
import Block
import Spritesheet
import GamePieces
import RuleController

class ChessGame:
	pygame.init()
	darkBrown = 183,112,0
	lightBrown = 248, 216, 166
	selectionColor = 0,100,200
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
	darkPieces = {}
	lightPieces = {}
	selection1 = ()
	selection2 = ()
	
	def start(self):
		self.loadSprites()
		self.createPieces()
		self.initializeBoard()
		self.ruleController = RuleController.RuleController(self.board,self.darkPieces,self.lightPieces)
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
	
	def createPieces(self):
		
		self.darkPieces = {
		'darkKing' : GamePieces.King(self.images.get('darkKing'),(0,4)),
		'darkQueen' : GamePieces.Queen(self.images.get('darkQueen'),(0,3)),
		'darkRook1' : GamePieces.Rook(self.images.get('darkRook'), (0,0)),
		'darkRook2' : GamePieces.Rook(self.images.get('darkRook'), (0,7)),
		'darkKnight1' : GamePieces.Knight(self.images.get('darkKnight'),(0,1)),
		'darkKnight2' : GamePieces.Knight(self.images.get('darkKnight'),(0,6)),
		'darkBishop1' : GamePieces.Bishop(self.images.get('darkBishop'),(0,5)),
		'darkBishop2' : GamePieces.Bishop(self.images.get('darkBishop'),(0,2)),
		'darkPawn1' : GamePieces.Pawn(self.images.get('darkPawn'),(1,0)),
		'darkPawn2' : GamePieces.Pawn(self.images.get('darkPawn'),(1,1)),
		'darkPawn3' : GamePieces.Pawn(self.images.get('darkPawn'),(1,2)),	
		'darkPawn4' : GamePieces.Pawn(self.images.get('darkPawn'),(1,3)),
		'darkPawn5' : GamePieces.Pawn(self.images.get('darkPawn'),(1,4)),
		'darkPawn6' : GamePieces.Pawn(self.images.get('darkPawn'),(1,5)),
		'darkPawn7' : GamePieces.Pawn(self.images.get('darkPawn'),(1,6)),
		'darkPawn8' : GamePieces.Pawn(self.images.get('darkPawn'),(1,7)),
		}

		self.lightPieces = {
		'lightKing' : GamePieces.King(self.images.get('lightKing'),(7,4)),
		'lightQueen' : GamePieces.Queen(self.images.get('lightQueen'),(7,3)),
		'lightRook1' : GamePieces.Rook(self.images.get('lightRook'), (7,0)),
		'lightRook2' : GamePieces.Rook(self.images.get('lightRook'), (7,7)),
		'lightKnight1' : GamePieces.Knight(self.images.get('lightKnight'),(7,1)),
		'lightKnight2' : GamePieces.Knight(self.images.get('lightKnight'),(7,6)),
		'lightBishop1' : GamePieces.Bishop(self.images.get('lightBishop'),(7,5)),
		'lightBishop2' : GamePieces.Bishop(self.images.get('lightBishop'),(7,2)),
		'lightPawn1' : GamePieces.Pawn(self.images.get('lightPawn'),(6,0)),
		'lightPawn2' : GamePieces.Pawn(self.images.get('lightPawn'),(6,1)),
		'lightPawn3' : GamePieces.Pawn(self.images.get('lightPawn'),(6,2)),		
		'lightPawn4' : GamePieces.Pawn(self.images.get('lightPawn'),(6,3)),
		'lightPawn5' : GamePieces.Pawn(self.images.get('lightPawn'),(6,4)),
		'lightPawn6' : GamePieces.Pawn(self.images.get('lightPawn'),(6,5)),
		'lightPawn7' : GamePieces.Pawn(self.images.get('lightPawn'),(6,6)),
		'lightPawn8' : GamePieces.Pawn(self.images.get('lightPawn'),(6,7)),
		}
		

		
		
	def initializeBoard(self):
		#Initialize board with pieces
		for y in range (8):
			line = []
			for x in range(8):
				line.append("EMPTY")
			self.board.append(line)
		
		for piece in self.lightPieces.itervalues():
			self.board[piece.position[0]][piece.position[1]] = piece
	
		for piece in self.darkPieces.itervalues():
			self.board[piece.position[0]][piece.position[1]] = piece		
			
	def mainLoop(self):
		self.currentPlayer = self.lightPieces
		while 1:
			self.paintBoard()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					position = event.pos
					row = position[1]//self.HEIGHTBLOCK
					col = position[0]//self.WIDTHBLOCK
					if not self.selection1:
						if self.board[row][col] in self.currentPlayer.values():
							self.selection1 = (row, col)
					elif self.selection1 == (row,col):
						self.selection1 = ()
					else:
						self.selection2 = (row,col)
						if self.ruleController.presentMove(self.selection1, self.selection2):
							self.selection1 = () 
							self.selection2 == ()
							if self.currentPlayer == self.lightPieces:
								self.currentPlayer = self.darkPieces
							else:
								self.currentPlayer = self.lightPieces
	
	def paintBoard(self):
		#Paint board
		for row in range(len(self.board)):
			line = []
			for col in range(len(self.board[row])):
				if (row,col) == self.selection1:
					pygame.draw.rect(self.screen,self.selectionColor, ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK),self.WIDTHBLOCK,self.HEIGHTBLOCK))
				elif (col+row) % 2 == 0:
					pygame.draw.rect(self.screen,self.lightBrown, ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK),self.WIDTHBLOCK,self.HEIGHTBLOCK))
				else:
					pygame.draw.rect(self.screen,self.darkBrown, ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK),self.WIDTHBLOCK,self.HEIGHTBLOCK))
				if self.board[row][col] != "EMPTY":
					self.screen.blit(self.board[row][col].image, ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK)))
			
		pygame.display.flip()

ChessGame().start()	
