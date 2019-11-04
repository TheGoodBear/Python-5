import Models.Player as Player
import Models.MazeElement as MazeElement

class Game:
    """
        Utility class used to manage the game

        Not instanciable
        Static methods only
    """


    @staticmethod
    def ApplicationStart():
        """ 
            Initialize application and show initial message
        """

        print("\nBonjour humain, merci de t'identifier afin que je puisse interagir avec toi.")


    @staticmethod
    def StartGame():
        """ 
            Give rules to player
        """

        print(
            "\nTon objectif est de sortir du labyrinthe." + 
            "\nPour cela il te faudra trouver la sortie et avoir collecté les objets nécessaires à l'ouverture de la porte." + 
            "\nTu es représenté par {0} et la porte de sortie par {1}.".format(Player.Image, MazeElement.GetElement("Sortie")["Image"]) + 
            "\nÀ chaque tour tu peux effectuer l'une des actions suivantes :" + 
            "\nTe déplacer vers le (H)aut, le (B)as, la (G)auche, la (D)roite ou (Q)uitter le jeu (et perdre...)" + 
            "\nBonne chance.")
