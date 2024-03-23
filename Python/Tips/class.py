class Character:
    def __init__(self, health, damage, speed):
        self.healt = health
        self.damage = damage
        self.speed = speed
        
        
    def double_speed(self):
        self.speed = self.speed *2
        
warrior = Character(60, 80,90)
ninja = Character(100, 90, 60)



print(warrior.speed)
print(ninja.speed)

ninja.speed = 900

print(ninja.speed)

ninja.double_speed()

print(ninja.speed)