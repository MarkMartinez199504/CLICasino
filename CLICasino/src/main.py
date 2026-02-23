import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    running = True

    hand_pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        #RENDER GAME HERE
        pygame.draw.rect(screen, "White", (hand_pos[0], hand_pos[1], 100, 200))

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
    