from pda_cfg import accepts_a_n_b_n, accepts_parentheses, accepts_nested_blocks

def main():
    samples = [
        ("a^n b^n", "aaabbb", accepts_a_n_b_n),
        ("Balanced parentheses", "(()())", accepts_parentheses),
        ("Nested blocks", "BEGIN x; BEGIN y; END END", accepts_nested_blocks),
    ]
    print("PDA and CFG Case-Study Demonstration")
    for label, value, fn in samples:
        print(f"{label:24} {value:30} -> {'ACCEPTED' if fn(value) else 'REJECTED'}")

if __name__ == "__main__":
    main()
