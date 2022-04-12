#
import pygame
import random
from src.trail import Trail
from src import utils
from src.window_manager import WindowManager
from src.rendered_text import RenderedText
from src.constants import FPS, GREEN, MAX_TRAILS
#from src.logger import logging
from src.utils import time_it

# Done? TODO Blit letters to the Trail surface
# Done? TODO Remove off screen trails only when new trails are made
# TODO Space same size letters apart to prevent overlapping

TRAIL_TIMER = pygame.USEREVENT + 0
MOUSE_TIMER = pygame.USEREVENT + 1

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen.fill("black")
        self.clock = pygame.time.Clock()
        self.trails = []
        self.bounds = pygame.Rect((0, 0), pygame.display.get_window_size())
        self.blured = False
        self.debug_mode = True
        self._init_timers()
        self._add_new_trails()

    def _init_timers(self):
        pygame.time.set_timer(TRAIL_TIMER, random.randint(100, 500))
        pygame.time.set_timer(MOUSE_TIMER, 1000)

    def hide_cursor(self):
        if pygame.mouse.get_visible():
            pygame.mouse.set_visible(False)

    def clear_screen(self):
        self.screen.fill('black')

    def quit(self):
        WindowManager.quit()
        pygame.quit()
        raise SystemExit

    def update_bounds(self):
        self.bounds.size = pygame.display.get_window_size()
        [trail.update_bounds(self.bounds) for trail in self.trails]

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == TRAIL_TIMER:
                pygame.time.set_timer(TRAIL_TIMER, random.randint(100, 500))
                self._add_new_trails()
            elif event.type == pygame.MOUSEMOTION and not pygame.mouse.get_visible():
                pygame.mouse.set_visible(True)
            elif event.type == MOUSE_TIMER and pygame.mouse.get_visible():
                pygame.time.set_timer(MOUSE_TIMER, 1000)
                self.hide_cursor()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.quit()
                elif event.key == pygame.K_w:
                    # Experimental
                    self.screen = WindowManager.toggle_wallpaper()
                    self.update_bounds()
                elif event.key == pygame.K_f:
                    self.screen = WindowManager.toggle_fullscreen()
                    self.update_bounds()
                elif event.key == pygame.K_b:
                    self.blured = not self.blured
                elif event.key == pygame.K_d:
                    self.debug_mode = not self.debug_mode

    def _add_new_trails(self):
        if len(self.trails) < MAX_TRAILS:
            amount = min(20, MAX_TRAILS - len(self.trails))
            self.trails += utils.make(Trail, amount, args=[self.bounds])
            self.trails.sort(reverse=False, key=lambda trail: trail.letters[0].size)

    def _handle_trails(self, dt):
        [(trail.update(dt), trail.draw(self.screen)) for trail in self.trails]
        if pygame.time.get_ticks() % 2:
            self.trails[:] = [trail for trail in self.trails if trail.on_screen()]

    def blur(self):
        new_surf = pygame.transform.smoothscale(self.screen, (self.bounds.width // 2, self.bounds.height // 2))
        new_surf = pygame.transform.smoothscale(new_surf, (self.bounds.width, self.bounds.height))
        self.screen.blit(new_surf, (0, 0))

    def display_fps(self):
        if not hasattr(self, 'all_fps'):
            self.all_fps = []
            self.performance_start_time = pygame.time.get_ticks()
        current_fps = self.clock.get_fps()
        if current_fps > 0:  # Exclude loading
            self.all_fps.append(current_fps)
        text = f"FPS: {current_fps:.0f} " \
               f"Trails: {len(self.trails)} " \
               f"Letters: {sum([len(trail.letters) for trail in self.trails])} " \
               f"Average FPS: {((sum(self.all_fps)/len(self.all_fps)) if self.all_fps else 0):.2f} " \
               f"Lowest FPS: {(min(self.all_fps) if self.all_fps else 0):.2f} " \
               f"Highest FPS: {(max(self.all_fps) if self.all_fps else 0):.2f} "

        size = 18
        rendered_text = RenderedText.font_objects[size].render(text, True, 'white')
        rendered_text_shadow = RenderedText.font_objects[size].render(text, True, 'purple')
        self.screen.blit(rendered_text_shadow, (-1, -1))
        self.screen.blit(rendered_text, (0, 0))
        #logging.debug(text)
        #if pygame.time.get_ticks() - self.performance_start_time >= 60_000:  # In miliseconds, 180_000 is 3 minute
        #    self.quit()

    def run(self):
        while True:
            dt = self.clock.tick_busy_loop()
            self._handle_events()

            self.clear_screen()
            self._handle_trails(dt)
            if self.blured:
                self.blur()
            if self.debug_mode:
                self.display_fps()
            pygame.display.flip()



