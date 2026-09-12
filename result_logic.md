# Rock Paper Scissors — Winner Logic

## 1. The numerical representation

We represent the three choices using numbers:

```text
1 = Rock
2 = Paper
3 = Scissors
```

The game rules are:

```text
Rock     beats Scissors
Paper    beats Rock
Scissors beats Paper
```

---

## 2. The important observation

There are only **three possible outcomes** between the player's choice and the opponent's choice:

```text
Draw
Player wins
Computer wins
```

Let:

```text
difference = player_choice - computer_choice
```

### Draw

When both choices are the same:

```text
1 - 1 = 0
2 - 2 = 0
3 - 3 = 0
```

Therefore:

```text
difference = 0
```

and consequently:

```text
difference % 3 == 0
```

means **draw**.

---

## 3. Player-winning cases

Check all cases where the player wins:

```text
Rock beats Scissors
1 - 3 = -2

Paper beats Rock
2 - 1 = 1

Scissors beats Paper
3 - 2 = 1
```

The differences are:

```text
-2, 1, 1
```

Now apply modulo 3:

```text
-2 % 3 = 1
 1 % 3 = 1
 1 % 3 = 1
```

So every player-winning case becomes:

```text
difference % 3 == 1
```

---

## 4. Computer-winning cases

Now check the cases where the computer wins:

```text
Rock loses to Paper
1 - 2 = -1

Paper loses to Scissors
2 - 3 = -1

Scissors loses to Rock
3 - 1 = 2
```

The differences are:

```text
-1, -1, 2
```

Applying modulo 3:

```text
-1 % 3 = 2
-1 % 3 = 2
 2 % 3 = 2
```

Therefore:

```text
difference % 3 == 2
```

means **computer wins**.

---

## 5. Why modulo works here

The key idea is that `% 3` gives the position of a number inside a cycle of length 3.

Think of:

```text
0 → 1 → 2 → 0 → 1 → 2 → ...
```

After every 3 steps, we return to the same position.

So numbers that differ by 3 have the same remainder:

```text
1 % 3 = 1
4 % 3 = 1
7 % 3 = 1
```

Modulo effectively **removes complete cycles of 3** and keeps only the position within the cycle.

Rock-Paper-Scissors has exactly 3 states and its rules form a cycle, so this mathematical property can be used to determine the winner.

---

## 6. The final logic

```python
def check_winner(self):
    if self.player_choice == self.computer_choice:
        return "draw"

    if (self.player_choice - self.computer_choice) % 3 == 1:
        return "player"

    return "computer"
```

The three possible modulo results are therefore:

```text
0 → draw
1 → player wins
2 → computer wins
```

---

## 7. The intuition to remember

Do **not** think:

> "Modulo 3 means player wins."

Instead think:

> "RPS is a 3-state cycle. Taking `% 3` removes complete cycles and tells me the relative position inside that cycle."

The numbering

```text
1 = Rock
2 = Paper
3 = Scissors
```

is important because it makes the winning relationships line up with the modulo pattern.

If the choices were assigned arbitrary numbers, this particular formula would not necessarily work.
