from queue import PriorityQueue
import numpy as np
from datetime import (datetime, timedelta)

class Algorithm:
  def __init__(self, count):
    self.count = count
    self.data = np.zeros([count, 5])
    self.pqueue = PriorityQueue()


  def set_(self, inp):
    self.goal_bound = list(map(int, inp.split()))
  

  def input(self, inp):
    for i, row in enumerate(inp):
      self.data[i, :] = list(map(int, row.split()))
    

  def cost(self, state, only_cost = True):
    if only_cost:
      return sum([self.data[node, 4] for node in state])
    else:
      return sum([self.data[node, :] for node in state])


  def score(self, state):
    not_state = list(set(range(self.count)) - set(state))
    not_state = self.data[not_state, :]
    not_state = not_state[:, :4] / not_state[:, 4].reshape(-1,1)

    cost = self.cost(state)

    nutrients = list(sum(self.data[node, :4] for node in state))
    for i, nutrient in enumerate(nutrients):
      d = nutrient - self.goal_bound[i]
      if d < 0:
        nut = not_state[:, i]
        nut = nut[nut != 0]
        cost += - d / np.median(nut)
        # cost += - d / np.mean(nut)

    return cost    
  

  def goal(self, state):
    nutrients = list(sum(self.data[node, :4] for node in state))
    for i, nutrient in enumerate(nutrients):
      d = nutrient - self.goal_bound[i]
      if d < 0: return False
    
    return True
  

  def get_branch(self, state):
    not_state = list(set(range(self.count)) - set(state))
    for node in not_state:
      state_tmp = state.copy()
      state_tmp = state_tmp + [node]
      score = self.score(state_tmp)
      self.pqueue.put((score, state_tmp))


  def out(self):
    self.get_branch([])
    best_solution = list(range(self.count))
    best_solution_row = self.cost(best_solution, False)

    max_time = datetime.now() + timedelta(seconds=9)

    if not self.goal(best_solution):
      return "0"

    while self.pqueue.qsize() != 0:
      state = self.pqueue.get()[1]
      state.sort()

      if self.goal(state):
        state_row = self.cost(state, False)

        if state_row[4] < best_solution_row[4]:
          best_solution = state
          best_solution_row = self.cost(best_solution, False)

        elif state_row[4] == best_solution_row[4]:
          if sum(state_row[:4]) > sum(best_solution_row[:4]):
            best_solution = state
            best_solution_row = self.cost(best_solution, False)
            
          elif sum(state_row[:4]) == sum(best_solution_row[:4]) and "".join(list(map(str, state))) < "".join(list(map(str, best_solution))):
            best_solution = state
            best_solution_row = self.cost(best_solution, False)
      
      elif self.cost(state) >= best_solution_row[4]: continue

      else:
        self.get_branch(state)
      
      if datetime.now() > max_time: break
    
    for i in range(len(best_solution)): best_solution[i] = best_solution[i] + 1
    
    return " ".join(list(map(str, best_solution)))


count = int(input())
algorithm = Algorithm(count)

inp = [input() for _ in range(count + 1)]
algorithm.set_(inp[0])
algorithm.input(inp[1:])
print(algorithm.out())