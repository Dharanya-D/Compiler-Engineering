class CFG:
    def __init__(self, non_terminals, terminals, productions, start_symbol):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.productions = productions
        self.start_symbol = start_symbol
        self.first = {nt: set() for nt in non_terminals}
        self.follow = {nt: set() for nt in non_terminals}
        self.follow[start_symbol].add('$')  # Add EOF to FOLLOW of start symbol

    def compute_first(self):
        # Initialize FIRST sets for terminals
        first = {t: {t} for t in self.terminals}
        first['ε'] = {'ε'}  # ε is the empty string

        # Iterate until no changes occur
        changed = True
        while changed:
            changed = False
            for nt in self.non_terminals:
                for production in self.productions[nt]:
                    # For each production A -> β1 β2 ... βk
                    for symbol in production:
                        if symbol in self.terminals or symbol == 'ε':
                            # If β1 is a terminal or ε, add to FIRST(A)
                            if symbol not in self.first[nt]:
                                self.first[nt].add(symbol)
                                changed = True
                            break
                        elif symbol in self.non_terminals:
                            # If β1 is a non-terminal, add FIRST(β1) - {ε} to FIRST(A)
                            prev_size = len(self.first[nt])
                            self.first[nt].update(self.first[symbol] - {'ε'})
                            if prev_size != len(self.first[nt]):
                                changed = True
                            if 'ε' not in self.first[symbol]:
                                break
                    else:
                        # If all symbols can derive ε, add ε to FIRST(A)
                        if 'ε' not in self.first[nt]:
                            self.first[nt].add('ε')
                            changed = True

    def compute_follow(self):
        # Iterate until no changes occur
        changed = True
        while changed:
            changed = False
            for nt in self.non_terminals:
                for production in self.productions[nt]:
                    # For each production A -> β1 β2 ... βk
                    trailer = self.follow[nt].copy()
                    for i in range(len(production) - 1, -1, -1):
                        symbol = production[i]
                        if symbol in self.non_terminals:
                            # Add TRAILER to FOLLOW(symbol)
                            prev_size = len(self.follow[symbol])
                            self.follow[symbol].update(trailer)
                            if prev_size != len(self.follow[symbol]):
                                changed = True
                            # Update TRAILER
                            if 'ε' in self.first[symbol]:
                                trailer.update(self.first[symbol] - {'ε'})
                            else:
                                trailer = self.first[symbol].copy()
                        elif symbol in self.terminals:
                            # Reset TRAILER for terminals
                            trailer = {symbol}

    def print_first_sets(self):
        print("FIRST Sets:")
        for nt in self.non_terminals:
            print(f"FIRST({nt}) = {self.first[nt]}")

    def print_follow_sets(self):
        print("FOLLOW Sets:")
        for nt in self.non_terminals:
            print(f"FOLLOW({nt}) = {self.follow[nt]}")


# Example usage
if __name__ == "__main__":
    # Define the CFG
    non_terminals = ['S', 'A', 'B']
    terminals = ['a', 'b', 'c', 'd']
    productions = {
        'S': [['A', 'B'], ['B', 'c']],
        'A': [['a', 'A'], ['ε']],
        'B': [['b', 'B'], ['d']]
    }
    start_symbol = 'S'

    # Create CFG object
    cfg = CFG(non_terminals, terminals, productions, start_symbol)

    # Compute FIRST and FOLLOW sets
    cfg.compute_first()
    cfg.compute_follow()

    # Print results
    cfg.print_first_sets()
    cfg.print_follow_sets()
