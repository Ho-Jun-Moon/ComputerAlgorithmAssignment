class Job:
  def __init__(self, arr):
    self.start = int(arr[0])
    self.end = int(arr[1])
    self.pay = int(arr[2])
    self.days = self.end - self.start + 1
  
  def isIn(self, n):
    return n == self.end

  def __str__(self):
    return f"{self.start} {self.end} {self.pay}"

class Plan:
  def __init__(self):
    self.tot_pay = 0
    self.tot_days = 0
    self.first = 0
  
  def copy(self, another):
    self.tot_pay = another.tot_pay
    self.tot_days = another.tot_days


  def add_job(self, job):
    self.tot_pay += job.pay + (1-self.first) * -10
    self.tot_days += job.days


  def __lt__(self, another):
    if self.tot_pay < another.tot_pay:
      return True
    elif self.tot_pay == another.tot_pay:
      if self.tot_days > another.tot_days:
        return True
      # if self.tot_days > another.tot_days:
      #   return True
      # else:
      #   return False
    return False

  def __str__(self):
    return f"{self.tot_pay} {self.tot_days}"


class Cleaning:
  def __init__(self):
    self.plans = []
    self.jobs = []
    self.max = 0
    self.first = True
    self.iter = 1


  def input(self, arr):
    split = arr.split()
    self.jobs.append(Job(split))
    if self.max < int(split[1]):
      self.max = int(split[1])
    

  def add_plan(self):
    best_plan = Plan()

    for job in self.jobs:
      if job.isIn(self.iter):
        if job.start == 1:
          tmp = Plan()
          tmp.first = 1
        else:
          tmp = Plan()
          tmp.copy(self.plans[job.start - 2])

          if tmp.tot_pay == 0 :
            tmp.first = 1
        
        # print(f"{self.iter} : {tmp} / {job}")
        tmp.add_job(job)
        # print(f"->{tmp}")
        
        if best_plan < tmp:
          best_plan = tmp

    if self.iter != 1:
      if best_plan < self.plans[self.iter - 2]:
          best_plan = self.plans[self.iter - 2]
      # print(f"{self.iter} :  {best_plan} {self.plans[self.iter - 2]} {best_plan < self.plans[self.iter - 2]}")

    self.plans.append(best_plan)
    self.iter += 1


  def create_plan(self):
    for i in range(self.max):
      self.add_plan()
    

  def out(self):
    self.create_plan()
    return str(self.plans[-1])

  def reset(self):
    self.plans = []
    self.jobs = []
    self.max = 0
    self.first = True
    self.iter = 1
  

cleaning = Cleaning()
num = int(input())
for i in range(num):
  cleaning.input(input())

print(cleaning.out())
