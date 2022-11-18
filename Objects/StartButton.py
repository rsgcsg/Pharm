from GameFrame import RoomObject

class StartButton(RoomObject):
    def __init__ (self,room,x,y):
        RoomObject.__init__(self,room,x,y)

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
        print(self.image13)
        self.set_image(self.image1,200,200)
        self.handle_mouse_events = True
        self.curr_img = 0
        self.set_timer(5, self.update_image)


    def update_image(self):
        self.curr_img += 1
        if self.curr_img %13== 0:
            self.set_image(self.image1, 200, 200)
        elif self.curr_img %13== 1:
            self.set_image(self.image2, 200, 200)
        elif self.curr_img %13== 2:
            self.set_image(self.image3, 200, 200)
        elif self.curr_img %13== 3:
            self.set_image(self.image4, 200, 200)
        elif self.curr_img %13== 4:
            self.set_image(self.image5, 200, 200)
        elif self.curr_img %13== 5:
            self.set_image(self.image6, 200, 200)
        elif self.curr_img %13== 6:
            self.set_image(self.image7, 200, 200)
        elif self.curr_img %13== 7:
            self.set_image(self.image8, 200, 200)
        elif self.curr_img %13== 8:
            self.set_image(self.image9, 200, 200)
        elif self.curr_img %13== 9:
            self.set_image(self.image10, 200, 200)
        elif self.curr_img %13== 10:
            self.set_image(self.image11, 200, 200)
        elif self.curr_img %13== 11:
            self.set_image(self.image12, 200, 200)
        elif self.curr_img %13== 12:
            self.set_image(self.image13, 200, 200)
        self.set_timer(2, self.update_image)

    def clicked (self,button_number):
        self.room.running=False
