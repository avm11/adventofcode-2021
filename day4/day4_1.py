import sys
from typing import List, Tuple, Optional
from functools import reduce


class BingoCard:
    def __init__(self, card_data: List[List[int]]) -> None:
        self.card_data = []
        for row in card_data:
            self.card_data.append([(n, False) for n in row])

    def __str__(self) -> str:
        result_str = ""
        for row in self.card_data:
            result_str += " ".join([f"{n : >2}" if not m else " X" for n, m in row])
            result_str += "\n"
        return result_str

    def mark(self, num: int) -> 'BingoCard':
        new_card_data = []
        for row in self.card_data:
            new_card_data.append([(n, True if n == num else m) for n, m in row])
        new_card = BingoCard([])
        new_card.card_data = new_card_data
        return new_card

    def is_winning(self) -> bool:
        col_marks = [m for _n, m in self.card_data[0]]
        for row in self.card_data:
            if reduce(lambda a, p: a and p[1], row, True):
                return True
            col_marks = [m and p[1] for m, p in zip(col_marks, row)]
        for col_mark in col_marks:
            if col_mark:
                return True
        return False

    def score(self) -> int:
        score_sum = 0
        for row in self.card_data:
            score_sum += sum([n if not m else 0 for n, m in row])
        return score_sum


def read_data(file_name: str) -> Tuple[List[int], List[BingoCard]]:
    with open(file_name) as input:
        numbers = [int(n) for n in input.readline().split(",")]

        card_data = None
        bingo_cards = []
        for line in input:
            if not line.strip():
                if card_data:
                    bingo_cards.append(BingoCard(card_data))
                card_data = []
                continue
            card_data.append([int(n) for n in line.split()])

    return (numbers, bingo_cards)

def mark_cards(bingo_cards: List[BingoCard], num: int) -> List[BingoCard]:
    return [card.mark(num) for card in bingo_cards]

def winner(bingo_cards: List[BingoCard]) -> Optional[BingoCard]:
    for card in bingo_cards:
        if card.is_winning():
            return card
    return None

numbers, bingo_cards = read_data(sys.argv[1])
winner_card = None
num = -1
for num in numbers:
    bingo_cards = mark_cards(bingo_cards, num)
    winner_card = winner(bingo_cards)
    if winner_card:
        break

if winner_card:
    print("Winning number", num)
    print(winner_card)
    print("Score sum", winner_card.score())
    print("Score", winner_card.score() * num)
else:
    print("No winners :(")
