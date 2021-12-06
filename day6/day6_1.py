import sys
from typing import List

NEW_TIMER = 6
NEWBORN_TIMER = 8

def state_to_str(state: List[int]) -> str:
    return ", ".join(map(str, state))

def day_cycle(state: List[int]) -> List[int]:
    newborn_num = 0
    new_state = []
    for timer in state:
        if timer == 0:
            newborn_num += 1
        new_state.append(timer - 1 if timer > 0 else NEW_TIMER)
    if newborn_num > 0:
        new_state.extend([NEWBORN_TIMER] * newborn_num)
    return new_state

state = []
with open(sys.argv[1]) as input:
    state = list(map(int, input.readline().split(",")))
# print("Initial state:", state_to_str(state))
for day in range(0, 80):
    state = day_cycle(state)
#     print(f"After {day:>2} days:", state_to_str(state))
print(len(state))
