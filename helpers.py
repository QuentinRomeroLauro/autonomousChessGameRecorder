import chess


# the following two functions are to make simulating the piece moves easier
# converts a (row, col) formatted position in the boolean sensor matrix into a chess notation (ex/ "e2") string
def convertToNotation (x, y):
    letters = "abcdefgh"
    l1 = letters[x]
    l2 = str(y+1)
    return l1+l2

# converts a chess notation string (ex/ "e4") into a sensor matrix position in the boolean sensor matrix (ex/ "A1" -> (0, 0) )
def convertToMatrix(position):
    letters = "abcdefgh"
    x = letters.index(position[0])
    y = int(position[1]) - 1
    return x, y

# returns the bool value that a current position has in the sensor matrix 
def getSensorValue(currentSensorArray, position):
    x, y = convertToMatrix(position)
    return currentSensorArray[y][x]


# this returns the position (in chess notation) of the moved piece
# called when a move is made (the sensor states will change)
def getMovedPiecePosition(prevSensorStates, currSensorStates):
  row = 0
  
  while row < 8:
    for col in range(8):
      if (prevSensorStates[row][col] == True) and (currSensorStates[row][col] == False):
        return convertToNotation(col, row)
        break
    row += 1


# there is no function to do this within the python-chess api so I had to make one here
# returns the legal moves for a given piece in a given position
# used to evaluate where a piece moved only based on our true and false values
def getLegalPieceMoves(board, piecePosition):
    legalMoves = []
    
    for possibleMove in range(63):
        try:
            board.find_move(chess.SQUARE_NAMES.index(piecePosition), possibleMove)
            legalMoves.append(chess.SQUARE_NAMES[possibleMove])
        except:
            pass
        
    return legalMoves
      


# if move is deterministic, returns the move. if move is not deterministic, returns a list of possibleMoves with the position the piece is moving from
def determineMove(prevSensorStates, currSensorStates, piecePosition, board):
    
    
    legalMoves = getLegalPieceMoves(board, piecePosition)
    possibleLegalMoves = []
    takeablePieces = 0
    likelyMove = None
    for possibleMove in legalMoves:
            
        # gets the boolean sensorState of the possible move on the previous sensor array
        possibleMovePrevSensorState = getSensorValue(prevSensorStates, possibleMove)
        possibleMoveCurrSensorState = getSensorValue(currSensorStates, possibleMove)
    
        # if a possible move was false before and now it is true, it has to be the move.
        if (possibleMovePrevSensorState == False) and (possibleMoveCurrSensorState == True):
            return (piecePosition + possibleMove).lower()

        # if there is only once takeable piece it is also determinable.
        if possibleMovePrevSensorState == True:
            likelyMove = possibleMove
            takeablePieces += 1

    # function won't reach this point if the first conditional in the for loop is met
    if takeablePieces == 1:
        # move is determinable if there is only one takeable piece  
        return (piecePosition + likelyMove).lower()
    else:
        # if there is more than one takeable piece, a list of all the legalMoves would be the determined move
        for move in legalMoves:
            if getSensorValue(prevSensorStates, move) == True:
                possibleLegalMoves.append(move)
            
        return possibleLegalMoves
    