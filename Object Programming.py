import pygame
import random
from blob import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3

WIDTH = 800
HEIGHT = 600
WHITE = (255,255,255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT)) # This creates the environment/window of the display
pygame.display.set_caption("Blob World") # Creates a title for the window
clock = pygame.time.Clock()  # Sets the FPS


class Fastblob(Blob): # This creates a sub-class of Blob, which basically builds a new class on top of Blob (Base class)

    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary) # super refers to all the base classes that this is built on
        #self.color = BLUE

    def move(self): # This overrides the old move function in blob.py
        self.x += random.randrange(-7, 8)
        self.y += random.randrange(-7, 8)


def draw_environment(blob_list):  # This function draws the environment, i.e.(Generates a frame to display)
    game_display.fill(WHITE)  # Paints the environment WHITE

    for blobs_dict in blob_list:
        for blob_id in blobs_dict:
            blob = blobs_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)  # Draws the blob
            blob.move()  # Moves blob
            blob.check_bounds()  # Checks boundary of blob

    pygame.display.update()  # Update display

def main():  # Define main frame
    blue_blob = dict(enumerate([Blob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    # Creates a dictionary to track the id of each blob
    red_blob = dict(enumerate([Fastblob(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    # Creates a dictionary to track the id of each blob
    while True:
        for event in pygame.event.get():  # Quit condition
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment([blue_blob, red_blob])
        clock.tick(60)


if __name__ == '__main__':  # Boilerplate function
    main()
