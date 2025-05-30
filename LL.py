inp = input("Enter the input string: ") + "$"  # Append end marker $
table = {
    ('S', 'a'): "AB",
    ('S', 'b'): "AB",
    ('A', 'a'): "aA",
    ('A', 'b'): "b",
    # ('A', '$'): "&", # A → ε when input is $
    ('B', 'a'): "CA",
    ('B', 'b'): "CA",
    ('B', 'c'): "CA",
    ('C', 'a'): "&",  # C → ε
    ('C', 'b'): "&",  # C → ε
    ('C', 'c'): "cC",
    # ('C', '$'): "&", # C → ε when input is $
}

stack = ['$']  # Initialize stack with the end marker
stack.append('S')  # Start symbol 'S'
i = 0
word = inp[i]

while True:
    focus = stack[-1]  # Always get the current top of stack

    # Success case: both stack and input have reached end
    if focus == '$' and word == '$':
        print("Success: Input parsed correctly!")
        print(stack)
        break

    # Terminal symbol or end symbol in focus
    elif focus in ['a', 'b', 'c', '$']:
        if focus == word:
            stack.pop()  # Pop the terminal symbol from stack
            i += 1  # Move to next character in the input
            word = inp[i]  # Update the current input symbol
            print(stack)
        else:
            print(f"Error: Expected '{focus}', but found '{word}'.")
            break

    # Non-terminal processing
    else:
        rule = table.get((focus, word))  # Get the rule for (focus, word)
        if rule:
            stack.pop()  # Pop focus from stack
            # Push RHS in reverse order (except epsilon)
            if rule != "&":
                for symbol in reversed(rule):
                    stack.append(symbol)
                    print(stack)
        else:
            print(f"Error: No rule found for ({focus}, {word}).")
            break
