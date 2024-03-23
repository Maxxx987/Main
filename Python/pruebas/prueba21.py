

#de ella-------------------
def draw(self, num):
    try:
        balls = random.sample(self.contents, num)
    except:
        balls = copy.deepcopy(self.contents)
    for ball in balls:
        self.contents.remove(ball)
    
    return balls
        

    
    
#mio-------------------
def draw(self, number_of_balls):
    if number_of_balls > len(self.contents):
      return self.contents
    else:

      drawn_balls = random.sample(self.contents, number_of_balls)

      for ball in self.contents:
        for drawn in drawn_balls:

          if ball == drawn:
            
            self.contents.remove(ball)

      return drawn_balls
  
#el otro-----------------------
  
def draw(self, num):
    try:
        balls = random.sample(self.contents, num)
    except:
        balls = copy.deepcopy(self.contents)
    for ball in balls:
        self.contents.remove(ball)

    return balls
  
  
  #--------------------------------------------------------------
  
  
  
  def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  successful = 0
  
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    #dic_balls = {}
    drawn_balls = hat_copy.draw(num_balls_drawn)


    #

  #   for ball in drawn_balls:
  #     dic_balls[ball] = dic_balls.get(ball, 0) + 1
    

    
  #   count = 0

  #   for key, val in dic_balls.items():
  #     k = expected_copy.get(key, 0)
  #     if val >= k:
  #       count += 1
        
        
  #   if count == len(dic_balls):
  #     successful += 1

  # probability = successful/ num_experiments

  # return probability

