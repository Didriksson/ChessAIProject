def knight(source, destination, board):
	deltaY = (source[0] - destination[0])
	deltaX = (source[1] - destination[1])
	
	sourceLocation = board[source[0]][source[1]]
	destinationLocation = board[destination[0]][destination[1]]
	
	if sourceLocation == 'EMPTY':
		return False
	
	if destinationLocation != 'EMPTY':
		if sourceLocation.color == destinationLocation.color:
			return False
		
	if abs(deltaX) == 2 and abs(deltaY) == 1 or abs(deltaX) == 1 and abs(deltaY) == 2:
		return True
	else:
		return False
	
def king(source, destination, board):
	deltaY = destination[0]-source[0]
	deltaX = destination[1]-source[1]
	
	sourceLocation = board[source[0]][source[1]]
	destinationLocation = board[destination[0]][destination[1]]

	if sourceLocation == 'EMPTY':
		return False
	
	if destinationLocation != 'EMPTY':
		if sourceLocation.color == destinationLocation.color:
			return False
			
	if abs(deltaY) <= 1 and abs(deltaX) <=1:
		return True
	else:
		return False

	
def rook(source, destination, board):
	deltaY = (source[0] - destination[0])
	deltaX = (source[1] - destination[1])
	sourceLocation = board[source[0]][source[1]]
	destinationLocation = board[destination[0]][destination[1]]
	
	if sourceLocation == 'EMPTY':
		return False
	
	if destinationLocation != 'EMPTY':
		if sourceLocation.color == destinationLocation.color:
			return False
	
	#Going wide!
	if abs(deltaX) > 0 and abs(deltaY) == 0:
		#Leftie!
		if(deltaX < 0):
			deltaPositions = range(source[1]+1, destination[1])
		#Rightie!
		else:
			deltaPositions = range(destination[1]+1, source[1])
		
		for index in deltaPositions:
			if board[source[0]][index] != 'EMPTY':
				return False
		return True
		
	#Going high!
	elif abs(deltaX) == 0 and abs(deltaY) > 0:
		#Upsie!
		if(deltaY < 0):
			deltaPositions = range(source[0]+1, destination[0])
		#Downie!
		else:
			deltaPositions = range(destination[0]+1, source[0])
		
		for index in deltaPositions:
			if board[index][source[1]] != 'EMPTY':
				return False
		return True
	
	else:
		return False


def queen(source, destination, board):
	if king(source, destination, board):
		return True
	if rook(source, destination, board):
		return True
	if pawn(source, destination, board):
		return True
	if bishop(source, destination, board):
		return True

	return False

def pawn(source, destination, board):
	deltaY = source[0] - destination[0]
	deltaX = source[1] - destination[1]
	
	sourceLocation = board[source[0]][source[1]]
	destinationLocation = board[destination[0]][destination[1]]
	
	if sourceLocation == 'EMPTY':
		return False
	
	if destinationLocation != 'EMPTY':
		if sourceLocation.color == destinationLocation.color:
			return False

	#Light!
	if sourceLocation.color == 'white':
		#Moves up or down on the board.
		print "This is it2!"
		if (deltaY == 2 and source[0] == 6) or (deltaX == 0 and deltaY == 1):
			if destinationLocation == "EMPTY" and deltaX == 0:
				return True
			else:
				return False
		#Take another.
		else:
			if deltaY == 1 and (abs(deltaX) == 1) and destinationLocation != 'EMPTY':
				return True
	#Dark!
	elif sourceLocation.color == 'black':
		#Moves up or down on the board.
		if (deltaY == -2 and source[0] == 1) or (deltaX == 0 and deltaY == -1):
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
def bishop(source, destination, board):
	deltaY = destination[0]-source[0]
	deltaX = destination[1]-source[1]
	
	sourceLocation = board[source[0]][source[1]]
	destinationLocation = board[destination[0]][destination[1]]
	
	if sourceLocation == 'EMPTY':
		return False
	
	if destinationLocation != 'EMPTY':
		if sourceLocation.color == destinationLocation.color:
			return False
			
	if (deltaX !=0 and deltaY !=0) and abs(deltaX/(float(deltaY))) == 1:
		if(deltaY < 0):
			deltaPositions = range(source[0], destination[0])
			xModifier = 1
		else:
			deltaPositions = range(destination[0], destination[0])
			xModifier = -1
		for index in deltaPositions:
			if board[index][source[1] + xModifier] != 'EMPTY':
				if not board[source[0]][source[1]]:
					return False
		return True
	else:
		return False