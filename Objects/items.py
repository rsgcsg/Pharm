from GameFrame import RoomObject
from Objects.drops import eggs,peas
import itertools
class items(RoomObject):
    def __init__(self, room,x,y):
        RoomObject.__init__(self, room,x,y)
        self.depth=1
        self.HP=0

    def updateImage(self):
        self.set_image(self.animatedLists[self.animeListState]["pictureList"][self.pictureState],
                           self.animatedLists[self.animeListState]["width"],
                           self.animatedLists[self.animeListState]["height"])

    def animated(self):
        if self.pictureState!=len(self.animatedLists[self.animeListState]["pictureList"])-1:
            self.updateImage()
            self.pictureState+=1
            self.set_timer(self.animatedLists[self.animeListState]["loopTime"],self.animated)
        else:
            if self.pictureLoopNumber!=self.animatedLists[self.animeListState]["loopNumber"]-1:
                self.updateImage()
                self.pictureLoopNumber+=1
                self.pictureState=0
                self.set_timer(self.animatedLists[self.animeListState]["loopTime"],self.animated)
            else:
                self.updateImage()
                self.pictureLoopNumber=0
                self.pictureState=0
                self.finishLoop()
    def update(self):
        if self.HP <=0:
            self.room.delete_object(self)
class hens(items):
    def __init__(self, room,x,y):
        items.__init__(self, room,x,y)
        self.image1 = self.load_image('hen-1.png')
        self.image2 = self.load_image('hen-2.png')
        self.image3 = self.load_image('hen-3.png')
        self.image4 = self.load_image('hen-4.png')
        self.image5 = self.load_image('hen-5.png')
        self.image6 = self.load_image('hen-6.png')
        self.image7 = self.load_image('hen-7.png')
        self.image8 = self.load_image('hen-8.png')
        self.image9 = self.load_image('hen-9.png')
        self.image10 = self.load_image('hen-10.png')
        self.image11 = self.load_image('hen-11.png')
        self.image12 = self.load_image('hen-12.png')
        self.image13 = self.load_image('hen-13.png')
        self.set_image(self.image1,50,50)
        self.HP=100
        self.animeListState="list1"
        self.pictureState=0
        self.pictureLoopNumber=0
        self.animatedLists={"list1":{"width":50,"height":50,"loopTime":4,"loopNumber":-1,"pictureList":[self.image1,self.image1,self.image2,self.image3,self.image7,self.image8,self.image10,self.image12,self.image13]},
                            "list2":{"width":50,"height":50,"loopTime":3,"loopNumber":1,"pictureList":[self.image1,self.image2,self.image3,self.image4,self.image4,self.image4,self.image4,self.image4,self.image4,self.image5,self.image5,self.image5,self.image5,self.image5,self.image5,self.image6,self.image7,self.image8,self.image10,self.image12,self.image13]}}
        self.animated()
        self.set_timer(500,self.layEgg)
    def finishLoop(self):
        self.animeListState="list1"
        self.pictureState=0
        self.pictureLoopNumber=0
        self.animated()
    def newEgg(self):
        New_egg=eggs(self.room,self.x+20,self.y+30)
        self.room.add_room_object(New_egg)
    def layEgg(self):
        self.animeListState="list2"
        self.pictureState=0
        self.pictureLoopNumber=0
        self.set_timer(35,self.newEgg)
        self.set_timer(500,self.layEgg)

class plantAttacker(items):
    def __init__(self, room,x,y):
        items.__init__(self, room,x,y)
        self.image1 = self.load_image('plantAttacker-1.png')
        self.image2 = self.load_image('plantAttacker-2.png')
        self.image3 = self.load_image('plantAttacker-3.png')
        self.image4 = self.load_image('plantAttacker-4.png')
        self.image5 = self.load_image('plantAttacker-5.png')
        self.image6 = self.load_image('plantAttacker-6.png')
        self.image7 = self.load_image('plantAttacker-7.png')
        self.image8 = self.load_image('plantAttacker-8.png')
        self.image9 = self.load_image('plantAttacker-9.png')
        self.image10 = self.load_image('plantAttacker-10.png')
        self.image11 = self.load_image('plantAttacker-11.png')
        self.set_image(self.image1,50,50)
        self.animeListState="list1"
        self.HP=100
        self.pictureState=0
        self.pictureLoopNumber=0
        self.animatedLists={"list1":{"width":50,"height":50,"loopTime":3,"loopNumber":-1,"pictureList":[self.image9,self.image9,self.image10,self.image11,self.image11]},
                            "list2":{"width":50,"height":50,"loopTime":3,"loopNumber":1,"pictureList":[self.image1,self.image2,self.image3,self.image4,self.image4,self.image5,self.image6,self.image7,self.image8]}}
        self.animated()
        self.set_timer(100,self.attack)
    def finishLoop(self):
        self.animeListState="list1"
        self.pictureState=0
        self.pictureLoopNumber=0
        self.animated()

    def newPea(self):
        New_pea=peas(self.room,self.x+40,self.y+7)
        self.room.add_room_object(New_pea)

    def attack(self):
        self.animeListState="list2"
        self.pictureState=0
        self.pictureLoopNumber=0
        self.set_timer(20,self.newPea)
        self.set_timer(100,self.attack)


