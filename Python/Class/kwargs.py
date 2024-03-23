
import random

random.randint()

class Hat:
  def __init__(self, **kwargs):
    self.kwargs = kwargs
    self.list = []
    
    if kwargs:
      
      for key, value in self.kwargs.items():
        for i in range(value):
          self.list.append(str(key))
        
    else:
      return None
    



hat1 = Hat()

print(hat1.list)