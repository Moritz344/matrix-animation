import pygame
import random

pygame.init()

x = 800
y = 600

screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()
pygame.display.set_caption("Matrix")

font = pygame.font.SysFont("Minecraft", 36)
col = int(x / font.size(" ")[0])
drops = [0 for _ in range(col)]

colours = [
    "green",
]
buchstaben = [
    "1",
    "0",
]


def draw_matrix():
    pygame.font.init()

    screen.fill("black")

    for i in range(len(drops)):
        text = font.render(random.choice(buchstaben), False,
                           random.choice(colours))
        # print(i)
        if drops[i] * font.size(" ")[1] and random.random() > 0.9:
            drops[i] = 0

        drops[i] += 1
        screen.blit(text,
                    (i * font.size(" ")[0], drops[i] * font.size(" ")[1]))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw_matrix()
    pygame.display.update()
    clock.tick(30)
