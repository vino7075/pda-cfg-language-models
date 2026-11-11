def accepts_parentheses(value: str) -> bool:
    if not isinstance(value, str):
        return False
    stack = []
    for symbol in value:
        if symbol == "(":
            stack.append(symbol)
        elif symbol == ")":
            if not stack:
                return False
            stack.pop()
        else:
            return False
    return not stack
