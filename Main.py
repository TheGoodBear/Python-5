# Maze v1.2
# POO

# Modules importation
# -------------------
import os
import json
import random
import Models.Game as Game
import Models.Maze as Maze


# Variables (must be declared BEFORE using them)
# ---------


# Methods (must be declared BEFORE using them)
# -------


# Application
# -----------

# 1) Show initial message and get player data

# Application start
Game.ApplicationStart()

# Ask for player data
PlayerName = GetPlayerData()

# Say welcome
SayWelcome()


# 2) Initialize Maze

# Load maze elements from json file
Maze.LoadMazeElementsFromFile(MazeFileName)
# Load maze from text file
Maze.LoadMazeFromFile(MazeFileName)

# Put objects in random positions
PlaceMazeObjectsAtRandomPositions()

# Place player in maze
PlacePlayerInMaze()

# Draw maze on screen
DrawMazeOnScreen()

# Start game
StartGame()


# 3) Game loop

# Variable for end of game
EndOfGame: bool = False

# Do this until end of game is triggered
while not EndOfGame:

    # Wait for a player action
    PlayerAction: str = WaitForPlayerAction()

    # Do action
    EndOfGame = ExecutePlayerAction(PlayerAction)
