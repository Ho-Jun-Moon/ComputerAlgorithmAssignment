import numpy as np

class algorithm:
  def input(self, text1, text2):
    self.text1 = text1.replace('\n', '')
    self.text2 = text2.replace('\n', '')
    # print(self.text1, self.text2)
    self.text1_length = len(text1)
    self.text2_length = len(text2)
    self.table = np.array(list(text1 * self.text2_length)).reshape(self.text2_length, self.text1_length)

    for i, char in enumerate(text2):
      self.table[i, :] = np.where(self.table[i,:] == char, char, '')

    self.table = self.table.tolist()

    self.change_table()
    # self.change_cell(2, 4)

  def change_cell(self, i, j):
    max = self.table[i][j]
    origin = max

    if i == 1: 
      start_i = 0
      end_i = 1
    else: 
      start_i = i - 2
      end_i = i

    if j == 1: 
      start_j = 0
      end_j = 1
    else: 
      start_j = j - 2
      end_j = j
    
    if origin == '':
      if not self.check(i-1, j-1):
        max = self.table[i-1][j-1]
    else: 
      for x in range(start_i, end_i):
        for y in range(start_j, end_j):
          cell = self.table[x][y]

          if self.check(x,y):
            continue
          else:
            if len(cell + origin) > len(max):
              max =  cell + origin
            elif len(cell + origin) == len(max) and cell + origin < max:
              max = cell + origin

      self.table[i][j] = max

    
  
  def change_table(self):
    for i in range(1, self.text2_length):
      for j in range(1, self.text1_length):
        self.change_cell(i,j)
  
  def check(self, i, j):
    origin = self.table[i][j]
    result = False

    if i == 0:
      return result

    if i == 1: 
      start_i = 0
      end_i = 1
    else: 
      start_i = i - 2
      end_i = i

    if j == 0:
      return result

    if j == 1: 
      start_j = 0
      end_j = 1
    else: 
      start_j = j - 2
      end_j = j

    for x in range(start_i, end_i):
      for y in range(start_j, end_j):
        cell = self.table[x][y]
        if cell == origin:
          result = True
          break
    
    return result

  def out(self):
    max = self.table[-1][-1]

    for i in range(self.text2_length):
      for j in range(self.text1_length):
        cell = self.table[i][j]
        if len(cell) > len(max):
            max = cell
        elif len(cell) == len(max) and cell < max:
            max = cell

    return max


al = algorithm()
text1 = input()
text2 = input()
al.input(text1, text2)
print(al.out())