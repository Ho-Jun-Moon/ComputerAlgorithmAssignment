class Cell:
  def __init__(self, operator = None, max = None, min = None):
    self.operator_ = operator
    self.max = max
    self.min = min

  def __str__(self):
    return f"operator : {self.operator_} max : {self.max} min : {self.min}"
  

  def __mul__(self, another):
    if another.operator_ == '+':
      max_ = self.max + another.max
      min_ = self.min + another.min
    
    elif another.operator_ == '-':
      max_ = self.max - another.min
      min_ = self.min - another.max
    
    else:
      max_ = max([self.max * another.max, self.max * another.min, self.min * another.max, self.min * another.min])
      min_ = min([self.max * another.max, self.max * another.min, self.min * another.max, self.min * another.min])

    return Cell(self.operator_, max_, min_)    

class Algorithm:
  def input(self, inp):
    inp = inp.replace(' ', '')
    self.cells = []

    while len(inp) != 0:
      operator, digit, inp = self.split(inp)
      self.cells.append(Cell(operator, digit, digit))
      # print(f"{operator}, {digit}, {inp}")
    
    if self.cells[0].operator_ == '-':
      self.cells[0].operator_ = '+'
      self.cells[0].max = self.cells[0].max * -1
      self.cells[0].min = self.cells[0].min * -1

    self.make_table()
    # self.print_table()
    self.fill_table()
    # self.print_table()


  def split(self, arr):
    operator = '+'
    digit = 1
    first = True

    for i, char in enumerate(arr):
      if char.isdigit():
        if i == len(arr) -1:
          return operator, digit * int(char), []
        return operator, digit * int(char), arr[i+1:]
      elif first:
        first = False
        operator = char
      elif char == '-':
        digit = -1
  
  def make_table(self):
    self.table = []
    row = []

    for i, cell in enumerate(self.cells):
      for j in range(len(self.cells)):
        if i == j:
          row.append(cell)
        else:
          row.append(Cell())
      self.table.append(row)
      row = []

  def fill_table(self):
    lt = len(self.table)

    for d in range(1, lt):
      for i in range(0, lt - d):
        self.change_cell(i, i+d)
  

  def change_cell(self, i, j):
    cells_max = []
    cells_min = []

    for k in range(i, j):
      cell = self.table[i][k] * self.table[k+1][j]
      cells_max.append(cell.max)
      cells_min.append(cell.min)

    max_ = max(cells_max)
    min_ = min(cells_min)
    operator = self.table[i][i].operator_

    self.table[i][j] = Cell(operator, max_, min_)

  def out(self):
    return str(self.table[0][-1].max)

al = Algorithm()
formula = input()
al.input(formula)
print(al.out())