import numpy as np

class Graph:
  def __init__(self, node_count):
    self.graph = np.zeros([node_count, node_count])
    self.char_int = {}
    self.i = 0
  

  def int_to_char(self, num):
    for key, value in self.char_int.items():
         if num == value:
             return key


  def assign_char_to_int(self, char):
    if not char in self.char_int.keys():
      self.char_int[char] = self.i
      self.i += 1


  def input(self, inp):
    for i in inp: self.add_edge(i)
  

  def add_edge(self, inp):
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
  

  def search(self, stack = None, trace = None, tot = None, start = False):
    if start:
      self.result = []
      self.search([self.graph.get_edge_list(0)], [0], 0)

    else:
      for node in stack[-1]:
        if node == 0:
          if (tot + self.graph.at(node, trace[-1])) == 42:
            self.result.append(trace)

          continue

        elif node in trace:
          continue

        elif not node in self.graph.get_edge_list(trace[-1]):
          continue

        elif (tot + self.graph.at(node, trace[-1])) >= 42:
          continue
          
        elif len(list(set(self.graph.get_edge_list(node)) - set(trace[1:]))) < 1:
          continue

        else:
          tot_ = tot
          trace_ = trace.copy()
          stack_ = stack.copy()

          tot_ += self.graph.at(node, trace_[-1])
          trace_.append(node)
          stack_[-1] = node
          stack_.append(self.graph.get_edge_list(node))
          self.search(stack_, trace_, tot_)


  def out(self):
    self.search(start = True)
    result = self.find_result()
    count = len(result.replace(" ", ""))
    print(count)
    print(result)

  def find_result(self):
    max_ = list(map(self.graph.int_to_char, self.result[0]))
    for i, r in enumerate(self.result[1:]):
      r = list(map(self.graph.int_to_char, r))
      if len(r) < len(max_): continue
      elif len(r) > len(max_): max_ = r
      else:
        r_str = "".join(r)
        max_str = "".join(max_)
        
        if r_str < max_str:
          max_ = r
          
    return " ".join(max_)
  

inp = input()
inp = list(map(int, inp.split()))

stack = Stack(inp[0])

inp_edges = [input() for _ in range(inp[1])]

stack.input(inp_edges)
stack.out()
