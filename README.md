<h1>Experiment: Cellular Automata in a Bidimensional Recirculatory Matrix Topology</h1>

## Topology.

### Matrix Visualisation:
Let's take a look at this 2d matrix.
- Red - Adjacent Cells
- Blue - Traversal Path
- Yellow - Current Cell
<img src="https://github.com/Vazno/game_of_life_experiment/assets/96925396/ef4dc892-85ee-4a2c-ba02-23679070112f">


Every path in the matrix lead back to their starting point, forming closed loops, the grid of cells is wrapped around on itself so that cells on the edge of the grid are connected to cells on the opposite edge. For instance:
- If you move from 44 to bottom-right: `44` -> `11` -> `22` -> `33` -> `44`.
- If you move from 44 to bottom-left: `44` -> `8` -> `17` -> `26` -> `35` -> `44`.

## Game.

### The game operates as follows (B3/S23):
- Cells can be alive or inactive.
- The "near" value of a cell indicates the number of alive neighboring cells.

In each iteration, cells evolve based on their "near" values:
- If a cell has 3 alive neighbors, it becomes alive.
- If a cell has fewer than 2 or more than 3 alive neighbors, it becomes inactive.

## Patterns
...
