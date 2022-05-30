import sys

k = int(sys.stdin.readline())
D = []


while True:
  inp = sys.stdin.readline()
  if len(inp) == 0: break
  else: D.append(inp)


def bucket_finding(k):
  global D

  T_0 = [k-1, k, k+1]

  SI = [range(len(D))]
  p = 0
  T = [None for t in T_0]
  minT = k-1
  maxT = k+1

  while p < 101:
    B = []

    for I in SI:
      newB = [ [] for _ in range(27) ]

      for i in I:
        key = D[i]

        if p >= len(key):
          newB[0].append(i)
        else:
          newB[ord(key[p]) - ord('a') + 1].append(i)
      
      for b in newB:
        if len(b) > 0 : B.append(b)


    SI = []
    tot = 0

    for i in range(len(B)):
      tot += len(B[i])

      check = True
      for j in range(len(T)):
        if not T[j] is None: continue
        else:  
          if tot == T_0[j] and len(B[i]) == 1:
            T[j] = B[i][0]

          else: check = False
      
      if check:
        return [ t+1 for t in T]
      
      T_None = [T_0[j] for j in range(len(T)) if T[j] is None]
      if len(T_None) >0 :
        minT = min(T_None)
        maxT = max(T_None)

      if tot > maxT:
        while tot >= minT:
          SI = [B[i]] + SI
          tot -= len(B[i])

          if i == 0: break
          else: i -= 1
        break
    
    
    T_0 = [ t - tot for t in T_0]
    p += 1



answer = bucket_finding(k)
for a in answer:
  print(a)