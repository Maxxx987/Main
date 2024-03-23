class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.total = 0.0

  def __repr__(self):
    stri = self.name.center(30,'*') + '\n'
    for item in self.ledger:
      description = item['description'][:23]
      stri += f'{description}{item["amount"]:>{30 -len(description)}}\n'
    stri += f'Total: {self.total}'
    return stri
    

  def deposit(self, amount, description = ''):
    self.ledger.append({'amount': amount, 'description' : description})
    self.total += amount

  def withdraw(self, amount, description = ''):
    if amount <= self.total:
      self.ledger.append({'amount': -amount, 'description' : description})
      self.total -= amount
      return True
    else:
      return False
      
    

  def get_balance(self):
    return self.total

    

  def check_funds(self, amt):
    return amt <= self.total



 
  def transfer(self, amount, destined_category):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {destined_category.name}')
      destined_category.deposit(amount, f'Transfer from {self.name}')
      return True
    else:
      return False
      
             
    

food = Category('Food')
food.deposit(80, 'milanesas dfd dfdfdf asd dfsfd')
car = Category('Car')

food.transfer(50, car)
food.withdraw(10, 'meal 1')

print(food.ledger)
print(str(food))




def create_spend_chart(categories):
  for item in categories:
    print('\nCATTTT:\n', item)
  pass
  
  s = ''
  
  for i in range(100,-1,-10):
    s += f'{i:3}|\n'
  print(s)
  
  while True:
    for i in categories:
      print(i)
    
  
    
  
l = ['car', 'albañil']

categorrrr = [car.name, food.name]

create_spend_chart(categorrrr)