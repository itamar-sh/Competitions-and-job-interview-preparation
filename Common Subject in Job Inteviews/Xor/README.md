# Consective Xor
## Problem
Chef has two binary strings AA and BB, both having length NN. He can perform the following operation on AA any number of times (possibly zero):

Select any index i (1 ≤ i ≤ N−1) and simultaneously set A_i := A_i ⊕ A_{i + 1} }
and A_{i + 1} := A_i ⊕ A_{i + 1}.

Formally, if initially A_i = x and A_{i + 1} = y.
then set A_i := x ⊕ y and A_{i + 1} := x ⊕ y
Here, ⊕ denotes the bitwise XOR operation.

Chef wants to determine if it is possible to make AA equal to BB by applying the above operation any number of times. Can you help Chef?

## Input Format
The first line contains a single integer TT — the number of test cases. Then the test cases follow.
The first line of each test case contains an integer NN — the length of the binary string AA.
The second line of each test case contains the binary string AA of length NN.
The third line of each test case contains the binary string BB of length NN.
## Output Format
For each test case, output YES if Chef can make string AA equal to string BB by applying the above operation any number of times. Otherwise, output NO.

You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical).

### Input Sample
3
2
00
10
3
010
000
4
0011
0100
### Output Sample
NO
YES
YES