
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
