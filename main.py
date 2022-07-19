from random import randint

import pygame

import sprites


def newCactus() -> sprites.Cactus:
    num = randint(1, 3)
    types_list = list()
    for i in range(num):
        types_list.append(randint(1, 2))
    return sprites.Cactus(num, types_list)


def newBird() -> sprites.Bird:
    bird_type = randint(1, 3)
    return sprites.Bird(bird_type)


width, heigh = 1200, 400
fps = 30
# real size is (240, 80)
pygame.init()
screen = pygame.display.set_mode((width, heigh))

pygame.display.set_caption("Google Dinosaur")
clock = pygame.time.Clock()
dino = sprites.Dinosaur([60, 195, 185, 105])
started, ended, restarted = False, False, False
is_right_leg_up = True
frames, score = 0, 0
do_dino_runs = False
do_jumping_up, do_jumping_down = False, False
font_start = pygame.font.SysFont('Arial', 50, bold=True)
font_score = pygame.font.SysFont('Consolas', 20, bold=True)
font_end = pygame.font.SysFont('Arial', 50, bold=True)
font_restart = pygame.font.SysFont('Arial', 25, bold=True)
cactuses, birds = list(), list()
is_bird_up = True
distance_to_last_obstacle, last_obstacle = 125, None
step, distance_between_obstacles = 2, 125


def end() -> bool:

    x, y, w, h = dino.rect

    for c in cactuses:
        for x_d in range(x // 5, x // 5 + w // 5):
            for y_d in range(y // 5, y // 5 + h // 5):
                if dino.pixels[x_d][y_d] == 'd' and c.pixels[x_d][y_d] == 'c':
                    return True

    for b in birds:
        for x_d in range(x // 5, x + w // 5):
            for y_d in range(y // 5, y // 5 + h // 5):
                if dino.pixels[x_d][y_d] == 'd' and b.pixels[x_d][y_d] == 'b':
                    return True
    return False


while True:
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (100, 100, 100), (0, 270), (1200, 270), 2)

    if not do_dino_runs and not restarted:
        render_start = font_start.render('PRESS SPACE TO START THE GAME', True, pygame.Color('orange'))
        screen.blit(render_start, (int(width / 2 - 350), int(heigh / 2 - 150)))

    if restarted:
        fps = 30
        dino = sprites.Dinosaur([60, 195, 185, 105])
        started, ended, restarted = False, False, False
        is_right_leg_up = True
        frames, score = 0, 0
        do_dino_runs = False
        do_jumping_up, do_jumping_down = False, False
        cactuses, birds = list(), list()
        is_bird_up = True
        distance_to_last_obstacle, last_obstacle = 125, None
        step, distance_between_obstacles = 2, 125

    if do_dino_runs:
        frames += 1
        score = frames // 5
        render_score = font_score.render(F'SCORE: {score}', True, (100, 100, 100))
        screen.blit(render_score, (int(width - 200), int(30)))

        if score % 100 == 0:
            fps += 1
            if distance_between_obstacles > 50:
                distance_between_obstacles -= 1

    dino.idle()
    for idx, cactus in enumerate(cactuses):
        cactus.draw(screen)
        if end():
            ended = True

        if started:
            cactus.clear()
            cactus.x -= step

        if cactus.x < -30:
            del cactuses[idx]

    if last_obstacle in [None, 'bird'] and distance_to_last_obstacle >= distance_between_obstacles:
        cactuses.append(newCactus())
        distance_to_last_obstacle = 0
        if score >= 0:
            last_obstacle = 'cactus'

    if last_obstacle == 'cactus' and distance_to_last_obstacle >= distance_between_obstacles and score > 0:
        birds.append(newBird())
        distance_to_last_obstacle = 0
        last_obstacle = 'bird'

    if do_dino_runs and not do_jumping_down and not do_jumping_up:
        dino.run(is_right_leg_up)
        if frames % 7 == 0:
            is_right_leg_up = not is_right_leg_up

    distance_to_last_obstacle += 1

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        do_dino_runs = True
        started = True
    if key[pygame.K_s] and not do_jumping_down and not do_jumping_up and started:
        dino.lay()
    if key[pygame.K_w] and not do_jumping_down and not do_jumping_up and started:
        do_jumping_up = True

    if do_jumping_up or do_jumping_down:
        if dino.rect[1] <= 10:
            do_jumping_up = False
            do_jumping_down = True
        if dino.rect[1] == 195:
            do_jumping_down = False
        dino.jump('up' if do_jumping_up else 'down')

    dino.draw(screen)

    for idx, bird in enumerate(birds):
        if frames % 10 == 0:
            is_bird_up = not is_bird_up
        bird.draw(screen, is_bird_up)

        if end():
            ended = True

        if started:
            bird.clear()
            bird.x -= step

        if bird.x < -30:
            del birds[idx]

    dino = sprites.Dinosaur(dino.rect)

    if ended:
        while True:
            render_end = font_end.render('YOU LOSE', True, pygame.Color('red'))
            screen.blit(render_end, (int(width / 2 - 100), int(heigh / 2 - 50)))

            render_restart = font_restart.render('PRESS SPACE TO RESTART', True, pygame.Color('red'))
            screen.blit(render_restart, (int(width / 2 - 140), int(heigh / 2)))

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                restarted = True
                break

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
