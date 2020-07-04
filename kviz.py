import random
class Player:
    
    def __init__(self, name, points): 
        self.__name = name
        self.__points = points

    @property 
    def points(self):
        return self.__points

    @points.setter
    def points(self, answer):
        self.__points = answer

    @property 
    def name(self):
        return self.__name

    @name.setter
    def name(self, username):
        self.__name = username

def play():
    numberPlays = 0
    username1 = input('Your name: ')
    username2 = input('Your name: ')
    e1 = Player(username1, 0)
    e2 = Player(username2, 0)
    print("-" * 15)
    print("Welcome " + e1.name + " and " + e2.name)
    print("Let's play it...")
    

    while numberPlays < 8:
        randQuestion=random.randint(0,3)
        if randQuestion == 0:
            randQuestion=random.randint(1,3)
            print("-" * 15)
            print("Cat is ...")
            print("A: Animal B: Fruit C: Brand")
            key = input('Player ' + e1.name + ' answer is: ')
            if key.lower() == "a":
                print("Corect answer.")
                numberPlays += 1
                e1.points += 1
            else:
                print("Incorect answer.")
                numberPlays += 1
                e1.points -= 1
            key = input('Player ' + e2.name + ' answer is: ')
            if key.lower() == "a":
                print("Corect answer.")
                numberPlays += 1
                e2.points += 1
            else:
                print("Incorect answer.")
                numberPlays += 1
                e2.points -= 1


        if randQuestion == 1:
            print("-" * 15)
            print("Golden State Warriors are ...")
            print("A: Army B: NBA Club C: Non-profit organization")
            key = input('Player ' + e1.name + ' answer is: ')
            if key.lower() == "b":
                print("Corect answer.")
                numberPlays += 1
                e1.points += 1
            else:
                print("Incorect answer.")
                numberPlays += 1
                e1.points -= 1
            key = input('Player ' + e2.name + ' answer is: ')
            if key.lower() == "b":
                print("Corect answer.")
                numberPlays += 1
                e2.points += 1
            else:
                print("Incorect answer.")
                numberPlays += 1
                e2.points -= 1


        if randQuestion == 2:
            print("-" * 15)
            print("HTML is  ...")
            print("A: Programing language B: Markup language C: Nothing")
            key = input('Player ' + e1.name + ' answer is: ')
            if key.lower() == "b":
                print("Corect answer.")
                numberPlays += 1
                e1.points += 1
            else:
                print("Incorect answer.")
                numberPlays += 1
                e1.points -= 1
            key = input('Player ' + e2.name + ' answer is: ')
            if key.lower() == "b":
                print("Corect answer.")
                numberPlays += 1
                e2.points += 1
            else:
                print("Incorect answer.")
                numberPlays += 1
                e2.points -= 1


        if randQuestion == 3:
            print("-" * 15)
            print("Potato is  ...")
            print("A: Anime character B: Name C: Food")
            key = input('Player ' + e1.name + ' answer is: ')
            if key.lower() == "c":
                print("Corect answer.")
                numberPlays += 1
                e1.points += 1
            else:
                print("Incorect answer.")
                numberPlays += 1
                e1.points -= 1
            key = input('Player ' + e2.name + ' answer is: ')
            if key.lower() == "c":
                print("Corect answer.")
                numberPlays += 1
                e2.points += 1
            else:
                print("Incorect answer.")
                numberPlays += 1
                e2.points -= 1

    if numberPlays == 8:
        if e1.points < 0:
            e1.points = 0
        if e2.points < 0:
            e2.points = 0
        print("Player " + e1.name + " got " , e1.points , " points")
        print("Player " + e2.name + " got " , e2.points , " points")
        if e1.points > e2.points:
            print("Player " + e1.name + " won!")
        elif e1.points < e2.points:
            print("Player " + e2.name + " won!")
        elif e1.points < 0 or e2.points < 0:
            print("RIP one or both players.")
            print("Nobody won. Play again.")
        else:
            print("Nobody won. Play again.")
    
play()
