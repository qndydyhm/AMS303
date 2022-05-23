# HW3
## 10.1
 - 1.
   - a) a, c or b, d
   - b) f
 - 3.  

    | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  | 26  | 27  | 28  | 29  | 30  | 31  | 32  | 33  | 34  | 35  | 36  | 37  | 38  | 39  | 40  | ... |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | 1   | 1   | 0   | 0   | 1   | 1   | 2   | 2   | 0   | 1   | 0   | 0   | 2   | 1   | 1   | 0   | 0   | 2   | 1   | 1   | 0   | 2   | 2   | 1   | 0   | 0   | 0   | 2   | 1   | 1   | 0   | 0   | 2   | 1   | 3   | 0   | 2   | 2   | 1   | 1   | 0   |

    3, 4, 9, 11, 12, 16, 17, 21, 25, 26, 27, 31, 32, 36, 40+
 - 8.
    - a)  

    | a   | b   | c   | d   |
    | --- | --- | --- | --- |
    | 0   | 1   | 0   | 1   |
   - b) impossible. Since there is no successor for f, then f must be 0. Because the graph is symmetric, so assuming start from e and e is 1, then d is 2, c is 1, b is 2, a is 1, e is 2, thus contradiction.

 - 12. 
   - a) Since  $K_n = K_{n−1} ∪ \{x | l(x) = n\ and\ s(x) ∩ K_{n−1} = Ø\}$, $l(x) = n$ iff there exist a path P $X_n->X_{n-1}->X_{n-2}...->X_0$ where $X_n \in L(n)$. This is the longest because if we the previous vertex must have higher level than the successor, if we skip any of the vertex say from $X_n->X_{n-2}$, the total length of the path must be shorter than the longest path gave before.  
 - 15.  
   - Grundy function: value is the first non used non negative integer of value of successors, then it must be different then successor's, proved.
   - Level numbers: $l(x) = k \Leftrightarrow x \notin L_{k-1}\ and\ s(x) \subseteq L_{k-1}$, thus any vertex must have different level than its successor.

## 10.2
 - 1.
   - a) 10, 11, 11, 101 -> 111, change 101 to 10 (move 3 from 4th)
   - b) 1, 11, 101, 111 -> 0, no winning condition
   - c) 10, 100, 100, 110 -> 100, change 100 to 0 or 101 to 1 (move 4 from 2nd, 3rd or 4th)
 - 2.
   - a) 10, 0, 0, 10 -> 0, no winning condition
   - b) 1, 0, 10, 1 -> 10, change 10 to 0 or 0 to 10 (move 2 from 3rd or 1 from 2nd)
   - c) 10, 1, 1, 0 -> 10, change 10 to 0 or 0 to 10 (move 2 from 1st or 1 from 4th)
 - 3.
   - a) 0, 0, 11, 0 -> 11, change 11 to 0 or 0 to 11 (move 3 from 3rd or 2 from 4th)
   - b) 1, 0, 1, 10 -> 10, change 10 to 0 or 1 to 11 (move 2 from 3rd or 4th)
   - c) 0, 1, 0, 1 -> 0, no winning condition
 - 4. Grundy value for number of sticks less than or equal to 7 is the same as exercise 2. Thus the answers are the same except for b), add a winning strategy by moving 5 from 3rd.
 - 6.
   - a) 100 to 1 or 110 to 11, move 3 from 2nd, 3rd or 4th
   - b) 100 to 10 or 110 to 0, move 2 from 2nd or 3rd or all from 4th