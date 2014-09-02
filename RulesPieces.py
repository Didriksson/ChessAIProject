def knight(source, destination, board, lightPieces, darkPieces):
	deltaY = (source[0] - destination[0])
	deltaX = (source[1] - destination[1])
	if tryingToTakeOwnPiece(source, destination, board, lightPieces, darkPieces):
		return False
	if abs(deltaX) == 2 and abs(deltaY) == 1 or abs(deltaX) == 1 and abs(deltaY) == 2:
		return True
	else:
		return False
	
def king(source, destination, board, lightPieces, darkPieces):
	deltaY = destination[0]-source[0]
	deltaX = destination[1]-source[1]
	if tryingToTakeOwnPiece(source, destination, board, lightPieces, darkPieces):
		return False
	sourcePiece = board[source[0]][source[1]]
	destinationPiece = board[destination[0]][destination[1]]
	if abs(deltaY) <= 1 and abs(deltaX) <=1:
		if sourcePiece in lightPieces.values():
			if destinationPiece == 'EMPTY' or destinationPiece in darkPieces.values():
				return True
			else:
				return False
		elif sourcePiece in darkPieces.values():
			if destinationPiece == 'EMPTY' or destinationPiece in lightPieces.values():
				return True
			else:
				return False
		else:
			return False

	
def rook(source, destination, board, lightPieces, darkPieces):
	deltaY = (source[0] - destination[0])
	deltaX = (source[1] - destination[1])
	
	if tryingToTakeOwnPiece(source, destination, board, lightPieces, darkPieces):
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


def queen(source, destination, board, lightPieces, darkPieces):
	if king(source, destination, board, lightPieces, darkPieces):
		return True
	if rook(source, destination, board, lightPieces, darkPieces):
		return True
	if pawn(source, destination, board, lightPieces, darkPieces):
		return True
	if bishop(source, destination, board, lightPieces, darkPieces):
		return True

	return False

def pawn(source, destination, board, lightPieces, darkPieces):
	deltaY = source[0] - destination[0]
	deltaX = source[1] - destination[1]
	#Light!
	if board[source[0]][source[1]] in lightPieces.values():
		#Moves up or down on the board.
		if (deltaY == 2 and source[0] == 6) or (deltaX == 0 and deltaY == 1):
			if board[destination[0]][destination[1]] == "EMPTY" and deltaX == 0:
				return True
			else:
				return False
		#Take another.
		else:
			if deltaY == 1 and (abs(deltaX) == 1):
					if(board[destination[0]][destination[1]] in darkPieces.values()):
						return True
					else:
						return False
	#Dark!
	if board[source[0]][source[1]] in darkPieces.values():
		#Moves up or down on the board.
		if (deltaY == -2 and source[0] == 1) or (deltaX == 0 and deltaY == -1):
			if board[destination[0]][destination[1]] == "EMPTY" and deltaX == 0:
				return True
			else:
				return False
		#Take another.
		else:
			if deltaY == -1 and (abs(deltaX) == 1):
					if(board[destination[0]][destination[1]] in lightPieces.values()):
						return True
					else:
						return False				
	else:
		return False

def bishop(source, destination, board, lightPieces, darkPieces):
	# deltaY = destination[0]-source[0]
	# deltaX = destination[1]-source[1]
	
	# if (deltaX !=0 and deltaY !=0) and abs(deltaX/deltaY) == 1:
		# if(deltaY < 0):
			# deltaPositions = range(source[0], destination[0])
			# xModifier = 1
		# else:
			# deltaPositions = range(destination[0], destination[0])
			# xModifier = -1
		# for index in deltaPositions:
			# if board[index][source[1] + xModifier] != 'EMPTY':
				# if not board[source[0]][source[1]]:
					# return False
		# return True
	# else:
		# return False
	return False
	
def tryingToTakeOwnPiece(source, destination, board, lightPieces, darkPieces):
	pieces = {board[source[0]][source[1]], board[destination[0]][destination[1]]}
	if pieces.issubset(lightPieces.values()) or pieces.issubset(darkPieces.values()):
		return True
	else:
		return False
		
	