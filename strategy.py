import random
from envelope import Envelope

class BaseStrategy(Envelope):
    # constructor
    def __init__(self, envelopes):
        self.envelopes = envelopes

    def perform_strategy(self):
        """
        go through every envelope, opens it and asks the user if he wants to take money if he does, it prints the amount of money
        :self.envelopes: the list of all the envelopes
        :type self.envelopes: list
        :money: the amount of money in the envelope
        :type money: int
        :answer: the answer of the user if he wants to take the money
        :type answer: string
        """
        for i in self.envelopes:
            money = int(i.Open())
            answer = input("do you want to take the money in envelope with " + str(money) + " dollars? (Y/N) ")
            if answer == "Y" or answer == "y" or answer == "yes":
                break
        print("you got " + str(money) + " dollars")



class Automatic_BaseStrategy(BaseStrategy):
    def perform_strategy(self):
        """
        randomly chooses an envelope and prints the number of the envelope and the amount of money
        :self.envelopes: the list of all the envelopes
        :type self.envelopes: list
        :random_number: a random number, which is the number of the envelope, between 1 to 100 included
        :type random_number : int
        """
        random_number = random.randint(1, 101)
        print("the number of envelope is: " + str(random_number) + " you got " + str(self.envelopes[random_number].Open()) + " dollars")

class N_max_strategy(BaseStrategy):
    def perform_strategy(self):
        """
        takes the highest amount of money out of the percents and then takes and prints the first higher
        amount of money out of the rest of the percents, if there is not higher amount, it takes and prints
        the money from the last envelope
        :max_money: the highest amount of money out of the given percents
        :type max_money: int
        :taken_money : the amount of money in the envelope which is higher than max_money
        or the amount of money in the last envelope if there is not a higher amount of money
        :type taken_money: int
        :self.percent: the percent of the envelopes which the user wants to open, the default is 25
        :type self.percent: string and then int
        """
        max_money = 0
        taken_money = 0
        self.percent = input("how many percent of envelopes do you want to open(1-99), the default is 25")
        if self.percent.isdigit():
            self.percent = int(self.percent)
            if not ((self.percent > 0) and (self.percent < 100)):
                self.percent = 25
        else:
            self.percent = 25
        for i in range(self.percent):
            if max_money < self.envelopes[i].Open():
                max_money = self.envelopes[i].Open()
        for i in range(self.percent, 100):
            if max_money < self.envelopes[i].Open():
                taken_money = self.envelopes[i].Open()
                break
        if taken_money == 0:
            taken_money = self.envelopes[99].Open()
        print("you got " + str(taken_money) + " dollars")

class More_then_N_percent_group_strategy(BaseStrategy):
    def perform_strategy(self):
        """
        asks the user how many higher amounts of money to take before stop opening more envelopes,
        and then prints the highest amount of money, if  there is not an higher amount and it gets to the
        last envelope, it will take the money from the last envelope
        :max_money: the highest amount of money out of the given number
        :type max_money: int
        :n: number of envelopes with higher amount of money to open before stop opening envelopes,
        the default is 3
        :n: string and then int
        :count: adding one every time max_money is changed
        :type count: int
        """
        n = input("enter a number bigger than 0 and lower than 100, the default is 3")
        if n.isdigit():
            n = int(n)
            if not ((n > 0) and (n < 100)):
                n = 3
        else:
            n = 3
        max_money = self.envelopes[0].Open()
        count = 1
        for i in self.envelopes:
            if count == n:
                break
            if i.Open() > max_money:
                max_money = i.Open()
                count += 1
        print("you got " + str(max_money) + " dollars")




