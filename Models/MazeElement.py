import os
import json

class MazeElement:
    """
        Used to manage elements compozing the maze

        Not instanciable
    """


    @staticmethod
    def LoadElementsFromFile(Maze):
        """ 
            Load maze elements from json file and store them into list of dictionaries
        """

        # try/exception block to trap errors
        try:
            # Open JSON file in read mode (and automatically close it when finished)
            with open(Maze.FilePath + Maze.FileName + " Elements.json", "r", encoding='utf-8') as MyFile:
                # Load them into maze elements list of dictionary
                Maze.Elements = json.load(MyFile)
                #print(MazeElements)

            # # Code sample to write to JSON file
            # # Open JSON file in write mode (and automatically close it when finished)
            # with open("MazeElements.json", "w", encoding="utf-8") as WriteFile:
            #     # Write to file using proper ascii encoding (with accents) and indentation
            #     json.dump(MazeElements, WriteFile, ensure_ascii=False, indent=4)

        except OSError:
            # If there is an OSError exception
            print("\nLes éléments du labyrinthe demandé n'ont pas été trouvés !\n")
            # exit application
            os._exit(1)

    
    @staticmethod
    def GetElement(
        Maze,
        Name: str = "",
        Symbol: str = "",
        Image: str = "") -> {}:
        """ 
            Return a maze element by its name, symbol or image or None if none matches

            :param arg1: The maze
            :type arg1: Maze
            :param arg2: The element name
            :type arg2: string
            :param arg3: The element symbol
            :type arg3: string
            :param arg4: The element image
            :type arg4: string

            :return: The element (dictionary of all its properties)
            :rtype: dictionary
        """

        # # Alternative syntax with list comprehension
        # return next((ME for ME in MazeElements if ME["Symbol"] == Symbol), None)

        # Browse all elements to find the matching one
        for CurrentElement in Maze.Elements:
            if(Name != "" and CurrentElement["Name"] == Name):
                return CurrentElement
            elif(Symbol != "" and CurrentElement["Symbol"] == Symbol):
                return CurrentElement
            elif(Image != "" and CurrentElement["Image"] == Image):
                return CurrentElement

        # If no element matches, return none (null/nothing)
        return None
