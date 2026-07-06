# -------------------------------
# Import required libraries
# -------------------------------
import pygame
import sys

# -------------------------------
# Initialize Pygame
# -------------------------------
pygame.init()

# -------------------------------
# Game Constants
# -------------------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

PLAYER_SIZE = 40
PLAYER_SPEED = 5

# Colors (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)

# -------------------------------
# Set up the game window
# -------------------------------
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple 2D Pygame Window")

clock = pygame.time.Clock()

# -------------------------------
# Player Class
# -------------------------------
class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.size = PLAYER_SIZE
        self.speed = PLAYER_SPEED

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, (self.x, self.y, self.size, self.size))

# -------------------------------
# Create player object
# -------------------------------
player = Player()

# -------------------------------
# Main Game Loop
# -------------------------------
running = True
while running:
    clock.tick(FPS)

    # ---------------------------
    # Event Handling
    # ---------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------------------------
    # Player Movement
    # ---------------------------
    keys = pygame.key.get_pressed()
    player.move(keys)

    # ---------------------------
    # Drawing Section
    # ---------------------------
    screen.fill(WHITE)     # Background color
    player.draw(screen)    # Draw player

    pygame.display.update()

# -------------------------------
# Quit Pygame
# -------------------------------
pygame.quit()
sys.exit()
