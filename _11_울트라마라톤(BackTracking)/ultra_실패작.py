import numpy as np

class Graph:
  def __init__(self, node_count):
    self.graph = np.zeros([node_count, node_count])
    self.char_int = {}
    self.i = 0

  def assign_char_to_int(self, char):
    if not char in self.char_int.keys():
      self.char_int[char] = self.i
      self.i += 1


  def input(self, inp):
    for i in inp: self.add_edge(i)
  

  def add_edge(self, inp):
    if len(inp) != 0:
      inp = inp.split()
      self.assign_char_to_int(inp[0])
      self.assign_char_to_int(inp[1])

      node1 = self.char_int[inp[0]]
      node2 = self.char_int[inp[1]]                         
      length = int(inp[2])

      self.graph[node1, node2] = self.graph[node2, node1] = length

      
  def get_edge_list(self, num):
    row = np.where(self.graph[num, :] > 0)[0]
    return list(row)

  
  def at(self, i, j):
    return self.graph[i,j]

class Stack:
  def __init__(self, node_count):
    self.graph = Graph(node_count)
    self.stack = []
  

  def input(self, inp):
    self.graph.input(inp)


  def bfs(self, node1, node2, trace):
    trace = trace.copy()

    queue = list(set(self.graph.get_edge_list(node1)) - set(trace))

    if node2 in queue:
      return True
      
    trace = trace + queue

    while len(queue) > 0:
      neiborhood = self.graph.get_edge_list(queue[0])

      if node2 in neiborhood:
        return True

      for n in neiborhood:
        if not n in trace:
          queue.append(n)
          trace.append(n)

      queue.pop(0)
    
    return False
    

  def count(self, trace):
    tot = 0

    for i in range(len(trace) - 1):
      tot += self.graph.at(trace[i], trace[i+1])

    return tot


  def dfs(self, node1 = 0, node2 = 0, stack = [], first = False):
    result = []
    edge_list = list(set(self.graph.get_edge_list(node1)) - set(stack))
    stack_candidate = [edge_list[1:]]
    stack = stack + [edge_list[0]]

    while len(stack) > 0:
      tail = stack[-1]
      neiborhood = list(set(self.graph.get_edge_list(tail)) - set(stack))

      if node2 in neiborhood:
        neiborhood.remove(node2)
        result.append(self.count([node1] + stack + [node2]))

      condition = len(neiborhood) > 0 and self.bfs(tail, 0, stack)

      if first and condition:
        possible_max_length = self.count([node1] + stack) + self.dfs(tail, stack = stack[1:-1])
        condition = condition and (possible_max_length > max(result))

      if condition :
        stack.append(neiborhood[0])
        stack_candidate.append(neiborhood[1:])

      else:
        while len(stack_candidate[-1]) == 0:
          stack.pop()
          stack_candidate.pop()

          if len(stack) == 0 or len(stack_candidate) == 0: 
            return int(max(result))
                  
        stack[-1] = stack_candidate[-1][0]
        stack_candidate[-1].pop(0)
    
    return int(max(result))


  def out(self):
    result = self.dfs(first = True)
    print(result)


inp = input()
inp = list(map(int, inp.split()))

stack = Stack(inp[0])

inp_edges = [input() for _ in range(inp[1])]

stack.input(inp_edges)
stack.out()