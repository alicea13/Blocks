import pygame


pygame.init()
size = width, height = 300, 200
screen = pygame.display.set_mode(size)
block_w, block_h = 30, 15
wh_line = 2
coordx, coordy = 0, 0


def draw():
    global half, count, screen, coordx, coordy
    screen.fill((255, 255, 255))
    for y in range(height):
        if y % 2 == 0:
            for x in range(width):
                if ((x * block_w + 2 * x) // 30) != 10:
                    pygame.draw.rect(screen, pygame.Color("red"),
                                     ((coordx, coordy), (block_w, block_h)))
                else:
                    pygame.draw.rect(screen, pygame.Color("red"),
                                     ((block_w * x + x * 2, block_h * y + 2 * y), (block_w // 2, block_h)))
        else:
            for x in range(width):
                if ((x * block_w + 2 * x) // 30) != 0:
                    pygame.draw.rect(screen, pygame.Color("red"),
                                     ((coordx, coordy), (block_w, block_h)))
                else:
                    pygame.draw.rect(screen, pygame.Color("red"),
                                     ((block_w * x + x * 2, block_h * y + 2 * y), (block_w // 2, block_h)))




draw()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()