from GameFrame import Level
from Objects import StartButton
class StartRoom(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self,screen, joysticks)
        self.set_background_image("StartRoom.png")
        self.add_room_object(StartButton(self,400,250))
