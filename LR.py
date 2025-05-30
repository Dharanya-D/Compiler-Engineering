# Grammar: [LHS, RHS]
grammar = [
    ["F", "S"],     # 0
    ["S", "XX"],    # 1
    ["X", "aX"],    # 2
    ["X", "b"]      # 3
]

# ACTION table (extended with S12 and S13)
action = {
    (0, 'a'): 'S3',
    (0, 'b'): 'S4',
    (1, '$'): 'Accept',
    (2, 'a'): 'S6',
    (2, 'b'): 'S7',
    (3, 'a'): 'S3',
    (3, 'b'): 'S4',
    (4, 'a'): 'R3',
    (4, 'b'): 'R3',
    (5, '$'): 'R1',
    (6, 'a'): 'S6',
    (6, 'b'): 'S7',
    (7, '$'): 'R3',
    (8, 'a'): 'R2',
    (8, 'b'): 'R2',
    (9, '$'): 'R2',
    (10, '$'): 'R1',
    (10, 'a'): 'S12',     # ← Added S12
    (11, 'a'): 'S6',
    (11, 'b'): 'S13',     # ← Added S13
    (12, '$'): 'R2',
    (13, '$'): 'R3'
}

# GOTO table (extend as needed)
goto = {
    (0, 'S'): 1,
    (0, 'X'): 2,
    (2, 'X'): 5,
    (3, 'X'): 8,
    (6, 'X'): 9,
    (10, 'X'): 12,
    (11, 'X'): 13
}

# Input string
inp = input("Enter the string: ") + '$'

# Initialize stack
stack = ['$']
stack.append(0)
i = 0
word = inp[i]
i += 1

# Parsing loop
while True:
    print(f"Symbol: {word}\tStack: {stack}")
    state = stack[-1]
    
    if (state, word) not in action:
        print("Not valid")
        break

    act = action[(state, word)]

    if act.startswith('R'):
        prod_num = int(act[1:])  # R#
        lhs, rhs = grammar[prod_num]
        for _ in range(2 * len(rhs)):
            stack.pop()
        if isinstance(stack[-1], int):
          state = stack[-1]
        else:
          state = stack[-2]

        stack.append(lhs)
        stack.append(goto[(state, lhs)])
    elif act.startswith('S'):
        stack.append(word)
        stack.append(int(act[1:]))  # S#
        word = inp[i]
        i += 1
    elif act == 'Accept':
        print("String Accepted")
        break
