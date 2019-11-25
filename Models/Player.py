#from Models.Maze import *
from Models.MazeElement import *

class Player:
    """
        Used to manage the player

        Instanciable
    """

    Name: str = "Anonyme"
    Image: str = "☻"
    X: int = 0
    Y: int = 0
    Backpack : list()

    #def __init__(self, 
    #    Name: str = "Anonyme", 
    #    Image: str = "☻"):
    #    """
    #        Constructor
    #
    #        :param arg1: Player name
    #        :type arg1: string
    #        :param arg2: Player image
    #        :type arg2: string
    #    """


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


    @classmethod
    def SayWelcome(cls):
        """ 
            Say Welcome to player
        """

        print(
            "\nEnchanté {0}, j'espère que tu vas bien t'amuser." 
            .format(cls.Name))


    @classmethod
    def PlaceInMaze(cls,
        Maze,
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
        if (cls.X == 0 and cls.Y == 0):
            # In that case put him at the entrance
            # find it by browsing maze list
            for Line in Maze.Map:
                # New line, set X coordinate to 0
                X = 0
                for Character in Line:
                    # If position contains entrance (E)
                    if (Maze.Map[Y][X] == MazeElement.GetElement(Maze, "Entrée")["Image"]):
                        # Save coordinates for player
                        cls.X = X
                        cls.Y = Y
                        # Replace entrance with player
                        Maze.Map[Y][X] = cls.Image
                        # Exit loops (and method)
                        return
                    # Increment X coordinate
                    X += 1
                # Increment Y coordinate
                Y += 1

        else:
            # Player is already in maze
            # replace actual player position with a floor
            Maze.Map[cls.Y][cls.X] = MazeElement.GetElement(Maze, "Sol")["Image"]
            # and place player to new position
            Maze.Map[PlayerNewY][PlayerNewX] = cls.PlayerImage


    @classmethod
    def WaitForAction(cls) -> str:
        """ 
            Wait player to make an action

            :return: The name of the action if the action is valid
            :rtype: string
        """

        # Show player backpack content
        print("\nContenu du sac à dos : ", end="")
        if (len(cls.Backpack) == 0):
            # if backpack is empty (nothing in list)
            print("vide")
        else:
            # if backpack contains at least 1 object (* means every item in list)
            print(*cls.Backpack, sep=', ')

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


    @classmethod
    def ExecuteAction(cls,
        Action: str) -> bool:
        """ 
            Execute player action and returns new position

            :param arg1: The action
            :type arg1: string

            :return: If this is the end of the game
            :rtype: boolean
        """

        # Variables for new player coordinates
        PlayerNewX: int = cls.X
        PlayerNewY: int = cls.Y

        # Calculate player new coordinates
        if (Action == "MoveUp"):
            PlayerNewY -= 1
        elif (Action == "MoveDown"):
            PlayerNewY += 1
        elif (Action == "MoveLeft"):
            PlayerNewX -= 1
        elif (Action == "MoveRight"):
            PlayerNewX += 1
        elif (Action == "QuitGame"):
            # If action is QuitGame then return game end
            return True


        # Check if new coordinates are valid (into maze limits)
        if (PlayerNewX<0 or 
            PlayerNewX>len(Maze.Map[0]) or 
            PlayerNewY<0 or 
            PlayerNewY>len(Maze.Map)):
            # if player is out of maze limits
            print("Tu es en dehors des limites, tu ne peux pas aller par là !")
            # redraw maze
            Maze.DrawOnScreen()
            return False

        # Get current maze element at new player coordinates
        CurrentElement = MazeElement.GetElement(Image=Maze[PlayerNewY][PlayerNewX])

        # Check current element behavior or name
        if (CurrentElement["Name"] == "Sortie"):
            # If exit is reached
            # check if player has all needed objects
            MissingObjects: int = 0
            # for each element in maze
            for Element in Maze.Elements:
                if ("Combine" in Element["Behavior"]
                    and not Element["Name"] in cls.Backpack):
                    # this element can be combined but is not in player backpack
                    MissingObjects += 1
            if (MissingObjects == 0):
                # player has all objects
                # replace player in maze
                cls.PlaceInMaze(PlayerNewX,PlayerNewY)
                # assign new coordinates to player
                cls.X = PlayerNewX
                cls.Y = PlayerNewY
                # redraw maze with new player position
                Maze.DrawOnScreen()
                # say victory
                print(
                    "\nOuiiii, bravo {0}, tu as trouvé la sortie et tu avais tous les objets nécessaires !\n"
                    .format(cls.Name))
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
            Maze.DrawOnScreen()
        
        elif ("Pick" in CurrentElement["Behavior"]):
            # If there is an object, put it in backpack
            cls.Backpack.append(CurrentElement["Name"])
            # say it
            print(
                "Chouette, tu as trouvé un(e) {0}\n"
                .format(CurrentElement["Name"]))
            # remove it from maze (put floor at its place)
            Maze.Map[PlayerNewY][PlayerNewX] = MazeElement.GetElement("Sol")["Image"]
            # replace player in maze
            cls.PlaceInMaze(PlayerNewX,PlayerNewY)
            # assign new coordinates to player
            cls.X = PlayerNewX
            cls.Y = PlayerNewY
            # and redraw maze with new player position
            Maze.DrawOnScreen()
            
        else:
            # If nothing special
            # replace player in maze
            cls.PlaceInMaze(PlayerNewX,PlayerNewY)
            # assign new coordinates to player
            cls.X = PlayerNewX
            cls.Y = PlayerNewY
            # and redraw maze with new player position
            Maze.DrawOnScreen()

        # Game is not yet ended    
        return False
