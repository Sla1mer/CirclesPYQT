import pygame
from copy import deepcopy


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 20
        self.top = 20
        self.cell_size = 20
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left,
                    y * self.cell_size + self.top,
                    self.cell_size,
                    self.cell_size), 1)
                if self.board[y][x] == 0:
                    pygame.draw.rect(screen, pygame.Color(0, 0, 0), (
                        x * self.cell_size + self.left + 1,
                        y * self.cell_size + self.top + 1,
                        self.cell_size - 2,
                        self.cell_size), 0)
                elif self.board[y][x] == 1:
                    pygame.draw.rect(screen, pygame.Color(0, 255, 0), (
                        x * self.cell_size + self.left + 1,
                        y * self.cell_size + self.top + 1,
                        self.cell_size - 2,
                        self.cell_size), 0)
        self.clock.tick(self.FPS)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def update_frame(self, tick):
        self.FPS += tick

        if self.FPS < 10:
            self.FPS = 10
        elif self.FPS > 150:
            self.FPS = 150


class Life(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.board = [[0 for _ in range(width)] for _ in range(height)]

        self.is_play = False

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        x1 = (mouse_pos[0] - self.left) // self.cell_size
        y1 = (mouse_pos[1] - self.top) // self.cell_size
        return x1, y1

    def on_click(self, cell_coords):
        if not self.is_play:
            if 0 <= cell_coords[0] < self.width and 0 <= cell_coords[1] < self.height:
                self.board[cell_coords[1]][cell_coords[0]] = (self.board[cell_coords[1]][cell_coords[0]] + 1) % 2

    def next_move(self):
        self.boardcopy = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                self.boardcopy[y][x] = self.step(y, x)

        self.board = deepcopy(self.boardcopy)

    def step(self, y, x):
        t = [self.board[y - 1][x - 1],
             self.board[y - 1][x],
             self.board[y - 1][(x + 1) % self.width],
             self.board[y][x - 1],
             self.board[y][(x + 1) % self.width],
             self.board[(y + 1) % self.height][x - 1],
             self.board[(y + 1) % self.height][x],
             self.board[(y + 1) % self.height][(x + 1) % self.width]
             ]
        if self.board[y][x] == 0 and sum(t) == 3:
            return 1
        elif self.board[y][x] == 1 and 2 <= sum(t) <= 3:
            return 1
        else:
            return 0

    def random_game(self):
        from random import randint
        self.board = [[randint(0, 1) for _ in range(self.width)] for _ in range(self.height)]


def main():
    pygame.init()
    size = 1200, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Инициализация игры')

    board = Life(50, 30)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.get_click(event.pos)
                elif event.button == 4:
                    board.update_frame(5)
                elif event.button == 5:
                    board.update_frame(-5)
                elif event.button == 3:
                    board.is_play = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                board.is_play = not board.is_play
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                board.random_game()
        if board.is_play:
            board.next_move()

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
