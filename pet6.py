class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.happiness = 5

    def eat(self):
        if self.is_alive:
            print(self.name + " says 'Mmmmmm, so good and tasty!'")
        else:
            print(self.name + " is too ded to eat.")
            
    def sleep(self):
        if self.is_alive:
            print("I'm schleeep")
        else:
            print("Sorry he is dead.")
    def play(self):
        if self.is_alive:
            print("Yeet!")
        else:
            print("Sorry he is dead.")
    def rotate_right(self):
        if self.is_alive:
            self.direction += 1

            if self.direction == 4:
                self.direction = 0
        else:
            print("Sorry he is dead.")
    def rotate_left(self):
        if self.is_alive:
            self.direction -= 1

            if self.direction == -1:
                self.direction = 3
        else:
            print("Sorry he is dead.")
    def move(self):
        if self.is_alive:
            if self.direction == 0:
                self.y += 1
            elif self.direction == 1:
                self.x += 1
            elif self.direction == 2:
                self.y -= 1
            elif self.direction == 3:
                self.x -= 1
        else:
            print("Sorry he is dead.")
    def kill(self, other):
        print(self.name + " attacks " + other.name +"!")
        print(other.name + " goes 'oof' and dies.")
        other.happiness = 0
        other.is_alive = False

    def hug(self, other):
        if self.is_alive and other.is_alive:
            print(self.name + " hugs " + other.name +"!")
            other.happiness += 1
            print(other.name + " says, 'HUG TIMES " + str(other.happiness) + "!")
        else:
            print("Sorry he is dead.")

    def kiss(self, other):
        if self.is_alive and other.is_alive == False:
            print(self.name + " kisses " + other.name + "! " + other.name + " is alive!")
            other.is_alive = True
            other.happiness = 2
            print(other.name + "'s happiness == " + str(other.happiness))
        else:
            print("Pet is already alive.")
    def punch(self, other):
        if self.is_alive and other.happiness > 0:
            print(self.name + " punches " + other.name + "!")
            other.happiness -= 1
            print(other.name + " says, 'Ouch!'")
            print(other.name + "'s happiness == " + str(other.happiness))
        elif self.is_alive and other.happiness == 0:
            print(self.name + " punches " + other.name + "!")
            other.happiness -= 1
            print(other.name + " goes 'oof' and dies.")
            other.is_alive = False
        elif self.is_alive and other.happiness < 0:
            print("Sorry he is dead")

    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"

    def status(self):
        print("Name --- " + self.name)
        print("Happiness --- " + str(self.happiness))
    
pet1 = Pet("Emma")
pet2 = Pet("Jackson")
pet3 = Pet("Enrique")

