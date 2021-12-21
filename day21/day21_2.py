from collections import namedtuple, defaultdict

Pos = namedtuple("Pos", "p1, score1, p2, score2")

MAX_SPACE_NUM = 10
MAX_SCORE = 21


def turn(pos, dice_roll, turn_num):
    if turn_num % 2 == 1:
        new_pos = (pos.p1 + dice_roll) % MAX_SPACE_NUM
        return Pos(new_pos, pos.score1 + new_pos + 1, pos.p2, pos.score2)
    else:
        new_pos = (pos.p2 + dice_roll) % MAX_SPACE_NUM
        return Pos(pos.p1, pos.score1, new_pos, pos.score2 + new_pos + 1)


def game_end(pos: Pos) -> bool:
    return pos.score1 >= MAX_SCORE or pos.score2 >= MAX_SCORE


def player1_win(pos: Pos) -> bool:
    return pos.score1 >= MAX_SCORE


def three_rolls():
    rolls = defaultdict(int)
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                rolls[i + j + k] += 1
    return rolls


start_pos = Pos(9, 0, 2, 0)
current_pos = {start_pos: 1}
turn_num = 0
rolls = three_rolls()
player1_wins = player2_wins = 0
while current_pos:
    turn_num += 1
    new_pos = dict()
    for pos, num in current_pos.items():
        for roll, roll_num in rolls.items():
            pos1 = turn(pos, roll, turn_num)
            if game_end(pos1):
                if player1_win(pos1):
                    player1_wins += num * roll_num
                else:
                    player2_wins += num * roll_num
            else:
                if pos1 in new_pos:
                    new_pos[pos1] += num * roll_num
                else:
                    new_pos[pos1] = num * roll_num
    current_pos = new_pos

print(player1_wins, player2_wins)
