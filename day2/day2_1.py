import sys

COMMANDS = {
    "forward": lambda param, pos: (pos[0] + param, pos[1]),
    "down": lambda param, pos: (pos[0], pos[1] + param),
    "up": lambda param, pos: (pos[0], pos[1] - param),
}

pos = (0, 0)
with open(sys.argv[1]) as input:
    for cmd_line in input:
        (cmd_str, param) = cmd_line.split()
        param = int(param)
        cmd = COMMANDS[cmd_str]
        pos = cmd(param, pos)
(hz_pos, depth) = pos
print("hz_pos =", hz_pos, "depth =", depth)
print(hz_pos * depth)