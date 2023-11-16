
import pygame
import random

size = width, height =(1200, 800)
road_w = int(width/1.6)
roadmark_w = int(width/60)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('warm.mp3')
sound.set_volume(0.5)
score = 0

running = True
screen=pygame.display.set_mode((size))
pygame.display.set_caption("Sangay's car game")
screen.fill((60, 220, 0))

# draw graphics
pygame.draw.rect(screen, (50, 50, 50), (width/2-road_w/2, 0, road_w, height))
pygame.draw.rect(screen, (255, 240, 60), (width/2 - roadmark_w/2, 0, roadmark_w, height))
pygame.draw.rect(screen, (255, 255, 255), (width/2 - roadmark_w/2 + roadmark_w*17, 0, roadmark_w, height))
pygame.draw.rect(screen, (255, 255, 255), (width/2 + roadmark_w/2 - roadmark_w*18, 0, roadmark_w, height))

# apply changes
pygame.display.update()

# load player vehicle
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = width/3 + road_w/2, height*0.7

# load enemy vehicle
car2 = pygame.image.load("car2.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2

while running:
    # Animate enemy vehicle
    car2_loc.y += 3
    if car2_loc.y > height:
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    score += 1 

    

    # end game
    if car_loc.colliderect(car2_loc):
      print("GAME OVER! YOU LOST")
      break

    # Event listeners
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key == pygame.K_RIGHT:
                car_loc = car_loc.move([int(road_w/2), 0])
        


    
    
    # Draw graphics
    pygame.draw.rect(screen, (50, 50, 50), (width/2-road_w/2, 0, road_w, height))
    pygame.draw.rect(screen, (255, 240, 60), (width/2 - roadmark_w/2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width/2 - roadmark_w/2 + roadmark_w*17, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width/2 + roadmark_w/2 - roadmark_w*18, 0, roadmark_w, height))
    # Create a font object
    font = pygame.font.Font(None, 50) 
    text = font.render("Score: " + str(score), True, (250, 250, 250))
    
    # Create a surface with the score text
    screen.blit(text, (10, 10)) 
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    sound.play()
    pygame.display.update()


pygame.quit()
