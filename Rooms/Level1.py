import pygame
import math
from GameFrame import Level
from GameFrame import TextObject
from GameFrame import Globals
from Objects.items import hens,plantAttacker
from Objects.drops import woodBoard,positionDisplay
from Objects.card import card,henCard,plantAttackerCard,sell
class Level1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self,screen, joysticks)
        self.itemDict={"sell":[0,0,0,0],"hens":[hens,50,160,120],"plantAttacker":[plantAttacker,100,160,120]}
        self.set_background_image("background.png")
        self.items={}
        self.items=locals()
        self.cardList=[henCard,plantAttackerCard]
        self.locationData=[[0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,0]]

        Globals.money=10000
        self.add_room_object(woodBoard(self,15,15))
        self.moneyLeft=TextObject(self, 35, 40, '$%s'%(Globals.money),20,'Comic Sans MS',(230, 50, 30),True)
        self.add_room_object(self.moneyLeft)
        self.addCard()
        self.preBlock={}
        self.add_room_object(sell(self,750,3))
    def addCard(self):

        for cardNumber in range(0,len(self.cardList)):
            self.add_room_object(self.cardList[cardNumber](self,160+72*cardNumber,3))
    def catch_events(self,events):
        for event in events:
            if event.type==1:
                self.moneyLeft.text=('$%s'%(Globals.money))
                self.moneyLeft.update_text()
            if event.type==2:
                if Globals.itemName=="sell":
                    if self.locationData[self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[1]][self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[0]]!=0:
                        self.delete_object(self.items[str(self.locationData[self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[1]][self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[0]])+"_"+str(self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[1])+"_"+str(self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[0])])
                        Globals.money+=math.floor(self.itemDict[str(self.locationData[self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[1]][self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[0]])][1]/2)
                        self.moneyLeft.text=('$%s'%(Globals.money))
                        self.moneyLeft.update_text()
                        self.locationData[self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[1]][self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[0]]=0

                elif Globals.money>=self.itemDict[Globals.itemName][1]:

                    if self.addItem(Globals.itemName,
                    self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[0],
                    self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[1]) ==True:
                        Globals.money-=self.itemDict[Globals.itemName][1]
                        self.moneyLeft.text=('$%s'%(Globals.money))
                        self.moneyLeft.update_text()

            if event.type==3:
                if pygame.mouse.get_pressed(3)[0]==True:
                    if (pygame.mouse.get_pos()[0] in range(150,850) and pygame.mouse.get_pos()[1] in range(125,475)) and Globals.money>=self.itemDict[Globals.itemName][1]:
                        currentBlock = positionDisplay(self,
                        self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[0]*70+150,
                        self.findLocation(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])[1]*70+125)
                        self.add_room_object(currentBlock)
                        self.delete_object(self.preBlock)
                        self.preBlock=currentBlock
                    else:
                        self.delete_object(self.preBlock)
                else:
                    self.delete_object(self.preBlock)



    def addItem(self,item,x,y):
        if self.locationData[y][x]==0:
            self.items[str(item)+"_"+str(y)+"_"+str(x)]=self.itemDict[item][0](self,self.itemDict[item][2]+70*x,self.itemDict[item][3]+70*y)
            self.add_room_object(self.items[str(item)+"_"+str(y)+"_"+str(x)])
            self.locationData[y][x]=str(item)
            return True


    def findLocation(self,x,y):
        locationX=math.floor((x-150)/70)
        locationY=math.floor((y-125)/70)
        return locationX,locationY
