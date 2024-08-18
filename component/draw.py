import time

from const import *


class Draw:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect[0], rect[1], rect[2], rect[3])

    def init_surface(self):
        surface = pygame.Surface((self.rect.w + LINE_WIDTH / 2, self.rect.h + LINE_WIDTH / 2))
        surface.fill(WHITE)
        pygame.draw.rect(surface, BLACK, (0, 0, self.rect.w, self.rect.h), LINE_WIDTH)
        return surface


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    background = pygame.display.set_mode((width, height))
    draw = Draw((0, 0, 500, 500))
    s = draw.init_surface()
    background.blit(s, (0, 0))
    pygame.display.set_caption("Monopoly by PlasmolysisMango")
    pygame.display.update()
    time.sleep(5)
