# 1510-A4

Every program needs a README.md

This is written in markdown. Read about markdown here: [markdowncheatsheet](https://www.markdownguide.org/cheat-sheet/)

## Your name:
Adam Goldsmith

## Your student number:
A01185566

## Your GitHub ID:
adambgoldsmith

## Any important comments you'd like to make about your work:
In hindsight, I ended up biting off WAY MORE than I can chew in such a small time-frame.
Aardwolfs style plus simple surface with a complex underbelly inspired me to make something similar.
Because I have a background with game development I wanted to push myself and see what I could create using my
newfound knowledge of python. The scope of my project ended up being massive, and even though I managed to
create the game flow that I wanted, it ended up leaving too many things to document and test.

I tried to make the regular battle loop and the boss battle loop one function for reusability, but it caused 
more trouble than just having two separate functions.

I made three songs for the game, but ended up not being able to use them due to multithreading limits for the
assignment. One is a theme for the start and end (lore), one for the map travel game play (main over world),
and finally, the boss theme.

For my flowchart, I tried to avoid using programmer lingo as much as possible so that anybody could
recreate the game even if they don't know how to code.



---------- REQUIRED ELEMENTS TABLE (BEST EXAMPLES) ----------

(a) use of immutable data structures     ||     helper_functions.board.py line 29
(b) use of mutable data structures       ||     helper_functions.nymph.py line 41
(c) exceptions and exception handling    ||     helper_functions.battle.py line 89, test_user_battle_choice.py line 42
(d) mini scope/lifetime of variables     ||     all
(e) small, atomic functions              ||     helper_functions.character.py line 32
(f) simple flat, readable code           ||     all
(g) list/dictionary comprehension        ||     helper_functions.board.py line 53
(h) selection using if statements        ||     helper_functions.board.py line 179
(i) repetition using loops               ||     helper_functions.boss.py line 48
(j) use of membership operator           ||     helper_functions.board.py line 145
(k) use of the range function            ||     helper_functions.chest.py line 39
(l) user of itertools functions          ||     helper_functions.battle.py line 49
(m) use of the random module             ||     helper_functions.battle.py line 290
(n) function annotation                  ||     helper_functions.board.py line 153
(o) doctests and unittests               ||     helper_functions.board.py line 88, test_generate_pattern.py line 11
(p) f-string formatting                  ||     helper_functions.boss.py line 80