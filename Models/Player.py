
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


    pass