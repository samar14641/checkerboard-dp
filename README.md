# checkerboard-dp
Dynamic programming solution to a version of the checkerboard problem.


Given: n x n checkerboard

Task: Traverse the board from the bottom to top row, starting at any square in the bottom row, and ending at any square in the top row. You are only allowed to travel upwards on each move, from a square in row i to a square in row i + 1. Furthermore, you can only travel directly upwards, or one square to the left or right of that square. From row i column j, you are only allowed to move to row i+1, column j-1 or column j or column j+1.

Model: Model the problem as more of a planning a trip over physical terrain by moving from the center of a geographic square plot of land to
the center of a neighboring square. We will start somewhere along the southern border of the land (row 0), and travel to the northern edge(row n-1). So, The cost to go from square \[i\]\[j\] to \[i+1\]\[j\] (i.e., travelling straight north) would be (A\[i\]\[j\] + A\[i + 1\]\[j\]) / 2; in other words, we are modelling that half our step would be travelling out of the originating square, and the other half would be travelling into the destination square, so we add half a unit’s worth of cost from each cell. To continue being more faithful to the travel analogy, when we go diagonally to the northwest or northeast, from \[i\]\[j\] to \[i + 1\]\[j - 1\] or \[i + 1\]\[j + 1\]respectively, our cost would again be half cost of originating square and half ending square, but be scaled by √2 to reflect the fact that travelling diagonally gives a longer path. 
Also note that under this version of the problem, the square you pick for the starting row (at the bottom) does now contribute to the cost of the path, and the square in the top row you end in contributes half its cost