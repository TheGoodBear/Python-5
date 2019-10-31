import Models.Maze as Maze

class Player:
    """
        Used to manage the player

        Instanciable
    """

    def __init__(self, 
        Name: str = "Anonyme", 
        Image: str = "☻"):
        """
            Constructor

            :param arg1: Player name
            :type arg1: string
            :param arg2: Player image
            :type arg2: string
        """
        self.Name: str = Name
        self.Image: str = Image 
        self.PlayerX: int = 0
        self.PlayerY: int = 0
        self.PlayerBackpack = list()


    @classmethod
    def GetPlayerData(cls):
        """ 
            Get player data

            :return: Player name
            :rtype: string
        """

        Name: str = ""

        # Ask for name until it is filled
        while(Name == ""):
            Name = input("\nMerci d'entrer ton nom : ")

        # Return Name
        cls.Name = Name


    @staticmethod
    def SayWelcome():
        """ 
            Say Welcome to player
        """

        print(
            "\nEnchanté {0}, j'espère que tu vas bien t'amuser." 
            .format(PlayerName))


    @classmethod
    def PlacePlayerInMaze(cls,
        PlayerNewX: int = 0,
        PlayerNewY: int = 0):
        """ 
            Place player in maze

            :param arg1: The new X position of player
            :type arg1: integer
            :param arg2: The new Y position of player
            :type arg2: integer
        """

        # Variables for maze coordinates
        X: int = 0
        Y: int = 0

        # Check if player is not already in the maze (coordinates set to 0)
        if (cls.PlayerX == 0 and cls.PlayerY == 0):
            # In that case put him at the entrance
            # find it by browsing maze list
            for Line in Maze.Map:
                # New line, set X coordinate to 0
                X = 0
                for Character in Line:
                    # If position contains entrance (E)
                    if (Maze[Y][X] == GetMazeElement("Entrée")["Image"]):
                        # Save coordinates for player
                        PlayerX = X
                        PlayerY = Y
                        # Replace entrance with player
                        Maze[Y][X] = PlayerImage
                        # Exit loops (and method)
                        return
                    # Increment X coordinate
                    X += 1
                # Increment Y coordinate
                Y += 1

        else:
            # Player is already in maze
            # replace actual player position with a floor
            Maze[PlayerY][PlayerX] = GetMazeElement("Sol")["Image"]
            # and place player to new position
            Maze[PlayerNewY][PlayerNewX] = PlayerImage


    def WaitForPlayerAction() -> str:
        """ 
            Wait player to make an action

            :return: The name of the action if the action is valid
            :rtype: string
        """

        # Show player backpack content
        print("\nContenu du sac à dos : ", end="")
        if (len(PlayerBackpack) == 0):
            # if backpack is empty (nothing in list)
            print("vide")
        else:
            # if backpack contains at least 1 object (* means every item in list)
            print(*PlayerBackpack, sep=', ')

        # Ask player input until it is a valid action
        while True:
            PlayerInput = input("\nQuelle est ta prochaine action ? ")

            # check if this is a valid action
            # show a message saying what player is doing
            # and return action name if valid
            if (PlayerInput.upper() == "H"):
                print("Tu te déplaces vers le haut...")
                return "MoveUp"
            elif (PlayerInput.upper() == "B"):
                print("Tu te déplaces vers le bas...")
                return "MoveDown"
            elif (PlayerInput.upper() == "G"):
                print("Tu te déplaces vers la gauche...")
                return "MoveLeft"
            elif (PlayerInput.upper() == "D"):
                print("Tu te déplaces vers la droite...")
                return "MoveRight"
            elif (PlayerInput.upper() == "Q"):
                print("Tu choisis de quitter le labyrinthe, tu as perdu !\n")
                return "QuitGame"
            else:
                print("Cette action n'est pas reconnue.")


    def ExecutePlayerAction(PlayerAction: str) -> bool:
        """ 
            Execute player action and returns new position

            :param arg1: The action
            :type arg1: string

            :return: If this is the end of the game
            :rtype: boolean
        """

        # Use global variables
        global PlayerX, PlayerY

        # Variables for new player coordinates
        PlayerNewX: int = PlayerX
        PlayerNewY: int = PlayerY

        # Calculate player new coordinates
        if (PlayerAction == "MoveUp"):
            PlayerNewY -= 1
        elif (PlayerAction == "MoveDown"):
            PlayerNewY += 1
        elif (PlayerAction == "MoveLeft"):
            PlayerNewX -= 1
        elif (PlayerAction == "MoveRight"):
            PlayerNewX += 1
        elif (PlayerAction == "QuitGame"):
            # If action is QuitGame then return game end
            return True


        # Check if new coordinates are valid (into maze limits)
        if (PlayerNewX<0 or 
            PlayerNewX>len(Maze[0]) or 
            PlayerNewY<0 or 
            PlayerNewY>len(Maze)):
            # if player is out of maze limits
            print("Tu es en dehors des limites, tu ne peux pas aller par là !")
            # redraw maze
            DrawMazeOnScreen()
            return False

        # Get current maze element at new player coordinates
        CurrentElement = GetMazeElement(Image=Maze[PlayerNewY][PlayerNewX])

        # Check current element behavior or name
        if (CurrentElement["Name"] == "Sortie"):
            # If exit is reached
            # check if player has all needed objects
            MissingObjects: int = 0
            # for each element in maze
            for Element in MazeElements:
                if ("Combine" in Element["Behavior"]
                    and not Element["Name"] in PlayerBackpack):
                    # this element can be combined but is not in player backpack
                    MissingObjects += 1
            if (MissingObjects == 0):
                # player has all objects
                # replace player in maze
                PlacePlayerInMaze(PlayerNewX,PlayerNewY)
                # assign new coordinates to player
                PlayerX = PlayerNewX
                PlayerY = PlayerNewY
                # redraw maze with new player position
                DrawMazeOnScreen()
                # say victory
                print(
                    "\nOuiiii, bravo {0}, tu as trouvé la sortie et tu avais tous les objets nécessaires !\n"
                    .format(PlayerName))
                # and return game end
                return True
            else:
                # some objects are missing
                # say how many
                print(
                    "\nHa, tu as bien trouvé la sortie mais il te manque encore {0} objet(s) pour ouvrir la porte..."
                    .format(MissingObjects))
        
        elif ("Block" in CurrentElement["Behavior"]):
            # If there is an obstacle, say it
            print("Oups un mur, tu ne peux pas bouger !")
            # and redraw maze
            DrawMazeOnScreen()
        
        elif ("Pick" in CurrentElement["Behavior"]):
            # If there is an object, put it in backpack
            PlayerBackpack.append(CurrentElement["Name"])
            # say it
            print(
                "Chouette, tu as trouvé un(e) {0}\n"
                .format(CurrentElement["Name"]))
            # remove it from maze (put floor at its place)
            Maze[PlayerNewY][PlayerNewX] = GetMazeElement("Sol")["Image"]
            # replace player in maze
            PlacePlayerInMaze(PlayerNewX,PlayerNewY)
            # assign new coordinates to player
            PlayerX = PlayerNewX
            PlayerY = PlayerNewY
            # and redraw maze with new player position
            DrawMazeOnScreen()
            
        else:
            # If nothing special
            # replace player in maze
            PlacePlayerInMaze(PlayerNewX,PlayerNewY)
            # assign new coordinates to player
            PlayerX = PlayerNewX
            PlayerY = PlayerNewY
            # and redraw maze with new player position
            DrawMazeOnScreen()

        # Game is not yet ended    
        return False
