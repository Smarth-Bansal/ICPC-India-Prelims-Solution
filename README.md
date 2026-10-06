# ICPC India Online Round 2026 (Prelims): Python Solutions

Python solutions for all 10 problems (A to J). Each file is named `<Letter>_<Title>.py` and reads from standard input with `input()`.

| ID | Problem | Time |
|----|---------|------|
| A | Phone Charging | O(1) per test |
| B | Cyclic Shift | O(n log n) |
| C | Furious Farming | O(n log n) |
| D | Curio Packing | O(n) |
| E | Side Hustle | O(n log n) |
| F | Take the L | O(n log n) |
| G | Team Formation Tactics | O(n log n) |
| H | Random Merging | O(n) after O(N) precompute |
| I | Mountain Medians | O(n^2) |
| J | Off With Their Heads | O(n) per test |

---

## A: Phone Charging

Charging has two speeds: `a` seconds per percent below 80, and `b` seconds per percent from 80 upward.

- If `x < 80`, pay `(80 - x) * a` to get to 80, then set `x = 80`.
- Then pay `(100 - x) * b` for the rest.
- If `x = 100`, the second part is 0, so the answer is 0.

## B: Cyclic Shift

Think of the array as a circle with `n` edges, one between each neighbouring pair (including last to first).
A cyclic shift cuts the circle at one edge, and that edge no longer counts in `f(b)`.

- Compute the absolute difference of every circular neighbouring pair.
- Cutting at the largest difference removes it, so the answer is the second largest difference (`diff[-2]` after sorting).

Example: `[1, 4, 2, 3]` has circular differences 3, 2, 1, 2. Cut the 3, and the max left is 2.

## C: Furious Farming

Sort the cloud positions. Let:

- `a` = empty fields to the left of the first cloud,
- `b` = empty fields to the right of the last cloud,
- `gap` = the largest run of empty fields between two neighbouring clouds.

All clouds move together, so the clouds sweep a range of shifts from `-L` to `+R`.
To cover everything we need `L >= a`, `R >= b`, and `L + R >= gap` (the widest gap is only covered by the combined sweep).

Two plans, taking the cheaper:

- Go left first for `a` days, then right: the walk costs `2a + max(b, gap - a)`.
- Go right first for `b` days, then left: the walk costs `2b + max(a, gap - b)`.

## D: Curio Packing

Iron never breaks, so all irons go into bag 2. Glasses go into bag 1, one on top of another.

- After `k + 1` glasses, the bottom glass in bag 1 already has `k` glasses above it, so bag 1 is full.
- The `(k + 2)`-th glass goes into bag 2 (on top of the irons). Irons between glass `k + 1` and glass `k + 2` sit below it and don't matter.
- Everything after the `(k + 2)`-th glass must also go into bag 2, on top of it, so its total weight (`G` = 1, `I` = 2) must be at most `k`.

Code: find the `(k + 2)`-th `G` with `find_nth`. If there is none, print `YES`. Otherwise sum the weights after it and print `NO` if the sum is greater than `k`, else `YES`. This is O(n).

## E: Side Hustle

A permutation splits into independent cycles. Handle each cycle separately and add the results.

- A cycle of length 1 is already correct and adds its reward `a`.
- For a longer cycle of length `L`, sort its rewards in descending order.
  - Fix only the best `j` people (for `j` from 1 to `L-2`) with `j` swaps: profit is `(sum of top j) - j*c`.
  - Fix the whole cycle with `L-1` swaps: profit is `(sum of all) - (L-1)*c`.
  - Do nothing: profit 0.
- Take the maximum of these.

## F: Take the L

- Sort the points by x and count how many times y decreases between neighbours.
- Sort the points by y and count how many times x decreases between neighbours.
- Print `YES` if the smaller of the two counts is at most 1, otherwise `NO`.

## G: Team Formation Tactics

Sort ratings in descending order and build prefix sums `P`.
There are three team kinds (strength `6x`, `4x + 4y`, `3x + 3y + 3z`).
Choose `a` teams of the first kind and `lo` of the second kind, and the rest `n - a - lo` of the third kind.

- The `a` first-kind teams use the `a` highest ratings, each counted 6 times.
- The `lo` second-kind teams use the next `2*lo` ratings, each counted 4 times.
- The remaining teams use consecutive ratings counted 3 times each.
- The smallest `2a + lo` ratings are left over as the filler members.
- The total is `2*P[a] + P[a + 2*lo] + 3*P[3n - 2a - lo]`.

The code loops over every `a` and binary searches the best `lo` by comparing the value at `mid` with `mid + 1`.
The answer is the maximum over all `a`.

## H: Random Merging

By linearity of expectation, count how many times each element contributes to `s`.

- An element at 0-based index `i` has `i` elements on its left and `n-1-i` on its right.
- Its expected number of contributions is `H[i] + H[n-1-i]`, where `H[k] = 1 + 1/2 + ... + 1/k` (harmonic number).
- The answer is the sum over `i` of `a[i] * (H[i] + H[n-1-i])`, modulo 998244353.

Modular inverses of 1..200001 are precomputed once with the linear formula `inv[i] = -(M // i) * inv[M % i]`, then prefix sums give `H`.

Check with `[1, 2, 3]`: `1*1.5 + 2*2 + 3*1.5 = 10`.

## I: Mountain Medians

Build the mountain from the largest value outward. After placing the largest `len` values they fill one block of
consecutive positions `[l, r]`, so the DP state is just `(l, r)`, about n^2/2 states.

- The next smaller value goes either just left of the block (`l-1`) or just right of it (`r+1`).
- Before placing value `v`, `checkL` builds the small set of positions where `v` can be a prefix or suffix median for that placement. Every position `j` with `a[j] = v` must be in this set. `checkR` is the mirror image (`x -> n-1-x`).
- Quick rejects: if any value appears more than 6 times in `a`, or `n` appears twice, the answer is 0.
- If `n` appears once, it must be at position 0 or `n-1`, otherwise the answer is 0.
- If `n` does not appear in `a`, the peak can start anywhere, so sum the DP over all starting positions.
- Only one layer of the DP is kept in memory (`prev`).

## J: Off With Their Heads

The final string has length `n + 1`, and the last string used always stays whole.

- Try each string type that exists as the last string.
- From the rest, drop `1`s and keep `0`s where possible. A kept `00` or `01` can be paired with a dropped `11` or `01`, with `11` dropped first.
- Put all zeros first, then the `01` pieces, then the leftover ones, then the last string.
- Print the smallest candidate among all choices of the last string.

With a single string, just print it.