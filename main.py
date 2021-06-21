from simulate import *
from helpers import *
import chess

# initialize the possible boards array. - at the begininning there is only one board by definition.
possibleChessBoards = [chess.Board()]

# in the final version, these values will be tied to variables.
# the record will be updated with a physical button press
# maybe could create an object ot make the hall sensor states more readable but it is what it is for now.
hallSensorStates = [ 
  [[True, True, True, True, True, True, True, True],
  [True, True, True, True, True, True, True, True],
  [False, False, False, False, False, False, False, False],
  [False, False, False, False, False, False, False, False],
  [False, False, False, False, False, False, False, False],
  [False, False, False, False, False, False, False, False],
  [True, True, True, True, True, True, True, True],
  [True, True, True, True, True, True, True, True]]
  ]


# called on the physical button press
# returns a new list of possibleBoards
def updatePossibleBoards(possibleChessBoards, currSensorStates, prevSensorStates):
  piecePosition = getMovedPiecePosition(prevSensorStates, currSensorStates)
  # stores indecies of possibleBoards to eliminate
  boardsToDelete = []
  # stores board objects to add 
  boardsToAdd = []
  for index, board in enumerate(possibleChessBoards):
    possibleMoves = determineMove(prevSensorStates, currSensorStates, piecePosition, board)
    if isinstance(possibleMoves, str):
          # move was determineable
          board.push(chess.Move.from_uci(possibleMoves))
          
    elif isinstance(possibleMoves, list) and len(possibleMoves) > 0:

          # move was not determinable
          boardsToDelete.append(index)
          for possibleMove in possibleMoves:
                # not sure if this works
                newBoard = board.copy()
                newBoard.push(chess.Move.from_uci(piecePosition + possibleMove))
                boardsToAdd.append(newBoard)
                
    else:
        # if there is nothing in the list and the move was not determinable it is deterministically not a possible board so delete the board from the list
        boardsToDelete.append(index)

  for index in boardsToDelete:
        possibleChessBoards.pop(index)
      
  for board in boardsToAdd:
        possibleChessBoards.append(board)

  return possibleChessBoards                
                


"""
# simulation
hallSensorStates.append(simulatePhysicalMove("g1", "f3", hallSensorStates[-1]))
possibleChessBoards = updatePossibleBoards(possibleChessBoards, hallSensorStates[-1], hallSensorStates[-2])

print(possibleChessBoards)

hallSensorStates.append(simulatePhysicalMove("g7", "g5", hallSensorStates[-1]))
possibleChessBoards = updatePossibleBoards(possibleChessBoards, hallSensorStates[-1], hallSensorStates[-2])

print(possibleChessBoards)

hallSensorStates.append(simulatePhysicalMove("b1", "c3", hallSensorStates[-1]))
possibleChessBoards = updatePossibleBoards(possibleChessBoards, hallSensorStates[-1], hallSensorStates[-2])

print(possibleChessBoards)

hallSensorStates.append(simulatePhysicalMove("e7", "e5", hallSensorStates[-1]))
possibleChessBoards = updatePossibleBoards(possibleChessBoards, hallSensorStates[-1], hallSensorStates[-2])

print(possibleChessBoards)

hallSensorStates.append(simulatePhysicalMove("f3", "g5", hallSensorStates[-1]))
possibleChessBoards = updatePossibleBoards(possibleChessBoards, hallSensorStates[-1], hallSensorStates[-2])

print(possibleChessBoards)

hallSensorStates.append(simulatePhysicalMove("d8", "g5", hallSensorStates[-1]))
possibleChessBoards = updatePossibleBoards(possibleChessBoards, hallSensorStates[-1], hallSensorStates[-2])

print(possibleChessBoards)

# it works !!!!

"""