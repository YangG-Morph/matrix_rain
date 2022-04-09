#
import random
import pygame.display
from src.utils import weighted_random_size, make
from src.letter import Letter
from src.constants import SPEED_MULT

class Trail(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.length = random.randint(10, 30)
        self.letters = None
        self.surface = None
        self.rect = pygame.Rect((0, 0), (0, 0))
        self.velocity = pygame.Vector2((0, 0))
        self.new_letters()

    def update_rect(self):
        window_width = pygame.display.get_window_size()[0]
        width = self.letters[0].surface.get_width() * 2
        height = self.letters[0].surface.get_height() * len(self.letters)
        x = random.randint(0, window_width)
        y = random.randint(-height - 200, -height)
        self.rect.update((x, y), (width, height))

    def update_surface(self):
        # Must clear trail surface
        self.surface = pygame.Surface(self.rect.size)
        self.surface.set_colorkey('black')
        # Must redraw every letter
        for letter in self.letters:
            letter.draw(self.surface)

    def new_letters(self):
        self.letters = make(Letter, self.length, args=(*weighted_random_size(),))
        self.velocity.update(0, self.letters[0].size * SPEED_MULT)
        self.update_rect()
        self.update_surface()

    def update(self, dt):
        [letter.update(dt) for letter in self.letters]
        if any(letter.changed for letter in self.letters):
            self.update_surface()
        self.rect.center += self.velocity

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

