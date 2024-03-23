import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.kwargs = kwargs
    self.contents = []
    if kwargs:
      for key, value in self.kwargs.items():
        for i in range(value):
          self.contents.append(str(key))
    else:
      return None
    
  def draw(self, number_of_balls):
    if number_of_balls > len(self.contents):
      return self.contents
    else:
      list1 = self.contents
      
      drawn_balls = []
      drawn_balls = random.sample(list1, number_of_balls)

      for ball in list1:
        for drawn in drawn_balls:
          if ball == drawn:
            list1.remove(ball)
      self.contents = list1
     
      return drawn_balls
        
      



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  
  
  successful = 0
  
  for i in range(num_experiments):
    dic_balls = {}
    drawn_balls = hat.draw(num_balls_drawn)
    for ball in drawn_balls:
      dic_balls[ball] += dic_balls.get(ball, 0) +1
  
    count = 0
    
    
    for key, val in dic_balls.items():
      k = expected_balls.get(key, 0)
      if val >= k:
        count += 1
        
        
    if count == len(dic_balls):
      successful += 1

  probability = (successful/ num_experiments) * 100

  print(probability)

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    
  
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=2000)
