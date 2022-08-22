# The idea: if B has 2 same consequtive digit so A can be convert to B In condition that A is not only zeros.
# Of course if A==B from the beginning we dont need any condition on B.

# cook your dish here
def test():
 N = int(input())
 A = str(input())
 B = str(input())
 if A == B:
  print("Yes")
  return
 if A == "0" * N:
  print("No")
  return
 one_flag = False
 zero_flag = False
 for i in range(N):
  if B[i] == "0":
   if zero_flag == True:
    print("Yes")
    return
   else:
    zero_flag = True
    one_flag = False
  if B[i] == "1":
   if one_flag == True:
    print("Ye3")
    return
   else:
    zero_flag = False
    one_flag = True
 print("No")
 return

 # 1110
 # 1101


tests = int(input())
for i in range(tests):
 test()