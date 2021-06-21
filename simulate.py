"""
- This file is for simulating boolean changes in the matrix of Hall Sensors.
"""
import copy
from helpers import *

# changes the values in the matrix from true to false or false to true
def changeSensorState(position, currentSensorArray, newState):
    positionInMatrix = convertToMatrix(position)
    updatedSensorArray = copy.deepcopy(currentSensorArray)
    updatedSensorArray[positionInMatrix[1]][positionInMatrix[0]] = newState
    return updatedSensorArray


# simulates a changing in true/false values on the simulated hallSensorStates Matrix
def simulatePhysicalMove(oldPosition, newPosition, currentSensorArray):  
    updatedSensorArray = changeSensorState(oldPosition, currentSensorArray, False)
    updatedSensorArray = changeSensorState(newPosition, updatedSensorArray, True)
    return updatedSensorArray