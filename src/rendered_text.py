#
import pygame
from src.constants import FONT_NAME, GREEN, GREENISH_WHITE, ALLOWED_LETTERS, MIN_FONT_SIZE, MAX_FONT_SIZE, BLACK

class RenderedText:
    font_objects = {i: pygame.font.SysFont(FONT_NAME, i) for i in range(MIN_FONT_SIZE, MAX_FONT_SIZE+1)}
    rendered = {}

    @classmethod
    def render_all_letters(cls):
        for color in [GREENISH_WHITE, GREEN]:
            for size, font_obj in cls.font_objects.items():
                for letter in ALLOWED_LETTERS:
                    rendered = font_obj.render(letter, True, color, BLACK)
                    rendered.set_colorkey(BLACK)
                    letter_dict = {letter: rendered}
                    try:
                        sizes_dict = cls.rendered[color]
                        try:
                            sizes_dict[size].append(letter_dict)
                        except KeyError:
                            sizes_dict.update({size: [letter_dict]})
                    except KeyError:
                        cls.rendered.update({color: {size: [letter_dict]}})

    def __new__(cls, *args, **kwargs):
        if cls is RenderedText:
            raise TypeError(f"Do not instantiate '{cls.__name__}'. Just use the class name.")

RenderedText.render_all_letters()