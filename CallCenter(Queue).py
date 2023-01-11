class CallCenter:
    def __init__(self):
      self.customers = []

    def is_empty(self):
      return self.customers == []

    def add(self, x):
      self.customers.insert(0, x)

    def next(self):
      return self.customers.pop()


c = CallCenter()

while True:
    n = input()
    if n == 'end':
        break
    c.add(n)

#your code goes here
time = 0
while True:
  if c.is_empty():
    break
  item = c.next()
  if item == 'general':
   time+=5
  elif item == 'technical':
   time+=10

print(time)
