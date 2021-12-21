from collections import namedtuple

Pos = namedtuple("Pos", "p1, score1, p2, score2")

MAX_SPACE_NUM = 10
MAX_SCORE = 1000


def dice100():
    while True:
        for n in range(1, 101):
            yield n


def turn(pos, dice, turn_num):
    steps = next(dice) + next(dice) + next(dice)
    if turn_num % 2 == 1:
        new_pos = (pos.p1 + steps) % MAX_SPACE_NUM
        return Pos(new_pos, pos.score1 + new_pos + 1, pos.p2, pos.score2)
    else:
        new_pos = (pos.p2 + steps) % MAX_SPACE_NUM
        return Pos(pos.p1, pos.score1, new_pos, pos.score2 + new_pos + 1)


def game_end(pos: Pos) -> bool:
    return pos.score1 >= MAX_SCORE or pos.score2 >= MAX_SCORE


d100 = dice100()
current_pos = Pos(9, 0, 2, 0)
turn_num = 0
while not game_end(current_pos):
    turn_num += 1
    current_pos = turn(current_pos, d100, turn_num)

total_score = turn_num * 3 * min(current_pos.score1, current_pos.score2)
print(total_score)
