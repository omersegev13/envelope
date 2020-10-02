from envelope import Envelope
from strategy import BaseStrategy, Automatic_BaseStrategy, N_max_strategy, More_then_N_percent_group_strategy

def cls(): print ("\n" * 20)

envelopes = []
for i in range(100):
    envelopes.append(Envelope())
strategies = []
strategies.append(BaseStrategy(envelopes))                              # user select manually envelopes
strategies.append(Automatic_BaseStrategy(envelopes))                    # random selection of envelop
strategies.append(N_max_strategy(envelopes))                            # return envelope after N max values (defualt N=3)
strategies.append(More_then_N_percent_group_strategy(envelopes))        # return envelope with more money that in the highest of N% group
cls()
number_of_strategy = input("enter a number between 1-4: ")
if number_of_strategy.isdigit():
    number_of_strategy = int(number_of_strategy)
    if number_of_strategy == 1:
        strategy1 = strategies[0].perform_strategy()
    elif number_of_strategy == 2:
        strategy2 = strategies[1].perform_strategy()
    elif number_of_strategy == 3:
        strategy3 = strategies[2].perform_strategy()
    elif number_of_strategy == 4:
        strategy4 = strategies[3].perform_strategy()
    else:
        print("you must enter a number between 1-4")
else:
    pass


