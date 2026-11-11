# Sample PDA Traces

## Input `aabb`
Stack top is shown at the right.

| Read | Action | Stack |
|---|---|---|
| start | initialize | `Z0` |
| `a` | push A | `Z0 A` |
| `a` | push A | `Z0 A A` |
| `b` | pop A | `Z0 A` |
| `b` | pop A | `Z0` |
| end | input consumed; no A remains | accept |

## Input `(()())`
- `(`: push
- `(`: push
- `)`: pop
- `(`: push
- `)`: pop
- `)`: pop
- End with empty stack: accept

## Nested block input
For `BEGIN x; BEGIN y; END END`, push on outer `BEGIN`, push on inner `BEGIN`, pop on inner `END`, and pop on outer `END`. The stack is empty at end, so the input is accepted.

## Limitations
These recognizers handle restricted educational grammars, not a complete programming language. They do not perform type checking, variable declaration checks, or program execution.
