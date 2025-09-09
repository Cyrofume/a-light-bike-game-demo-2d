import pygame


#intialization here...
pygame.init()

#provide window dimension as tuple
screen = pygame.display.set_mode((640,640))

#surfaces is the dimention of a image in memory
#load a image that can become your world/game surface
#and then convert to match a size
bike_img = pygame.image.load('../images/random-bike-pic.webp').convert()

#transforms, more in docuemntations
bike_img = pygame.transform.scale(bike_img, (bike_img.get_width() * 2, bike_img.get_height() * 2))

#run the program
running = True

#having a clock we can hold a image for a certain amout of time based on frame rate
clock = pygame.time.Clock()


#we will use the x coord to determine position
x = 0
#to detect appropriate frame rate we calculate delta
delta_time = 0.1

#simple program to close when click x
while running:
    # print("running")
    #here I made a mistake, I was filling on top of the images
    #here I fill, then add a image to a new dimension
    screen.fill((255, 255, 255))
    #move our image into the window
    screen.blit(bike_img, (x, 30))
    #using fill we can refresh a image, either the image or window, we will go window
    # screen.fill((255, 255, 255))

    #to move the image we will move a value x
    x += 25 * delta_time

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

pygame.quit()