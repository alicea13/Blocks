import pygame


pygame.init()
size = width, height = 300, 200
screen = pygame.display.set_mode(size)
block = True
line = False
half = False
wh_l = 0
bw, bh = 90, 45


def draw():
    global wh_l, block, half
    for j in range(1):
        for i in range(2):
            if block:
                pygame.draw.rect(screen, (255, 0, 0),
                                 ((i * bw + wh_l * 2, j * bh),
                                  (i * bw + bw + wh_l, j * bh + bh)))
                pygame.draw.line(screen, (255, 255, 255),
                                 (i * bw + bw, j * bh),
                                 (i * bw + bw, j * bh + bh))
                wh_l += 1


draw()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()