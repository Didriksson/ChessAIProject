def knight(move, board):
	deltaY = (move.source[0] - move.destination[0])
	deltaX = (move.source[1] - move.destination[1])
	
	sourceLocation = board[move.source[0]][move.source[1]]
	destinationLocation = board[move.destination[0]][move.destination[1]]
	
	if sourceLocation == 'EMPTY':
		return False
	
	if destinationLocation != 'EMPTY':
		if sourceLocation.color == destinationLocation.color:
			return False
		
	if abs(deltaX) == 2 and abs(deltaY) == 1 or abs(deltaX) == 1 and abs(deltaY) == 2:
		return True
	else:
		return False
	
def king(move, board):
	deltaY = move.destination[0]-move.source[0]
	deltaX = move.destination[1]-move.source[1]
	
	sourceLocation = board[move.source[0]][move.source[1]]
	destinationLocation = board[move.destination[0]][move.destination[1]]
	
	if sourceLocation == 'EMPTY':
		return False
	
	if destinationLocation != 'EMPTY':
		if sourceLocation.color == destinationLocation.color:
			return False
			
	if abs(deltaY) <= 1 and abs(deltaX) <=1:
		return True
	else:
		return False

	
def rook(move, board):
	deltaY = (move.source[0] - move.destination[0])
	deltaX = (move.source[1] - move.destination[1])
	sourceLocation = board[move.source[0]][move.source[1]]
	destinationLocation = board[move.destination[0]][move.destination[1]]
	xModifier = 1
	yModifier = 1
	
	if sourceLocation.color == 'EMPTY':
		return False
	
	if destinationLocation.color != 'EMPTY':
		if sourceLocation.color == destinationLocation.color:
			return False
			
	if (deltaX * deltaY) == 0:
		boardRange = [] 
		if deltaX >= 1:
			boardRange = range(abs(deltaX))
			xModifier = 1
			yModifier = 0
		elif deltaX <= -1:
			boardRange = range(abs(deltaX))
			xModifier = -1
			yModifier = 0
		elif deltaY >= 1:
			boardRange = range(abs(deltaY))
			yModifier = -1
			xModifier = 0
		else:
			boardRange = range(abs(deltaY))
			yModifier = 1
			xModifier = 0

		for index in boardRange:
			row = move.source[0] + index*yModifier
			col = move.source[1] + index*xModifier
			if col not in range(8) or row not in range(8):
				break

			if board[row][col].color != 'EMPTY':
				if board[row][col] is not sourceLocation:
					return False
		return True
	else:
		return False


def queen(move, board):
	if king(move, board):
		#print "Moving with kings rules."
		return True
	if rook(move, board):
		#print "Moving with rook rules."
		return True
	if pawn(move, board):
		#print "Moving with pawn rules."
		return True
	if bishop(move, board):
		#print "Moving with bishop rules."
		return True

	return False

def pawn(move, board):
	deltaY = move.source[0] - move.destination[0]
	deltaX = move.source[1] - move.destination[1]
	
	sourceLocation = board[move.source[0]][move.source[1]]
	destinationLocation = board[move.destination[0]][move.destination[1]]	
	if sourceLocation == 'EMPTY':
		return False
	
	if destinationLocation != 'EMPTY':
		if sourceLocation.color == destinationLocation.color:
			return False

	#Light!
	if sourceLocation.color == 'white':
		#Moves up or down on the board.
		if (deltaY == 2 and move.source[0] == 6) or (deltaX == 0 and deltaY == 1):
			if destinationLocation.color == "EMPTY" and deltaX == 0:
				return True
			else:
				return False
		#Take another.
		else:
			if deltaY == 1 and (abs(deltaX) == 1) and destinationLocation.color != 'EMPTY':
				return True
	#Dark!
	elif sourceLocation.color == 'black':
		#Moves up or down on the board.
		if (deltaY == -2 and move.source[0] == 1) or (deltaX == 0 and deltaY == -1):
			if destinationLocation.color == "EMPTY" and deltaX == 0:
				return True
			else:
				return False
		#Take another.
		else:
			if deltaY == -1 and (abs(deltaX) == 1) and destinationLocation.color != 'EMPTY':
				return True
	else:
		return False
def bishop(move, board):
	deltaY = move.destination[0]-move.source[0]
	deltaX = move.destination[1]-move.source[1]
	sourceLocation = board[move.source[0]][move.source[1]]
	destinationLocation = board[move.destination[0]][move.destination[1]]
	
	if sourceLocation.color == 'EMPTY':
		return False
	
	if destinationLocation.color != 'EMPTY':
		if sourceLocation.color == destinationLocation.color:
			return False
			
	if (deltaX !=0 and deltaY !=0) and abs(deltaX/(float(deltaY))) == 1:
		if deltaX >= 1:
			xModifier = 1
		else:
			xModifier = -1
		if deltaY >= 1:
			yModifier = 1
		else:
			yModifier = -1

		for index in range(abs(deltaY)):
			row = move.source[0] + index*yModifier
			col = move.source[1] + index*xModifier
			if col not in range(len(board)) or row not in range(len(board)):
				break
			if board[row][col].color != 'EMPTY':
				if board[row][col] is not sourceLocation:
					return False
		return True
	else:
		return False