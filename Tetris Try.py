import pygame
import random

# Define constants
GRID_WIDTH = 20
GRID_HEIGHT = 20
BLOCK_SIZE = 30
WINDOW_WIDTH = GRID_WIDTH * BLOCK_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

# Define the Piece class
class Piece:
    shapes = [
        [[1, 1, 1],
         [0, 1, 0]],

        [[2, 2],
         [2, 2]],

        [[0, 3, 3],
         [3, 3, 0]],

        [[4, 4, 0],
         [0, 4, 4]],

        [[5, 5, 5, 5]],

        [[0, 6, 0],
         [6, 6, 6]],

        [[7, 7, 7],
         [7, 0, 0]]
    ]

    colors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, WHITE]

    def __init__(self, shape, x=0, y=0):
        self.shape = shape
        self.color = random.choice(Piece.colors)
        self.x = x
        self.y = y

    def move_down(self):
        self.y += 1

    def move_up(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def rotate(self):
        self.shape = [
            [self.shape[j][i] for j in range(len(self.shape))]
            for i in range(len(self.shape[0]) - 1, -1, -1)
        ]

# Set up the game window and initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# Define the game functions
def draw_block(x, y, color):
    pygame.draw.rect(window, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            draw_block(x, y, grid[y][x] or BLACK)

def draw_piece(piece):
    for y, row in enumerate(piece.shape):
        for x, col in enumerate(row):
            if col:
                draw_block(piece.x + x, piece.y + y, piece.color)

def new_piece():
    shape = random.choice(Piece.shapes)
    return Piece(shape, x=GRID_WIDTH // 2 - len(shape[0]) // 2)

def check_collision(piece):
    for y, row in enumerate(piece.shape):
        for x, col in enumerate(row):
            if col:
                if piece.x + x < 0 or piece.x + x >= GRID_WIDTH or piece.y + y >= GRID_HEIGHT or grid[piece.y + y][piece.x + x]:
                    return True
    return False

def lock_piece(piece):
    for y, row in enumerate(piece.shape):
        for x, col in enumerate(row):
            if col:
                grid[piece.y + y][piece.x + x] = piece.color

def clear_rows():
    global score

    num_cleared = 0
    y = GRID_HEIGHT - 1
    while y >= 0:
        if all(grid[y]):
            num_cleared += 1
            for i in range(y, 0, -1):
                grid[i] = grid[i - 1][:]
            grid[0] = [0] * GRID_WIDTH
        else:
            y -= 1

    if num_cleared:
        score += 10 * num_cleared

def game_over():
    font = pygame.font.Font(None, 48)
    text = font.render("GAME OVER", True, WHITE)
    rect = text.get_rect()
    rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    window.blit(text, rect)
    pygame.display.update()

    pygame.time.wait(1000)

    pygame.quit()
    quit()

# Initialize the game variables
clock = pygame.time.Clock()
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
current_piece = new_piece()
next_piece = new_piece()
score = 0
fps = 10

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            elif event.key == pygame.K_SPACE:
                while not check_collision(current_piece):
                    current_piece.move_down()
                lock_piece(current_piece)
                clear_rows()
                current_piece = next_piece
                next_piece = new_piece()

            elif event.key == pygame.K_LEFT:
                current_piece.move_left()
                if check_collision(current_piece):
                    current_piece.move_right()

            elif event.key == pygame.K_RIGHT:
                current_piece.move_right()
                if check_collision(current_piece):
                    current_piece.move_left()

            elif event.key == pygame.K_UP:
                current_piece.rotate()
                if check_collision(current_piece):
                    current_piece.rotate()

            elif event.key == pygame.K_DOWN:
                current_piece.move_down()
                if check_collision(current_piece):
                    current_piece.move_up()
                    lock_piece(current_piece)
                    clear_rows()
                    current_piece = next_piece
                    next_piece = new_piece()

    # Update the game
    if not check_collision(current_piece):
        current_piece.move_down()
    else:
        current_piece.move_up()
        lock_piece(current_piece)
        clear_rows()
        current_piece = next_piece
        next_piece = new_piece()

        if check_collision(current_piece):
            game_over()

    # Draw the game
    window.fill(BLACK)
    draw_grid()
    draw_piece(current_piece)
    pygame.display.update()

    # Update the clock
    clock.tick(fps)