import pygame


#we want the bike to run in a grid like platform
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED =  (255,0,0)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

START_Y = 190

BIKE_WIDTH = 1
BIKE_HEIGHT = 1

#controls pf prev
# local prev = None
def start():
    #global vars
    global screen, clock
    #intialization here...
    pygame.init()

    #provide window dimension as tuple
    #lets use the window screen constants as our world

    # screen = pygame.display.set_mode((640,640))
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    #surfaces is the dimention of a image in memory
    #load a image that can become your world/game surface
    #and then convert to match a size
    bike_img = pygame.image.load('../images/random-bike-pic.webp').convert()

    #transforms, more in docuemntations
    bike_img = pygame.transform.scale(bike_img, (BIKE_WIDTH, BIKE_HEIGHT))

    #run the program
    running = True

    #having a clock we can hold a image for a certain amout of time based on frame rate
    clock = pygame.time.Clock()


    #we will use the x coord to determine position
    # x = 0
    #to detect appropriate frame rate we calculate delta
    delta_time = 0.1

    #set the image as a player
    # p = GameObject(bike_img, x, START_Y)
    x = LightBikeObject(bike_img, 20, 1)
    moves = [x.move(up=True),x.move(down=True),x.move(left=True),x.move(right=True)]
    prev = 3 #what if 0 = False...
    # print(prev)
    #simple program to close when click x
    while running:
        # local prev
        # print("running")
        #here I made a mistake, I was filling on top of the images
        #here I fill, then add a image to a new dimension
        # screen.fill((255, 255, 255))
        drawGrid()
        #move our image into the window
        # screen.blit(bike_img, (x, START_Y))
        #using fill we can refresh a image, either the image or window, we will go window
        # screen.fill((255, 255, 255))
        # print(pygame.surf)
        
        
        #to move the image we will move a value x
        # x += 25 * delta_time
        #previous move set
        # prev
        # x.move(right=True)
        
        #wsad control
        keys = pygame.key.get_pressed()
        # print(keys)
        prevX, prevY, _, _ = x.pos
        if keys != None:
            # print(keys[pygame.K_DOWN])
            # keys = pygame.key.get_pressed()
            # prev = keys
            if keys[pygame.K_UP]:
                # prev = 0
                x.move(up=True)
                # prev = x.move(up=True)
                
            if keys[pygame.K_DOWN]:
                x.move(down=True)
                # prev = x.move(down=True)
                # prev = 1
            if keys[pygame.K_LEFT]:
                x.move(left=True)
                # prev = x.move(left=True)
                # prev = 2
            if keys[pygame.K_RIGHT]:
                x.move(right=True)
                # prev = x.move(right=True)
                # prev = 3
            if keys[pygame.K_SPACE]:
                x.move(space=True)
                #lets make our speed faster fora bit
                pass
            # prev
        if keys[pygame.K_DOWN] == False and keys[pygame.K_UP] == False and keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
            # print(moves)
            x.move()
            pass
        # print(prev)
        # print(moves[1](up))
            # print(prev)
            # if prev != None:
            #     prev()
            # else:
            #     x.move(right=True)
        # else:
            # if prev != None:
            #     prev
            # else:
            #     x.move(right=True)
            # prev if prev else x.move(right=True)
            # if prev == None:
        # # x.move(right=True)
            # if prev[pygame.K_UP]:
            #     x.move(up=True)
            # if prev[pygame.K_DOWN]:
            #     x.move(down=True)
            # if prev[pygame.K_LEFT]:
            #     x.move(left=True)
            # if prev[pygame.K_RIGHT]:
            #     x.move(right=True)
            # if prev == None:
            #     x.move(right=True)

        #we need to check before moving it right?
        currX, currY, _, _ = x.pos
        # pygame.Surface.get_at(currX, currY)
        # print(pygame.Surface.get_at([currX, currY])
        # print(screen.get_at((currX, currY)))
        if screen.get_at((currX, currY)) == (255, 255, 255, 255):
            print("touched white?")
            x.kill()
        else:
            # print("not")
            pass
        # lightBikeX, lightBikeY, _ _ = LightBikeObject.pos()
        # print(LightBikeObject)
        # if is_collision(prevX, prevY, currX, currY):
        # if is_collision(currX, currY, LightBikeObject.pos, currY):
            # print("collision occured")
        #now update the item
        screen.blit(x.image, x.pos)
        
        # x.pos += 25 * delta_time
        #now how do I update it so it always move what ever direction?
        #did this above, now how do I determine when to kill the bike?
        # if is_collision(x.pos)
        # print(x.pos)


        #read event documentation for more info
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#this Constant name is upper and exact to work
                running = False
            #add a feature to pause or play again

        #call display.flip to render and continue having the image loaded before
        pygame.display.flip()
        #call clock.tick() and some number in the parameter with desired framerate default 60..
        #calculate new delta time
        delta_time = clock.tick(60) / 1000
        delta_time = max(0.001, min(0.1, delta_time)) #take consideration of bounds incase of stuttering

        #update?
        # pygame.display.update()
    pygame.quit()

def main():
    # print("hello")
    start()
    # pass
def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, RED, rect, 1)

#find when two pixels are metting for the first time
# def is_collision(x1,y1,x2,y2):
#     # if x1 >= x2 + bikesize + 
#     #logic for something ahead of us
#     # if y1 >= y2 and y1 <= y2 + 1:
#     #     if x1 >= x2 and x1 <= x2 + 1:
#     if x1 >= x2 and x1 <= x2 + 1:
#         if y1 >= y2 and y1 <= y2 + 1:
#             return True 


class LightBikeObject:

    prev = 3
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    # def move(self):
    #     self.pos = self.pos.move(self.speed, 0)
    #     if self.pos.right > 600: #what dose this mean?
    #         self.pos.left = 0



    #we need to move our object based on keyboard keys
    def move(self, up=False, down=False, left=False, right=False, space=False):
        #these are the rules if any of the arrows keys are used
        if right:
            # print("pressing right")
            self.pos.right += self.speed
            self.prev = 3
        if left:
            self.pos.right -= self.speed
            self.prev = 2
        if down:
            self.pos.top += self.speed
            self.prev = 1
        if up:
            self.pos.top -= self.speed
            self.prev = 0
        #this rule is a idle rule, to always move based on the previous or default comd
        #python has the javascript syntax, where False != 0 != not
        #using not and 0 fails the same condition below
        if up==False and down==False and left==False and right==False:
            # print("idle")
            if self.prev == 3:
            # print("pressing right")
                self.pos.right += self.speed
                # prev = 3
            if self.prev == 2:
                self.pos.right -= self.speed
                # prev = 2
            if self.prev == 1:
                self.pos.top += self.speed
                # prev = 1
            if self.prev == 0:
                self.pos.top -= self.speed
            # self.pos.right += self.speed
        #these are the rules it falls on the grid

        #speed up is a new mode added
        if space:
            print("space added")
            self.speed = 1 * 1.01;
        # else:
        #     self.speed = 20
        if self.pos.right > WINDOW_WIDTH:
            self.pos.left = 0
        if self.pos.top > WINDOW_HEIGHT-BIKE_HEIGHT:
            self.pos.top = 0
        if self.pos.right < BIKE_WIDTH:
            self.pos.right = WINDOW_WIDTH
        if self.pos.top < 0:
            self.pos.top = WINDOW_HEIGHT-BIKE_HEIGHT
        
    def kill(self):
        self.prev = -1
        self.speed = 0
#we need to create a class for our object
# def LightBikeObject:


if __name__ == "__main__":
    main()
