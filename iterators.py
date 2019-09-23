#top ten iterators (creating iterators)


class iterators:
  
  def __init__(self):
    self.num = 1
   
  def __iter__(self):
    return self
   
  def __next__(self):
    if self.num <= 10:
      val = self.num
      self.num += 1
      return val
    else:
      raise StopIteration
      
      
      
values = iterators()

print(next(values))  #1
print(next(values))  #2
print(next(values))  #3
print(next(values))  #4
print(next(values))  #5
print(next(values))  #6
print(next(values))  #7
print(next(values))  #8
print(next(values))  #9
print(next(values))  #10
