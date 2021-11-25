class CoffeeMachine(object):
    def __init__(self, water=400, milk=540, coffee=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money


    def start(self):
       return input("Write action(buy,fill,take,remaining,exit):\n")


    def buy(self):
        b = input("What do you want to buy? 1-espresso,2-latte,3-cappuccino,back to main menu:\n")
        if b == '1':
            self.water -= 250
            self.milk -= 0
            self.coffee -= 16
            self.cups -= 1
            self.money += 4
            if self.water < 0:
                print("Sorry, not enough water!")
            elif self.coffee < 0:
                print("Sorry, not enough coffee!")
            elif self.cups < 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
        if b == '2':
            self.water -= 350
            self.milk -= 75
            self.coffee -= 20
            self.cups -= 1
            self.money += 7
            if self.water < 0:
                print("Sorry, not enough water!")
            elif self.coffee < 0:
                print("Sorry, not enough coffee!")
            elif self.cups < 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
        if b == '3':
            self.water -= 200
            self.milk -= 100
            self.coffee -= 12
            self.cups -= 1
            self.money += 6
            if self.water < 0:
                print("Sorry, not enough water!")
            elif self.coffee < 0:
                print("Sorry, not enough coffee!")
            elif self.cups < 0:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
        if b == 'back':
            self.start()
            return self.buy()


    def fill(self):
        b1 = int(input("Write how many ml of water you want to add:\n"))
        b2 = int(input("Write how many ml of milk you want to add:\n"))
        b3 = int(input("Write how many grams of coffee beans you want to add:\n"))
        b4 = int(input("Write how many disposable coffee beans you want to add:\n"))
        self.water += b1
        self.milk += b2
        self.coffee += b3
        self.cups += b4


    def take(self):
        print("I gave you", self.money)
        self.money = (self.money * 0)


    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee, "of coffee beans")
        print(self.cups, "of disposable cups")
        print(self.money, "of money")


    def main(self):
       words = self.start()
       if words == "buy":
           self.buy()
           self.main()
       elif words == "fill":
           self.fill()
           self.main()
       elif words == "take":
           self.take()
           self.main()
       elif words == "remaining":
           self.remaining()
           self.main()
       elif words == "exit":
           quit()
       else:
           return self.main()


if __name__ == "__main__":
    d = CoffeeMachine()
    d.main()



