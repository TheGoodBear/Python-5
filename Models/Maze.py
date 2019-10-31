import os
import random
import Models.MazeElement as ME

class Maze:
    """
        Used to manage the maze

        Instanciable
    """

    FilePath: str = ""
    FileName: str = ""
    Map = list()
    Elements = list()


    @staticmethod
    def Initialize( 
        FilePath: str = "Mazes/", 
        FileName: str = "Maze 1"):
        """
            Constructor

            :param arg1: Maze file path
            :type arg1: string
            :param arg2: Maze file name
            :type arg2: string
        """
        FilePath: str = FilePath
        FileName: str = FileName


    @classmethod
    def LoadFromFile(cls):
        """ 
            Load maze from text file and store it into a 2 dimensional list
        """

        # try/exception block to trap errors
        try:
            # Open file in read mode (and automatically close it when finished)
            with open(cls.MazeFilePath + cls.FileName + ".maz", "r") as MyFile:
                for Line in MyFile:
                    # Ignore blank lines and comments
                    if(Line[0] == "\n" or Line[0] == "#"):
                        continue
                    # Define temporary list to store every character in a line
                    LineCharacters = list()
                    # For each Character in Line
                    for Character in Line:
                        # Store Character in LineCharacters list (except new line \n)
                        if (Character != "\n"):
                            # Search in maze elements for matching symbol
                            CurrentElement = ME.GetElement(Symbol=Character)
                            if(CurrentElement != None):
                                # If an element was found, append element's image
                                LineCharacters.append(CurrentElement["Image"])
                            else:
                                # If no element was found append character
                                LineCharacters.append(Character)
                    # Store LineCharacters list in Maze list (2 dimensional list)
                    Map.append(LineCharacters)

        except OSError:
            # If there is an OSError exception
            print("\nLe labyrinthe demandé n'a pas été trouvé !\n")
            # exit application
            os._exit(1)


    @classmethod
    def PlaceObjectsAtRandomPositions(cls):
        """ 
            Place all objects from dictionary at random positions in maze
        """

        # Use global Maze variable
        global Maze

        # Browse every maze element
        for CurrentObject in cls.Elements:
            if("Pick" in CurrentObject["Behavior"]):
                # the current object is pickable
                # draw random coordinates in maze limits
                ObjectX: int = random.randint(0, len(Maze)-1)
                ObjectY: int = random.randint(0, len(Maze[0])-1)
                while(Maze[ObjectY][ObjectX] != ME.GetElement("Sol")["Image"]):
                    # do it again until random position is ground
                    ObjectX = random.randint(0, len(Maze)-1)
                    ObjectY = random.randint(0, len(Maze[0])-1)
                # place current object at this position (replace the ground with it)
                Maze[ObjectY][ObjectX] = CurrentObject["Image"]


    @staticmethod
    def DrawOnScreen():
        """ 
            Draw maze in console
            Including player
        """

        # Prints a blank line
        print()

        # With simple loop (gives only the content)
        # For each line (Y) in Maze
        for Line in Map:
            # For each character (X) in line
            for Column in Line:
                # Print current maze element at Y, X without jumping a line
                print(Column, end="")
            # Jump a line for new Y
            print()
        
        # # With range and len (gives only the coordinates)
        # # For each line (Y) in Maze
        # for Y in range(len(Maze)):
        #     # For each character (X) in line
        #     for X in range(len(Maze[Y])):
        #         # Print current maze element at Y, X without jumping a line
        #         print(Maze[Y][X], end="")
        #     # Jump a line for new Y
        #     print()
        
        # # With enumerate (gives the content and the coordinates)
        # # For each line (Y) in Maze
        # for Y, Line in enumerate(Maze):
        #     # For each character (X) in line
        #     for X, Column in enumerate(Maze[Y]):
        #         # Print current maze element at Y, X without jumping a line
        #         print(Maze[Y][X], end="")
        #     # Jump a line for new Y
        #     print()

