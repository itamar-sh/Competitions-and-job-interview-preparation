# P polindrome
# N = len(P)
#

def test():
    len_p = input()
    P = str(input())
    #   print(P)
    # Loop through the lst `C` and sum its values.
    for i in range(len(P)):
        Q = P[-1:-i - 2:-1]
        # print(Q)
        # print(P+Q)
        PQ = P + Q
        flag = True
        for i in range(len(PQ) // 2):
            if PQ[i] != PQ[-i - 1]:
                flag = False
                break
        if flag:
            print(Q)
            break


# Read the number of test cases.
T = int(input())
# Loop over the number of test cases.
for test_no in range(1, T + 1):
    # Print case number
    print("Case #%d:" % test_no, end=" ")
    # and solve each test.
    test()


"""
Input:
3
4
abba
4
cccc
6
cdccdc
Output:
Case #1: abba
Case #2: c
Case #3: cdc
"""