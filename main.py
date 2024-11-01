import pygame
import random
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
NUM_PARTICLES = 100

COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 165, 0), (255, 0, 255),
    (0, 255, 255), (255, 255, 255)
]


class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(2, 5)
        self.life = random.randint(20, 60)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(1, 4)

    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.life -= 1

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)


def create_firework(x, y):
    color = random.choice(COLORS)
    particles = [Particle(x, y, color) for _ in range(NUM_PARTICLES)]
    return particles


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Virtual Fireworks Display')
    clock = pygame.time.Clock()

    fireworks = []

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    fireworks.append(create_firework(x, y))

        for firework in fireworks[:]:
            for particle in firework[:]:
                if particle.life > 0:
                    particle.update()
                    particle.draw(screen)
                else:
                    firework.remove(particle)
            if not firework:
                fireworks.remove(firework)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
