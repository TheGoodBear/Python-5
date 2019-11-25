import os
import json
#from Models.Maze import *

class MazeElement:
    """
        Used to manage elements compozing the maze

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
            Return a maze element by its name, symbol or image

            :param arg1: The element name
            :type arg1: string
            :param arg2: The element symbol
            :type arg2: string
            :param arg3: The element image
            :type arg3: string

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
