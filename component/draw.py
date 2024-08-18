import pygame

class Draw:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])

    def init_surface(self):
        surface = pygame.Surface((self.rect.w + LINEWIDTH / 2, self.rect.h + LINEWIDTH / 2))
        surface.fill(WHITE)
        pygame.draw.rect(surface, BLACK, (0, 0, self.rect.w, self.rect.h), LINEWIDTH)
        return surface

if __name__ == '__main__':
    pygame.init()