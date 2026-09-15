# Assessment: Multidimensional Lists — Tic-Tac-Toe

This assessment applies the concepts from the Multidimensional Lists lesson, particularly representing grids using 2D lists, accessing positions with `list[row][column]`, and traversing multidimensional structures. Part B extends these concepts by requiring multiple 3×3 grids to be stored and managed together. 

# Part A: Two-Player Tic-Tac-Toe

Create a two-player Tic-Tac-Toe game that can be played entirely in the terminal. Player 1 will use `X` and Player 2 will use `O`. Players will take turns entering coordinates to place their character on a 3×3 board.

Coordinates should use Python's normal **0-based indexing**, so both the rows and columns are numbered `0`, `1`, and `2`.

## Requirements

* Store the game board as a **3×3 2D list** and display the current board between turns.
* On each turn, ask the current player to enter a **row and column from `0–2`** to select a space.
* Only allow a character to be placed if the coordinates are valid and the selected space is empty. Invalid selections must be rejected without changing players.
* After every valid turn, check all **rows, columns, and diagonals** to determine whether the current player has won.
* Alternate between `X` and `O` until a player gets three in a row or all **9 spaces are filled**, resulting in a tie.

## Suggested Board Display

Your board needs to clearly show the current state of the game between turns. You may design your own terminal display, or use a format similar to:

```text
    0   1   2
  +---+---+---+
0 | X |   | O |
  +---+---+---+
1 |   | X |   |
  +---+---+---+
2 | O |   |   |
  +---+---+---+
```

Including the row and column numbers makes it easier for players to determine which coordinates they should enter.

## Test Cases

Before submitting, verify that your program correctly handles each of these situations:

| Test                                           | Expected Result                                         |
| ---------------------------------------------- | ------------------------------------------------------- |
| `X` fills an entire row.                       | `X` wins.                                               |
| `O` fills an entire column.                    | `O` wins.                                               |
| A player fills either diagonal.                | That player wins.                                       |
| A player selects an occupied space.            | The move is rejected and the same player chooses again. |
| A player enters a row or column outside `0–2`. | The move is rejected and the same player chooses again. |
| All 9 spaces fill without three in a row.      | The game ends in a tie.                                 |

# Part B: Ultimate Tic-Tac-Toe

Expand your program into a two-player version of **Ultimate Tic-Tac-Toe**.

Ultimate Tic-Tac-Toe is played using **nine normal Tic-Tac-Toe boards arranged into another 3×3 grid**. Each of the nine small boards is therefore also a space on the larger board.

Before programming Part B, use these resources to make sure you understand how the game works:

