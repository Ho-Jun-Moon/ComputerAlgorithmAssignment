class algorithm:
  def input(self, inp):
    self.table = []
    self.inp = inp

    # 초기값 세팅
    for i in range(len(inp)):
      self.table.append([])

    for i in range(len(inp)):
      for j in range(i + 1):
        if i == j:
          self.table[i].append(inp[i])
        else:
          self.table[i].append('.')

    for i in range(len(inp)-1):
      if inp[i] == inp[i+1]:
        self.table[i].append(inp[i:i+2])
      else:
        self.table[i].append(min(inp[i], inp[i+1]))
  
  def secret(self, i, j):
    if self.inp[i] == self.inp[j]:
      return self.inp[i] + self.table[i+1][j-1] + self.inp[j]

    else:
      down = self.table[i+1][j]
      left = self.table[i][j-1]
      if len(down) > len(left):
        return down
      elif len(down) < len(left):
        return left
      else:
        return min(down, left)    
  
  def create_table(self):
    for delta in range(2, len(self.inp)):
      for i in range(0, len(self.inp) - delta):
        self.table[i].append(self.secret(i, i+delta))

  def out(self, inp):
    self.input(inp)
    self.create_table()

    return self.table[0][-1]

al = algorithm()
input = input()
print(al.out(input))