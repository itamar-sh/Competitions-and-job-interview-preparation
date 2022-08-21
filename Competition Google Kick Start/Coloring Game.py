def test():
  # Read N integers from the standard input and save them in the list `C`.
  C = int(input())
  # Compute the value accordint to Tape.
  result = C // 5
  if C % 5 != 0:
    result += 1
  # Print the result onto the standard output.
  print(result)


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
1
3
6
Output:
Case #1: 1
Case #2: 1
Case #3: 2
"""