**[YouTube | Gather Together Games | How to Play Ultimate Tic-Tac-Toe](https://www.youtube.com/watch?v=L96GZCfTFzs)**

**[Michael Xing | Play Ultimate Tic-Tac-Toe](https://michaelxing.com/UltimateTTT/v3/)**

## Understanding the Board

Both the **large grid** and each **small grid** use coordinates from `0–2`.

The large grid identifies which small Tic-Tac-Toe board is being used:

```text
          LARGE GRID

       Col 0   Col 1   Col 2

Row 0  (0, 0)  (0, 1)  (0, 2)

Row 1  (1, 0)  (1, 1)  (1, 2)

Row 2  (2, 0)  (2, 1)  (2, 2)
```

Each of these positions contains another 3×3 Tic-Tac-Toe board that also uses coordinates from `(0, 0)` through `(2, 2)`.

This means a move can require **two ordered pairs**:

```text
Board: (row, column)
Space: (row, column)
```

For example:

```text
Board: (2, 1)
Space: (0, 2)
```

This places the player's character in space `(0, 2)` of the small board located at `(2, 1)`.

## How Turns Work

The first player may play anywhere. They choose both:

```text
Board: (row, column)
Space: (row, column)
```

After the first turn, however, players normally **do not get to choose which small board they play on**.

The position selected **inside the small board determines which board the next player must use**.

For example, suppose `X` makes this move:

```text
Board: (2, 1)
Space: (0, 2)
```

Because `X` selected space `(0, 2)`, Player `O` is sent to:

```text
Board: (0, 2)
```

`O` is now forced to play somewhere on that board. They only need to select a space:

```text
Space: (row, column)
```

Suppose `O` selects:

```text
Space: (1, 1)
```

Player `X` is now forced to play on:

```text
Board: (1, 1)
```

The coordinates of the space selected on one turn therefore become the coordinates of the board used on the next turn.

## Completed and Forced Boards

A small board is considered **completed** when either:

* `X` has won that board.
* `O` has won that board.
* All 9 spaces have been filled without a winner.

Once a small board is completed, **no additional characters may be placed on it**.

This creates an important exception to the forced-board rule.

Suppose a player selects:

```text
Space: (2, 0)
```

Normally, the next player would be forced to play on:

```text
Board: (2, 0)
```

However, if board `(2, 0)` has already been won or is completely filled, the next player **cannot** play there.

Instead, the next player gets a **free choice** and must enter two ordered pairs:

```text
Board: (row, column)
Space: (row, column)
```

The board they select must still be unfinished.

After they make their move, their selected **space coordinates once again determine the board for the following player**.

## Winning Small Boards

Each small board follows normal Tic-Tac-Toe rules.

If `X` gets three in a row on a small board, `X` has won that position on the large grid. The same applies to `O`.

For example, the state of the large grid might eventually be:

```text
 X |   | O
-----------
   | X |
-----------
 O |   | X
```

This does **not** represent individual moves. Each `X` or `O` represents an entire small board that has been won by that player.

## Winning Ultimate Tic-Tac-Toe

The goal is to win the **large 3×3 grid**.

A player wins the overall game when they win three small boards in a:

* Row
* Column
* Diagonal

For example:

```text
 X | X | X
-----------
 O |   |
-----------
   | O |
```

`X` has won all three small boards across the top row, so `X` wins the entire game.

## Requirements

* Store and manage all **nine 3×3 small boards using multidimensional lists**.
* Allow a player to enter a **board coordinate and space coordinate** when they have a free choice, and only a **space coordinate** when they have been forced to a specific board.
* After every valid move, use the selected **space coordinate as the board coordinate for the next player's turn**.
* Detect when a small board has been **won or completely filled** and prevent any further moves on that board. If a player is sent to a completed board, give them a free choice of any unfinished board.
* Track the winners of the nine small boards and end the game when a player wins **three small boards in a row, column, or diagonal**.

## Suggested Board Display

The player must be able to see the state of **all nine small boards** between turns. Your display should also clearly identify the board the current player is required to use.

One option is to display all nine boards together:

```text
        0       1       2
    0 1 2   0 1 2   0 1 2
   ------- ------- -------
0  X| |O   |X|     O| |
   -+-+-   -+-+-   -+-+-
1   |X|     |O|     |X|
   -+-+-   -+-+-   -+-+-
2  O| |     | |X    | |
   ------- ------- -------
    0 1 2   0 1 2   0 1 2
   ------- ------- -------
0   | |     | |     |O|
   -+-+-   -+-+-   -+-+-
1   | |    X|X|     | |
   -+-+-   -+-+-   -+-+-
2   | |     | |     | |
   ------- ------- -------
    0 1 2   0 1 2   0 1 2
   ------- ------- -------
0   | |     | |    X| |
   -+-+-   -+-+-   -+-+-
1   | |O    | |     | |
   -+-+-   -+-+-   -+-+-
2   | |     | |     |O|
```

You do not need to copy this exact formatting. A simpler display is acceptable as long as a player can clearly determine:

* The contents of each small board.
* The coordinates of the small boards.
* The coordinates of spaces within each board.
* Which board they are currently required to play on.

You may also display a separate **large-board status** showing which small boards have been won:

```text
Large Board:

 X |   | O
-----------
   | X |
-----------
 O |   |
```

When a player is forced to a particular board, the program should explicitly tell them:

```text
Player O
You must play on board (0, 2).
Enter a space from (0, 0) to (2, 2):
```

When the player has a free choice because the forced board is completed:

```text
Player X
Board (0, 2) is complete.
You may play on any unfinished board.

Enter board coordinates:
Enter space coordinates:
```

## Test Cases

Before submitting, verify that your program correctly handles each of these situations:

| Test                                                                            | Expected Result                                                                   |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| The first player begins the game.                                               | They may select any unfinished board and any empty space.                         |
| `X` plays on board `(2, 1)` at space `(0, 2)`.                                  | `O` is forced to board `(0, 2)`.                                                  |
| `O` is forced to board `(0, 2)`.                                                | `O` chooses a space within `(0, 2)` and cannot choose another board.              |
| A player selects an occupied space.                                             | The move is rejected and the same player chooses again.                           |
| A player enters coordinates outside `0–2`.                                      | The move is rejected and the same player chooses again.                           |
| A player completes three spaces in a row, column, or diagonal on a small board. | That small board is recorded as won by that player and cannot be played on again. |
| A small board fills completely without a winner.                                | The board is recorded as completed and cannot be played on again.                 |
| A move sends the next player to a board that has already been won.              | The next player receives a free choice of any unfinished board.                   |
| A move sends the next player to a board that is completely filled.              | The next player receives a free choice of any unfinished board.                   |
| During a free choice, a player selects a completed board.                       | The selection is rejected and the same player chooses another board.              |
| `X` wins three small boards across a row.                                       | `X` wins the overall game.                                                        |
| `O` wins three small boards down a column.                                      | `O` wins the overall game.                                                        |
| A player wins three small boards diagonally.                                    | That player wins the overall game.                                                |


### Assessment Checklist

#### Part A: Two-Player Tic-Tac-Toe — 10 Marks

| Criteria                                                                                                    |   Marks |
| ----------------------------------------------------------------------------------------------------------- | ------: |
| Game board is correctly stored and managed as a **3×3 2D list**.                                            |      /2 |
| Players can enter **row and column coordinates (0–2)** to place `X` and `O`, and turns alternate correctly. |      /2 |
| Invalid coordinates and attempts to use **occupied spaces** are rejected without changing turns.            |      /2 |
| Program correctly detects wins across **all rows, columns, and diagonals**.                                 |      /2 |
| Board is clearly displayed between turns, and the game correctly identifies a **winner or tie**.            |      /2 |
| **Part A Total**                                                                                            | **/10** |

#### Part B: Ultimate Tic-Tac-Toe — 15 Marks

| Criteria                                                                                                                                            |   Marks |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ------: |
| All **nine 3×3 boards** are correctly stored and managed using multidimensional lists.                                                              |      /3 |
| Players can correctly select a **board and space** when they have a free choice.                                                                    |      /2 |
| The selected space correctly determines the **forced board for the next player**.                                                                   |      /3 |
| Completed boards are correctly detected and cannot be played on; being sent to a completed board correctly gives the next player a **free choice**. |      /3 |
| Wins on individual boards are correctly detected and recorded on the **large board**.                                                               |      /2 |
| Program correctly detects when a player wins the overall game with **three small-board wins in a row, column, or diagonal**.                        |      /1 |
| The complete game state and required board are **clearly displayed between turns**.                                                                 |      /1 |
| **Part B Total**                                                                                                                                    | **/15** |

**Total: /25**
