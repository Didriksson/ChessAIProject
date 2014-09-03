import pygame
import Block
import Spritesheet
import GamePieces
import RuleController
import AIFunctions

class ChessGame:
	pygame.init()
	darkBrown = 183,112,0
	lightBrown = 248, 216, 166
	selectionColor = 0,100,200
	white = 255,255,255
	marginX = 5 
	marginY = 5
	winner = None

	
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
		self.ruleController = RuleController.RuleController(self.darkPieces,self.lightPieces)
		self.aiController = AIFunctions.AIFunctions(self.lightPieces, self.darkPieces)
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
		
		
		# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
		self.myfont = pygame.font.SysFont("monospace", 35)

	
	def createPieces(self):
		
		self.darkPieces = {
		'darkKing' : GamePieces.King('darkKing',(0,4), 'black'),
		'darkQueen' : GamePieces.Queen('darkQueen',(0,3),'black'),
		'darkRook1' : GamePieces.Rook('darkRook', (0,0),'black'),
		'darkRook2' : GamePieces.Rook('darkRook', (0,7),'black'),
		'darkKnight1' : GamePieces.Knight('darkKnight',(0,1),'black'),
		'darkKnight2' : GamePieces.Knight('darkKnight',(0,6),'black'),
		'darkBishop1' : GamePieces.Bishop('darkBishop',(0,5),'black'),
		'darkBishop2' : GamePieces.Bishop('darkBishop',(0,2),'black'),
		'darkPawn1' : GamePieces.Pawn('darkPawn',(1,0),'black'),
		'darkPawn2' : GamePieces.Pawn('darkPawn',(1,1),'black'),
		'darkPawn3' : GamePieces.Pawn('darkPawn',(1,2),'black'),	
		'darkPawn4' : GamePieces.Pawn('darkPawn',(1,3),'black'),
		'darkPawn5' : GamePieces.Pawn('darkPawn',(1,4),'black'),
		'darkPawn6' : GamePieces.Pawn('darkPawn',(1,5),'black'),
		'darkPawn7' : GamePieces.Pawn('darkPawn',(1,6),'black'),
		'darkPawn8' : GamePieces.Pawn('darkPawn',(1,7),'black'),
		}

		self.lightPieces = {
		'lightKing' : GamePieces.King(('lightKing'),(7,4),'white'),
		'lightQueen' : GamePieces.Queen(('lightQueen'),(7,3),'white'),
		'lightRook1' : GamePieces.Rook(('lightRook'), (7,0),'white'),
		'lightRook2' : GamePieces.Rook(('lightRook'), (7,7),'white'),
		'lightKnight1' : GamePieces.Knight(('lightKnight'),(7,1),'white'),
		'lightKnight2' : GamePieces.Knight(('lightKnight'),(7,6),'white'),
		'lightBishop1' : GamePieces.Bishop(('lightBishop'),(7,5),'white'),
		'lightBishop2' : GamePieces.Bishop(('lightBishop'),(7,2),'white'),
		'lightPawn1' : GamePieces.Pawn(('lightPawn'),(6,0),'white'),
		'lightPawn2' : GamePieces.Pawn(('lightPawn'),(6,1),'white'),
		'lightPawn3' : GamePieces.Pawn(('lightPawn'),(6,2),'white'),		
		'lightPawn4' : GamePieces.Pawn(('lightPawn'),(6,3),'white'),
		'lightPawn5' : GamePieces.Pawn(('lightPawn'),(6,4),'white'),
		'lightPawn6' : GamePieces.Pawn(('lightPawn'),(6,5),'white'),
		'lightPawn7' : GamePieces.Pawn(('lightPawn'),(6,6),'white'),
		'lightPawn8' : GamePieces.Pawn(('lightPawn'),(6,7),'white'),
		}
		
		
	def initializeBoard(self):
		#Initialize board with pieces
		for y in range (8):
			line = []
			for x in range(8):
				line.append(GamePieces.Empty())
			self.board.append(line)
		
		for piece in self.lightPieces.itervalues():
			self.board[piece.position[0]][piece.position[1]] = piece
	
		for piece in self.darkPieces.itervalues():
			self.board[piece.position[0]][piece.position[1]] = piece		
			
	def mainLoop(self):
		self.currentPlayer = 'white'
		while 1:
			if(self.winner == None):
				self.paintBoard()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
						position = event.pos
						row = position[1]//self.HEIGHTBLOCK
						col = position[0]//self.WIDTHBLOCK
						
						if self.currentPlayer == 'black':
							if not self.selection1:
								if self.board[row][col].color == 'black':
									self.selection1 = (row, col)

							elif self.selection1 == (row,col):
								self.selection1 = ()

							else:
								self.selection2 = (row,col)
								print "PING!"
								if self.ruleController.presentMove(self.board,self.selection1, self.selection2):
									self.board = self.ruleController.makeMove(self.board, self.selection1, self.selection2, True)
									self.selection1 = () 
									self.selection2 == ()
									self.currentPlayer = 'white'
				
				if self.currentPlayer == 'white':
					self.board = self.aiController.max(self.board)
					self.currentPlayer = 'black'
			

			
			
			
			
			
			else:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
				label = self.myfont.render("Congratulations " + self.winner, 1, (255,0,0))
				self.screen.blit(label, (50, 150))
				pygame.display.flip()

	
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
				if self.board[row][col].color != "EMPTY":
					self.screen.blit(self.images[self.board[row][col].image], ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK)))
		
		# if self.ruleController.isChess(self.board,self.currentPlayer):
			# label = self.myfont.render("Chess!!", 1, (255,0,0))
			# self.screen.blit(label, (200, 50))
		pygame.display.flip()

ChessGame().start()	
