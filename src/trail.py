#
import random
import pygame.display
from src.utils import weighted_random_size, make
from src.letter import Letter
from src.constants import SPEED_MULT
from src.utils import time_it

class Trail(pygame.sprite.Group):
    def __init__(self, bounds):
        super().__init__()
        self.length = random.randint(10, 30)
        self.letters = None
        self.surface = None
        self.rect = pygame.Rect((0, 0), (0, 0))
        self.velocity = pygame.Vector2((0, 0))
        self.bounds = bounds
        self.new_letters()

    def update_bounds(self, bounds):
        self.bounds = bounds

    def on_screen(self):
        return self.rect.top < self.bounds.bottom

    def update_rect(self, letter_width, letter_height):
        width = letter_width * 2
        height = letter_height * len(self.letters)
        x = random.randint(0, self.bounds.width)
        y = random.randint(-height - 200, -height)
        self.rect.update((x, y), (width, height))

    def update_surface(self):
        # Must clear trail surface
        self.surface = pygame.Surface(self.rect.size)
        self.surface.set_colorkey('black')
        # Must redraw every letter
        [letter.draw(self.surface) for letter in self.letters]

    def new_letters(self):
        self.letters = make(Letter, self.length, args=[*weighted_random_size()])
        first_letter = self.letters[0]
        self.velocity.update(0, first_letter.size * SPEED_MULT)
        self.update_rect(*first_letter.surface.get_size())
        self.update_surface()

    def update(self, dt):
        [letter.update(dt) for letter in self.letters]
        if any(letter.changed for letter in self.letters):
            self.update_surface()
        self.rect.center += self.velocity

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

