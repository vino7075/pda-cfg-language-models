import re

TOKEN = re.compile(r"BEGIN|END|[A-Za-z_][A-Za-z0-9_]*|;", re.ASCII)

def tokenize(source: str):
    tokens, pos = [], 0
    while pos < len(source):
        if source[pos].isspace():
            pos += 1
            continue
        match = TOKEN.match(source, pos)
        if not match:
            raise ValueError(f"Invalid token at position {pos}")
        tokens.append(match.group())
        pos = match.end()
    return tokens

def accepts_nested_blocks(source: str) -> bool:
    try:
        tokens = tokenize(source)
    except (TypeError, ValueError):
        return False
    stack = []
    expecting_statement = True
    for token in tokens:
        if token == "BEGIN":
            stack.append("BEGIN")
            expecting_statement = True
        elif token == "END":
            if not stack:
                return False
            stack.pop()
            expecting_statement = False
        elif token == ";":
            if expecting_statement:
                return False
            expecting_statement = True
        else:
            if not stack or not expecting_statement:
                return False
            expecting_statement = False
    return bool(tokens) and not stack and not expecting_statement
