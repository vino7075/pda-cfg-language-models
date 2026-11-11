# CFG and PDA Case Studies

## Case 1: Equal number of `a` symbols followed by `b` symbols
**Language:** `L = { a^n b^n | n >= 1 }`

**CFG**
```text
S -> aSb | ab
```
**PDA:** Push one marker for every `a`. When the first `b` appears, switch to popping mode. Pop one marker for each `b`. Accept at end only when the stack has returned to its bottom marker.

Accepted: `ab`, `aabb`, `aaabbb`. Rejected: `aab`, `abb`, `ba`.

## Case 2: Balanced parentheses
**CFG**
```text
S -> (S)S | epsilon
```
**PDA:** Push a marker for every `(` and pop one for every `)`. Reject a closing parenthesis when the stack has no marker. Accept at end when the stack is empty.

Accepted: `()`, `(())`, `(()())`, and the empty string. Rejected: `)(`, `(()`, `())`.

## Case 3: Nested program blocks
**Simplified grammar**
```text
Program   -> Block
Block     -> BEGIN Items END
Items     -> Statement
           | Statement ; Items
           | Block
           | Block ; Items
Statement -> identifier
```
A PDA pushes a marker on `BEGIN` and pops it on `END`. Identifiers and semicolons are checked according to this restricted statement grammar.

Accepted: `BEGIN x END`, `BEGIN x; BEGIN y; END END`. Rejected: `BEGIN x`, `END`.

## Why a finite automaton is insufficient
A finite automaton has a fixed number of states and cannot store an arbitrary number of unmatched opening symbols. The languages `a^n b^n` and nested delimiters require unbounded counting or nesting. A PDA provides a stack for this memory.

## Ambiguity and determinism
The grammar `S -> aSb | ab` has a direct recursive structure. The standard balanced-parentheses grammar describes nested pairs. The block grammar is deliberately simplified; a complete programming language would need additional statement and error-handling rules. The implementations are deterministic stack simulations for these restricted languages. General CFG parsing can require nondeterministic choices or LL/LR parsing.
