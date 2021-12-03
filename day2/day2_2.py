import sys

COMMANDS = {
    "forward": lambda param, aim, hz, d: (aim, hz + param, d + aim * param),
    "down": lambda param, aim, hz, d: (aim + param, hz, d),
    "up": lambda param, aim, hz, d: (aim - param, hz, d),
}

aim = hz_pos = depth = 0
with open(sys.argv[1]) as input:
    for cmd_line in input:
        (cmd_str, param) = cmd_line.split()
        param = int(param)
        cmd = COMMANDS[cmd_str]
        (aim, hz_pos, depth) = cmd(param, aim, hz_pos, depth)
print("aim =", aim, "hz_pos =", hz_pos, "depth =", depth)
print(hz_pos * depth)