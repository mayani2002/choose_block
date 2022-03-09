Rohan has arranged $N$ wooden block in a line and has numbered them from $1$ to $N$ to identify them correctly. He has $M$ different paints where every color is given a code number from $1$ to $M$. Rohan decides to paint each block in a particular color where he might use all $M$ colors ( $ie.$ $C_1,C_2,…,C_m$ ) to paint the blocks or might miss out on few colors. There can be one or more than one block of same color code.

He gives you a challenge where you have to select the longest contiguous subsegment of the blocks such that there is at least one color among all $M$ colors which does not occur in that subsegment of blocks. 

---

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two integers $N$ and $M$.
- The second line contains $N$ space-separated integers $C_1,C_2,…,C_m$

---
**Output**

For each test case, print a single line containing one integer ― the maximum length of a valid subsegment.

---

**Constraints**

$1≤T≤100$

$1≤N≤10^3$

$2≤M≤10^3$

$1≤C_i≤M$ for each valid $i$

---
**Sample Input**

    2
    6 2
    1 1 1 2 2 1
    5 3
    1 1 2 2 1

---
**Sample Output**

    3
    5