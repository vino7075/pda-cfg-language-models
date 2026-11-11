def accepts_a_n_b_n(value: str) -> bool:
    if not isinstance(value, str) or not value:
        return False
    stack = []
    reading_b = False
    seen_a = 0
    for symbol in value:
        if symbol == "a" and not reading_b:
            stack.append("A")
            seen_a += 1
        elif symbol == "b":
            reading_b = True
            if not stack:
                return False
            stack.pop()
        else:
            return False
    return seen_a > 0 and reading_b and not stack
