from GameFrame import Globals,TextObject,RoomObject
import pygame
class drops(RoomObject):
    def __init__(self, room,x,y):
        RoomObject.__init__(self, room,x,y)
class eggs(drops):
    def __init__(self, room,x,y):
        drops.__init__(self, room,x,y)
        self.image=self.load_image("egg.png")
        self.set_image(self.image,15,16.5)
        self.x_speed = -10
        self.y_speed = 2
        self.set_timer(3,self.blocked)
        self.handle_mouse_events = True
        self.set_timer(200,self.sell)
        self.depth=0
    def sell(self):
        self.room.delete_object(self)
        pygame.event.pump()
        self.moneyUpdate=pygame.event.Event(1)
        Globals.money+=25
        pygame.event.post(self.moneyUpdate)
    def clicked(self,button_number):
        self.sell()
class woodBoard(drops):
    def __init__(self, room,x,y):
        drops.__init__(self, room,x,y)
        self.image=self.load_image("woodBoard.png")
        self.set_image(self.image,120,80)
        self.depth=-1
class positionDisplay(drops):
    def __init__(self, room,x,y):
        drops.__init__(self, room,x,y)
        self.image=self.load_image("positionDisplay.png")
        self.set_image(self.image,70,70)
        self.depth=0
class peas(drops):
    def __init__(self, room,x,y):
        drops.__init__(self, room,x,y)
        self.image=self.load_image("peas.png")
        self.set_image(self.image,15,15)
        self.depth=2
        self.x_speed = 15
