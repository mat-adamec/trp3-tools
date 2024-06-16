from itertools import groupby

PALETTE = ['2f63a0', '4f7ca4', '7395ba', '747ea4']

def gradient(string, palette, backward=False):
    string = list(string)
    out = []
    for _, g in groupby(enumerate(string, 2), lambda k: True if k[1] == '.' else k[0]):
        out.append(''.join(val for _, val in g))
    space_indices = []
    while ' ' in out:
        i = out.index(' ') + len(space_indices)
        del out[i - len(space_indices)]
        space_indices.append(i)
    string = out
    new_string = []
    length = len(string) / len(palette)
    if len(string) < 4:
        if len(string) == 1:
            order = [0]
        elif len(string) == 2:
            order = [0, 1]
        elif len(string) == 3:
            order = [0, 1, 2]
    elif len(string) % len(palette) == 0:
        length = int(length)
        order = [0] * length + [1] * length + [2] * length + [3] * length
    elif len(string) % len(palette) == 1:
        length = int(length)
        order = [0] * length + [1] * (length+1) + [2] * length + [3] * length
    elif len(string) % len(palette) == 2:
        length = int(length)
        order = [0] * length + [1] * (length+1) + [2] * (length+1) + [3] * length
    elif len(string) % len(palette) == 3:
        length = int(length)
        order = [0] * length + [1] * (length+1) + [2] * (length+2) + [3] * length
    if backward:
        order = reversed(order)
    for ch, co in zip(string, order):
        new_string += ['{col:' + palette[co] + '}' + ch + '{/col}']
    for space in space_indices:
        new_string.insert(space, ' ')
    return ''.join(new_string)

def colorize(string, palette):
    half = len(string)/2
    if half == int(half):
        forward = gradient(string[:int(half)], palette)
        backward = gradient(string[int(half):], palette, backward=True)
        mid = ''
    else:
        forward = gradient(string[:int(half)], palette)
        backward = gradient(string[int(half)+1:], palette, backward=True)
        mid = '{col:' + palette[-1] + '}' + string[int(half)] + '{/col}'
    return forward + mid + backward

def left_to_right(string, palette):
    return gradient(string, palette)

def right_to_left(string, palette):
    return gradient(string, palette, backward=True)

def symmetrical(string, palette):
    return colorize(string, palette)
    
    
    
    
## USER INPUT ##
# Put your color palette hex codes here.
PALETTE = ['2f63a0', '4f7ca4', '7395ba', '747ea4']
# Put your string here.
STRING = 'Terawyne'

LR = left_to_right(STRING, palette=PALETTE)
RL = right_to_left(STRING, palette=PALETTE)
SYM = symmetrical(STRING, palette=PALETTE)

print(f'Left to right: {LR}')
print(f'Right to left: {RL}')
print(f'Symmetrical: {SYM}')