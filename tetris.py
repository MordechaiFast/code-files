import pygame
import random


DISPLAY_SIZE = (400, 500)
FPS = 25
BOARD_X = 100
BOARD_Y = 60
ZOOM = 20

# Model
FIGURES = (
    ({1, 5, 9, 13}, {4, 5, 6, 7}),
    ({4, 5, 9, 10}, {2, 6, 5, 9}),
    ({6, 7, 9, 10}, {1, 5, 6, 10}),
    ({1, 2, 5, 9}, {0, 4, 5, 6}, {1, 5, 9, 8}, {4, 5, 6, 10}),
    ({1, 2, 6, 10}, {5, 6, 7, 9}, {2, 6, 10, 11}, {3, 5, 6, 7}),
    ({1, 4, 5, 6}, {1, 4, 5, 9}, {4, 5, 6, 9}, {1, 5, 6, 9}),
    ({1, 2, 5, 6}, ),
)
COLORS = (
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
)

class Figure:
    def __init__(self, col=0, row=0):
        self.col = col
        self.row = row
        self.type = random.randint(0, len(FIGURES) - 1)
        self.color = random.randint(1, len(COLORS) - 1)
        self.rotation = 0

    @property
    def image(self) -> set[int]:
        return FIGURES[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(FIGURES[self.type])

# Controler
class Tetris:
    def __init__(self, height=20, width=10, level=2):
        self.height = height
        self.width = width
        self.level = level
        self.gameover = False
        self.field = [[0 for y in range(width)] for x in range(height)]
        self.score = 0
        self._new_figure()

    def _new_figure(self):
        self.figure = Figure(col=(self.width - 1) // 2 - 1)
        if self._figure_intersects:
            self.figure = None
            self.gameover = True
        else:
            self.hit_bottom = False

    @property
    def _figure_intersects(self) -> bool:
        for cell in self.figure.image:
            y = self.figure.row + cell // 4
            x = self.figure.col + cell % 4
            if (y >= self.height or x >= self.width or x < 0
                or self.field[y][x] != 0):
                return True
        return False

    def step_down(self):
        self.figure.row += 1
        if self._figure_intersects:
            self.figure.row -= 1
            if self.hit_bottom:
                self._freeze_figure()
            else:
                self.hit_bottom = True
        else:
            self.hit_bottom = False

    def fall_down(self):
        while not self._figure_intersects:
            self.figure.row += 1
        self.figure.row -= 1
        self._freeze_figure()

    def _freeze_figure(self):
        for cell in self.figure.image:
            y = self.figure.row + cell // 4
            x = self.figure.col + cell % 4
            self.field[y][x] = self.figure.color
        self._break_lines()
        self._new_figure()

    def _break_lines(self):
        lines = 0
        for row in range(1, self.height):
            if all(self.field[row][col] != 0 for col in range(self.width)):
                lines += 1
                for lower_row in range(row, 1, -1):
                    for col in range(self.width):
                        self.field[lower_row][col] = self.field[lower_row - 1][col]
        self.score += lines ** 2

    def go_side(self, dx: int):
        self.figure.col += dx
        if self._figure_intersects:
            self.figure.col -= dx

    def rotate_figure(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self._figure_intersects:
            self.figure.rotation = old_rotation

# View
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
# Initialize the game engine
pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 25, True, False)
font1 = pygame.font.SysFont('Calibri', 65, True, False)
text_game_over = font1.render("Game Over", True, (255, 125, 0))
text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

quitting = False
pressing_down = False
counter = 0

pygame.display.set_caption("Tetris")
game = Tetris()

while not quitting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # The user clicked the close button.
            quitting = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not game.gameover:
                game.rotate_figure()
            elif event.key == pygame.K_DOWN:
                pressing_down = True
            elif event.key == pygame.K_LEFT and not game.gameover:
                game.go_side(-1)
            elif event.key == pygame.K_RIGHT and not game.gameover:
                game.go_side(1)
            elif event.key == pygame.K_SPACE and not game.gameover:
                game.fall_down()
            elif event.key == pygame.K_ESCAPE:
                # Restart the game
                game = Tetris()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    counter += 1
    if counter % (FPS // game.level // 2) == 0 or pressing_down:
        if not game.gameover:
            game.step_down()

    screen.fill(WHITE)
    text = font.render(f"Score: {game.score}", True, BLACK)
    screen.blit(text, [0, 0])
    for y in range(game.height):
        for x in range(game.width):
            pygame.draw.rect(
                screen,
                GRAY,
                [BOARD_X + ZOOM * x, BOARD_Y + ZOOM * y,
                 ZOOM, ZOOM],
                1
            )
            if game.field[y][x] > 0:
                pygame.draw.rect(
                    screen,
                    COLORS[game.field[y][x]],
                    [BOARD_X + ZOOM * x + 1,
                     BOARD_Y + ZOOM * y + 1,
                     ZOOM - 2, ZOOM - 1]
                )
    if not game.gameover:
        for y in range(4):
            for x in range(4):
                if (y * 4 + x) in game.figure.image:
                    pygame.draw.rect(
                        screen,
                        COLORS[game.figure.color],
                        [BOARD_X + ZOOM * (x + game.figure.col) + 1,
                         BOARD_Y + ZOOM * (y + game.figure.row) + 1,
                         ZOOM - 2, ZOOM - 2]
                    )
    else:
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
