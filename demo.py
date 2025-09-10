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
prev = None
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

    #simple program to close when click x
    while running:
        # print("running")
        #here I made a mistake, I was filling on top of the images
        #here I fill, then add a image to a new dimension
        # screen.fill((255, 255, 255))
        drawGrid()
        #move our image into the window
        # screen.blit(bike_img, (x, START_Y))
        #using fill we can refresh a image, either the image or window, we will go window
        # screen.fill((255, 255, 255))

        #to move the image we will move a value x
        # x += 25 * delta_time
        #previous move set
        
        #wsad control
        if pygame.key.get_pressed():
            
            keys = pygame.key.get_pressed()
            prev = keys
            if keys[pygame.K_UP]:
                x.move(up=True)
            if keys[pygame.K_DOWN]:
                x.move(down=True)
            if keys[pygame.K_LEFT]:
                x.move(left=True)
            if keys[pygame.K_RIGHT]:
                x.move(right=True)
            
        # else:
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
        # x.move(right=True)

        #now update the item
        screen.blit(x.image, x.pos)
        # x.pos += 25 * delta_time
        #now how do I update it so it always move what ever direction?

        #read event documentation for more info
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#this Constant name is upper and exact to work
                running = False

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
class LightBikeObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    # def move(self):
    #     self.pos = self.pos.move(self.speed, 0)
    #     if self.pos.right > 600: #what dose this mean?
    #         self.pos.left = 0



    #we need to move our object based on keyboard keys
    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed
        if self.pos.right > WINDOW_WIDTH:
            self.pos.left = 0
        if self.pos.top > WINDOW_HEIGHT-BIKE_HEIGHT:
            self.pos.top = 0
        if self.pos.right < BIKE_WIDTH:
            self.pos.right = WINDOW_WIDTH
        if self.pos.top < 0:
            self.pos.top = WINDOW_HEIGHT-BIKE_HEIGHT
#we need to create a class for our object
# def LightBikeObject:


if __name__ == "__main__":
    main()
