# Maze v1.2
# POO

# Modules importation
# -------------------
from Models.Game import *
from Models.Maze import *
from Models.MazeElement import *
from Models.Player import *

# Application
# -----------

# 1) Show initial message and get player data

# Initialize game
Game.Initialize()

# Ask for player data
PlayerName = Player.GetData()


# 2) Initialize Maze
Maze.Initialize()

# Load maze elements from json file
MazeElement.LoadElementsFromFile(Maze)
# Load maze from text file
Maze.LoadMapFromFile()

# Put objects at random positions
Maze.PlaceObjectsAtRandomPositions()

# Place player in maze
Player.PlaceInMaze(Maze)

# Draw maze on screen
Maze.DrawOnScreen()

# Start game
Game.Start(Maze)


# 3) Game loop

# Variable for end of game
EndOfGame: bool = False

# Do this until end of game is triggered
while not EndOfGame:

    # Wait for a player action
    PlayerAction: str = Player.WaitForAction()

    # Do action
    EndOfGame = Player.ExecuteAction(PlayerAction)
