# a = int(input("Write how many cups of coffee you will need:"))
# w = (a * 200)
# m = (a * 50)
# c = (a * 15)
# print("For ", a, "cups of coffee you will need:")
# print(w, "ml of water")
# print(m, "ml of milk")
# print(c, "of coffee beans")
# w = int(input("Write how many water of coffee you will need:"))
# m = int(input("Write how many milk of coffee you will need:"))
# c = int(input("Write how many coffee of coffee you will need:"))
# a = int(input("Write how many cups of coffee you will need:"))
# if w//200 == a and m//50 == a and c//15 == a:
#     print("Yes, I can amount of coffee")
# elif w//200 > a and m//50 > a and c//15 > a:
#     q = min(w//200, m//50, c//15)
#     N = q - a
#     print("Yes,I can make that amount of coffee(and even ", N, " more than that)")
# else:
#     q = min(w//200, m//50, c//15)
#     print("No, I can make only", q, "cups of coffee")
#
# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready")

# print("The coffee machine has:")
# print(water, "of water")
# print(milk, "of milk")
# print(coffee, "of coffee beans")
# print(cups, "of cups")
# print(money, "of money")
# water = 400
# milk = 540
# coffee = 120
# cups = 9
# money = 550
# def start():
#     water = 400
#     milk = 540
#     coffee = 120
#     cups = 9
#     money = 550
#     a = (input("Write action(buy,fill,take,remaining,exit):\n"))
#     if a == 'buy':
#         b = input("What do you want to buy? 1-espresso,2-latte,3-cappuccino,back to main menu:\n")
#         if b == '1':
#             water = (water - 250)
#             milk = (milk - 0)
#             coffee = (coffee - 16)
#             cups = (cups - 1)
#             money = (money + 4)
            # print("The coffee machine has:")
            # print(water, "of water")
            # print(milk, "of milk")
            # print(coffee, "of coffee beans")
            # print(cups, "of cups")
            # print(money, "of money")
        #     if water < 0:
        #         print("Sorry, not enough water!")
        #     elif coffee < 0:
        #         print("Sorry, not enough coffee!")
        #     elif cups < 0:
        #         print("Sorry, not enough cups!")
        #     else:
        #         print("I have enough resources, making you a coffee!")
        # if b == '2':
        #     water = (water - 350)
        #     milk = (milk - 75)
        #     coffee = (coffee - 20)
        #     cups = (cups - 1)
        #     money = (money + 7)
            # print("The coffee machine has:")
            # print(water, "of water")
            # print(milk, "of milk")
            # print(coffee, "of coffee beans")
            # print(cups, "of cups")
            # print(money, "of money")
        #     if water < 0:
        #         print("Sorry, not enough water!")
        #     elif coffee < 0:
        #         print("Sorry, not enough coffee!")
        #     elif cups < 0:
        #         print("Sorry, not enough cups!")
        #     else:
        #         print("I have enough resources, making you a coffee!")
        # if b == '3':
        #     water = (water - 200)
        #     milk = (milk - 100)
        #     coffee = (coffee - 12)
        #     cups = (cups - 1)
        #     money = (money + 6)
            # print("The coffee machine has:")
            # print(water, "of water")
            # print(milk, "of milk")
            # print(coffee, "of coffee beans")
            # print(cups, "of cups")
            # print(money, "of money")
    #         if water < 0:
    #             print("Sorry, not enough water!")
    #         elif coffee < 0:
    #             print("Sorry, not enough coffee!")
    #         elif cups < 0:
    #             print("Sorry, not enough cups!")
    #         else:
    #             print("I have enough resources, making you a coffee!")
    #     if b == 'back':
    #         start()
    #     else:
    #         start()
    # if a == 'fill':
    #     b1 = int(input("Write how many ml of water you want to add:\n"))
    #     b2 = int(input("Write how many ml of milk you want to add:\n"))
    #     b3 = int(input("Write how many grams of coffee beans you want to add:\n"))
    #     b4 = int(input("Write how many disposable coffee beans you want to add:\n"))
    #     water = (water + b1)
    #     milk = (milk + b2)
    #     coffee = (coffee + b3)
    #     cups = (cups + b4)
        # print("The coffee machine has:")
        # print(water, "of water")
        # print(milk, "of milk")
        # print(coffee, "of coffee beans")
        # print(cups, "of cups")
        # print(money, "of money")
#     if a == 'take':
#         print("I gave you", money)
#         money = (money * 0)
#     if a == 'remaining':
#         print("The coffee machine has:")
#         print(water, "of water")
#         print(milk, "of milk")
#         print(coffee, "of coffee beans")
#         print(cups, "of disposable cups")
#         print(money, "of money")
#     if a == 'exit':
#         quit()
#
#
# start()



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
            # print("The coffee machine has:")
            # print(water, "of water")
            # print(milk, "of milk")
            # print(coffee, "of coffee beans")
            # print(cups, "of cups")
            # print(money, "of money")
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
            # print("The coffee machine has:")
            # print(water, "of water")
            # print(milk, "of milk")
            # print(coffee, "of coffee beans")
            # print(cups, "of cups")
            # print(money, "of money")
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
            # print("The coffee machine has:")
            # print(water, "of water")
            # print(milk, "of milk")
            # print(coffee, "of coffee beans")
            # print(cups, "of cups")
            # print(money, "of money")
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
        # print("The coffee machine has:")
        # print(water, "of water")
        # print(milk, "of milk")
        # print(coffee, "of coffee beans")
        # print(cups, "of cups")
        # print(money, "of money")


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



