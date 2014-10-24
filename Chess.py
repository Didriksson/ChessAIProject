import pygame
import Spritesheet
import RuleController
import AIFunctions
import Board
import Move

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
	
	images = {}
	selection1 = ()
	selection2 = ()
	
	def start(self):
		self.loadSprites()
		self.board = Board.Board()
		self.ruleController = RuleController.RuleController()
		self.aiController = AIFunctions.AIFunctions()
		self.mainLoop()
		self.paintBoard()
	
	def loadSprites(self):
		imageList = Spritesheet.Spritesheet("pieces.png").getAllSprites(2,6, 64,64,-1)
		self.images = {
		'BlackKing' : imageList[0],
		'BlackQueen' : imageList[1],
		'BlackRook' : imageList[2],
		'BlackKnight' : imageList[3],
		'BlackBishop' : imageList[4],
		'BlackPawn' : imageList[5],
		'WhiteKing' : imageList[6],
		'WhiteQueen' : imageList[7],
		'WhiteRook': imageList[8],
		'WhiteKnight': imageList[9],
		'WhiteBishop': imageList[10],
		'WhitePawn': imageList[11]
		}
		
		
		# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
		self.myfont = pygame.font.SysFont("monospace", 35)


	def mainLoop(self):
		while 1:
			if(self.board.winner == None):
				if self.board.currentPlayer == 'White':
					move = self.aiController.max(self.board)
					print move.source
					print "Destination piece : ", self.board.board[move.destination[0]][move.destination[1]]
					print "Source piece: ", self.board.board[move.source[0]][move.source[1]]
					self.board = self.ruleController.makeMove(self.board, move, True)

				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()

					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
						position = event.pos
						row = position[1]//self.HEIGHTBLOCK
						col = position[0]//self.WIDTHBLOCK
						
						if self.board.currentPlayer == 'Black':
							if not self.selection1:
								if 'Black' in self.board.board[row][col]:
									self.selection1 = (row, col)

							elif self.selection1 == (row,col):
								self.selection1 = ()

							else:
								self.selection2 = (row,col)
								move = Move.Move(self.selection1, self.selection2)
								if self.ruleController.presentMove(self.board,move):
									self.board= self.ruleController.makeMove(self.board, move, True)
									self.selection1 = () 
									self.selection2 == ()
								else:
									print 'Not OK move'""
				self.paintBoard()			
			else:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
				label = self.myfont.render("Congratulations " + self.board.winner, 1, (255,0,0))
				self.screen.blit(label, (50, 150))
				pygame.display.flip()

	
	def paintBoard(self):
		#Paint board
		for row in range(len(self.board.board)):
			line = []
			for col in range(len(self.board.board[row])):
				if (row,col) == self.selection1:
					pygame.draw.rect(self.screen,self.selectionColor, ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK),self.WIDTHBLOCK,self.HEIGHTBLOCK))
				elif (col+row) % 2 == 0:
					pygame.draw.rect(self.screen,self.lightBrown, ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK),self.WIDTHBLOCK,self.HEIGHTBLOCK))
				else:
					pygame.draw.rect(self.screen,self.darkBrown, ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK),self.WIDTHBLOCK,self.HEIGHTBLOCK))
				if self.board.board[row][col] != '':
					self.screen.blit(self.images[self.board.board[row][col]], ((col*self.WIDTHBLOCK),(row*self.HEIGHTBLOCK)))
		pygame.display.flip()

ChessGame().start()	