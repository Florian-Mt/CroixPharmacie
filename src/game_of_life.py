import pygame
from random import randint, shuffle

from pharmacontroller import SCREEN_SIZE, PharmaScreen

SURVIVAL_RULES = [2, 3]
BIRTH_RULES = [3]


def generate_random_world():
    return [[randint(0, 1) for _ in range(SCREEN_SIZE)] for _ in range(SCREEN_SIZE)]


def get_neighbours(world: list[list[int]], x: int, y: int):
    return [
        # Previous row
        world[(x - 1) % SCREEN_SIZE][(y - 1) % SCREEN_SIZE],
        world[(x - 1) % SCREEN_SIZE][y],
        world[(x - 1) % SCREEN_SIZE][(y + 1) % SCREEN_SIZE],

        # Current row
        world[x][(y - 1) % SCREEN_SIZE],
        world[x][(y + 1) % SCREEN_SIZE],

        # Next row
        world[(x + 1) % SCREEN_SIZE][(y - 1) % SCREEN_SIZE],
        world[(x + 1) % SCREEN_SIZE][y],
        world[(x + 1) % SCREEN_SIZE][(y + 1) % SCREEN_SIZE],
    ]


def get_next_state(world: list[list[int]], x: int, y: int):
    neighbours = get_neighbours(world, x, y)
    is_alive = world[x][y] == 1
    alive_neighbours = sum(neighbours)
    alive_next_gen = (alive_neighbours in SURVIVAL_RULES and is_alive) or alive_neighbours in BIRTH_RULES
    return 1 if alive_next_gen else 0


def next_generation(world: list[list[int]]):
    return [[get_next_state(world, i, j) for j in range(SCREEN_SIZE)] for i in range(SCREEN_SIZE)]


def play_death_animation(last_world: list[list[int]]):
    # Animation: remove all active cells randomly to the last one
    active_cell = [(i, j) for i in range(SCREEN_SIZE) for j in range(SCREEN_SIZE) if last_world[i][j] == 1]
    shuffle(active_cell)
    for i, j in active_cell:
        last_world[i][j] = 0
        screen.set_image(last_world)

    # Wait for 1 more tick
    screen.set_image(last_world)


def play_until_death():
    initial_world = generate_random_world()
    encountered_worlds = []

    while True:
        encountered_worlds.append(hash("".join("".join(str(cell) for cell in row) for row in initial_world)))
        screen.set_image(initial_world)
        next_world = next_generation(initial_world)

        # If this world has already been encountered, exit
        if hash(next_world) in encountered_worlds:
            return initial_world

        else:
            initial_world = next_world


def play():
    while True:
        last_world = play_until_death()
        play_death_animation(last_world)


if __name__ == "__main__":
    pygame.init()
    screen = PharmaScreen(color_scale=False)
    play()
