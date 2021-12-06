import sys
from typing import List, Dict

NEW_TIMER = 6
NEWBORN_TIMER = 8

def vals_to_state(state_vals: List[int]) -> Dict[int, int]:
    state = dict()
    for timer in state_vals:
        state[timer] = state.get(timer, 0) + 1
    return state

def day_cycle(state: Dict[int, int]) -> Dict[int, int]:
    new_state = dict()
    for timer, num in state.items():
        if timer == 0:
            new_state[NEWBORN_TIMER] = new_state.get(NEWBORN_TIMER, 0) + num
        new_timer = timer - 1 if timer > 0 else NEW_TIMER
        new_state[new_timer] = new_state.get(new_timer, 0) + num
    return new_state

with open(sys.argv[1]) as input:
    state_vals = list(map(int, input.readline().split(",")))
state = vals_to_state(state_vals)
print("Initial state:", state)
for day in range(0, 256):
    state = day_cycle(state)
#    print(f"After {day + 1:>2} days:", state)
population = sum(v for _k, v in state.items())
print(population)
