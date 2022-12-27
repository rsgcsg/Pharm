from GameFrame import RoomObject,Globals
import pygame
import math
class card(RoomObject):
    def __init__ (self,room,x,y):
        RoomObject.__init__(self,room,x,y)
        self.x=x
        self.y=y
        self.handle_mouse_events = True
        self.initialX=-1
        self.initialY=-1


    def postPlantEvent(self):
        plantEvent = pygame.event.Event(2)
        pygame.event.post(plantEvent)
    def update(self):
        if Globals.itemData[0]!=self.itemName:
            self.set_image(self.image1,self.width,self.height)
        else:
            self.set_image(self.image2,self.width,self.height)

    def clicked(self, button_number):
        if Globals.itemData[0] != self.itemName:
            Globals.itemData[0] = self.itemName
        else:
            Globals.itemData[0] = 0
    def mouse_event(self, mouse_x, mouse_y, button_left, button_middle, button_right):
        positionX=-1
        positionY=-1
        if Globals.itemData[0]!=0:
            if mouse_x in range(150,850) and mouse_y in range(125,475):
                if button_left==True:
                    Globals.plantMode=True
                    positionX=math.floor((mouse_x-150)/70)
                    positionY=math.floor((mouse_y-125)/70)

                else:
                    if Globals.plantMode==True:
                        Globals.itemData[1] = self.initialX
                        Globals.itemData[2] = self.initialY
                        pygame.event.pump()
                        Event=pygame.event.Event(3)
                        pygame.event.post(Event)
                        self.set_timer(2,self.postPlantEvent)
                        self.initialX = positionX
                        self.initialY = positionY
                        Globals.plantMode=False
            else:
                Globals.plantMode=False
                pygame.event.pump()
                Event=pygame.event.Event(3)
                pygame.event.post(Event)
                self.initialX=positionX
                self.initialY=positionY

            if self.initialX != positionX or self.initialY != positionY:
                pygame.event.pump()
                Event=pygame.event.Event(3)
                pygame.event.post(Event)
                self.initialX=positionX
                self.initialY=positionY
class henCard(card):
    def __init__ (self,room,x,y):
        RoomObject.__init__(self,room,x,y)
        self.itemName="hens"
        self.image1=self.load_image("henCard.png")
        self.image2=self.load_image("henCard2.png")
        self.set_image(self.image1,57,76)
        self.handle_mouse_events = True
        self.initialX=-1
        self.initialY=-1
        self.width=66
        self.height=88
        self.x=x
        self.y=y


class plantAttackerCard(card):
    def __init__ (self,room,x,y):
        RoomObject.__init__(self,room,x,y)
        self.itemName="plantAttacker"
        self.image1=self.load_image("plantAttackerCard.png")
        self.image2=self.load_image("plantAttackerCard2.png")
        self.set_image(self.image1,57,76)
        self.handle_mouse_events = True
        self.initialX=-1
        self.initialY=-1
        self.width=66
        self.height=88
        self.x=x
        self.y=y

class sell(card):
    def __init__ (self,room,x,y):
        RoomObject.__init__(self,room,x,y)
        self.itemName="sell"
        self.image1=self.load_image("sell.png")
        self.image2=self.load_image("sell2.png")
        self.set_image(self.image1,76,76)
        self.handle_mouse_events = True
        self.initialX=-1
        self.initialY=-1
        self.width=80
        self.height=80
        self.x=x
        self.y=y
