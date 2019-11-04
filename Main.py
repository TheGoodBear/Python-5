# Maze v1.2
# POO

# Modules importation
# -------------------
import os
import json
import random
import Models.Game as Game
import Models.Player as Player
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
PlayerName = Player.GetPlayerData()

# Say welcome
Game.SayWelcome()


# 2) Initialize Maze
Maze.Initialize()
# Load maze elements from json file
Maze.LoadElementsFromFile()
# Load maze from text file
Maze.LoadMapFromFile()

# Put objects in random positions
Maze.PlaceObjectsAtRandomPositions()

# Place player in maze
Player.PlaceInMaze()

# Draw maze on screen
Maze.DrawOnScreen()

# Start game
Game.StartGame()


# 3) Game loop

# Variable for end of game
EndOfGame: bool = False

# Do this until end of game is triggered
while not EndOfGame:

    # Wait for a player action
    PlayerAction: str = Player.WaitForAction()

    # Do action
    EndOfGame = Player.ExecuteAction(PlayerAction)
