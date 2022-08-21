# N students
# R_j <= 2*R_i

def test():
  # Read the number of students.
  students = int(input())

  unsorted_C = list(map(int, input().split()))
  C = [(unsorted_C[i], i,0) for i in range(len(unsorted_C))]
  C.sort(key=lambda c: c[0])

  Rating_index = 0
  for i in range(len(C)):
    student_mentor = i-1
    while Rating_index < len(C) and 2*C[i][0] >= C[Rating_index][0]:
      Rating_index += 1
    student_mentor = Rating_index-1
    if student_mentor == i:
      if len(C)==1 or student_mentor == 0:
        student_mentor = -1
      else:
        student_mentor = i-1
    if student_mentor == -1:
        C[i] = (C[i][0], C[i][1], -1)
    else:
        C[i] = (C[i][0], C[i][1], C[student_mentor][0])
  C.sort(key=lambda c: c[1])
  for c in C:
    print(c[2], end=" ")
  print()


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
3
2000 1500 1900
5
1000 600 1000 2300 1800
2
2500 1200
output:
Case #1: 1900 2000 2000
Case #2: 1800 1000 1800 1800 2300
Case #3: 1200 -1
"""