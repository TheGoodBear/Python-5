import os

class Maze:
    """
        Used to manage the maze

        Instanciable
    """

    def __init__(self, 
        FilePath: str = "Mazes/", 
        FileName: str = "Maze 1"):
        """
            Constructor

            :param arg1: Maze file path
            :type arg1: string
            :param arg2: Maze file name
            :type arg2: string
        """
        self.FilePath: str = FilePath
        self.FileName: str = FileName
        self.Maze = list()
        self.MazeElements = list()


    def LoadMazeFromFile(self):
        """ 
            Load maze from text file and store it into a 2 dimensional list
        """

        # try/exception block to trap errors
        try:
            # Open file in read mode (and automatically close it when finished)
            with open(self.MazeFilePath + self.FileName + ".maz", "r") as MyFile:
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
                            CurrentElement = GetMazeElement(Symbol=Character)
                            if(CurrentElement != None):
                                # If an element was found, append element's image
                                LineCharacters.append(CurrentElement["Image"])
                            else:
                                # If no element was found append character
                                LineCharacters.append(Character)
                    # Store LineCharacters list in Maze list (2 dimensional list)
                    Maze.append(LineCharacters)

        except OSError:
            # If there is an OSError exception
            print("\nLe labyrinthe demandé n'a pas été trouvé !\n")
            # exit application
            os._exit(1)

