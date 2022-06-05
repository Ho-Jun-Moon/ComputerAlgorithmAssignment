import numpy as np
import sys

count = int(sys.stdin.readline())
P = [list(map(int, sys.stdin.readline().split())) for _ in range(count)]

def marina():
  global P

  no_answer = True

  length = len(P)
  for i in range(length):

    T = np.array(P[(i-1)%length] + [1] +  P[i] + [1] + P[(i+1)%length] + [1]).reshape(3, 3)
    signed_area = np.linalg.det(T)

    if signed_area < 0: 
      print(i+1)
      no_answer = False
  

  if no_answer: print(0)

marina()