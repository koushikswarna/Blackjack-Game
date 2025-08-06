import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

count = 0
class Card():
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
        self.value=values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self):
        self.allcards=[]
        for suit in suits:
            for rank in ranks:
                created_card=Card(rank,suit)
                self.allcards.append(created_card)

    def shuffle1(self):
        random.shuffle(self.allcards)


my_cards=Deck()

class Chip:
    def __init__(self, starting_amount):
        self.starting_amount = starting_amount

    def bet1(self,betting_amount):
        while True:
            if self.starting_amount >=betting_amount:
                self.starting_amount-=betting_amount
                return self.starting_amount
            else:
                print('You cannot bet that much')
    def __str__(self):
        return f'Player has {self.starting_amount} chips'


class Hand:
    def __init__(self, name):
        self.cards = []
        self.name = name

    def add1(self):
            self.cards.append(my_cards.allcards.pop(0))
            return self.cards


dealer=Hand('Dealer')
player=Hand('Player')
player_chips=Chip(5)
my_cards.shuffle1()

def bet_amount():

    while True:
        try:
            amount=int(input('How many chips would you like to bet: '))
        except:
            print('Sorry, try again')
            continue
        else:
            return amount

def add():
    dealer.add1()
    dealer.add1()
    player.add1()
    player.add1()
    return player.cards,dealer.cards



print('Hello and Welcome to Blackjack!')

print('You have 5 chips to start with and you can bet as much as you like using those 5 chips')
x=True
while x:
    betting_amount=bet_amount()
    player_chips.bet1(betting_amount)
    x,y=add()
    print('These are the players cards')
    print('Card 1:'),print(x[0]), print('Card 2:'), print(x[1])

    print('These are the dealers cards')
    print('Card 1'), print(y[0]),print('Card 2:?')

    d=True
    while d:
        count=0
        for card in player.cards:
            count += card.value
        if count > 21:
            print('YOU LOSE!!!!')
            print(f'Your total count is {count}')
            print(f'The player has {player_chips.starting_amount} chips')
            d = False
            x = False
            break
        choice = input('Would you like to hit or stand')
        if choice == 'hit':
            count=0
            player.add1()
            print('Card that has been added to your hand'),print(player.cards[-1])
            for card in player.cards:
                count += card.value
            if count > 21:
                print('YOU LOSE!!!!')
                print(f'Your total count is {count}')
                print(f'The player has {player_chips.starting_amount} chips')
                d = False
                x = False
                break
            if count < 21:
                print(f'Your total count is {count}')
                print('You are fine')
                continue
        if choice == 'stand':
            print('Card 2 of the dealer:'),print(dealer.cards[1])
            while True:
                dealer.add1()
                print('Card that has been added to the hand of the dealer'),print(dealer.cards[-1])
                count=0
                for card in dealer.cards:
                    count += card.value
                if 17<count<21:
                    print(f'Your total count is {count}')
                    print('Its fine')
                    d=False
                    x=False
                    break
                if count > 21:
                    print(f'Dealer total count is {count}')
                    print('Player wins')
                    player_chips.starting_amount += 2 * betting_amount
                    print(f'The player has {player_chips.starting_amount} chips')
                    x=False
                    d=False
                    break
                if count < 17:
                    print(f'Your total count is {count}')
                    print('Dealer is fine')


        count1=0
        count2=0
        for card in dealer.cards:
            count1 += card.value
        for card in player.cards:
            count2 += card.value
        while count1<21 and count2<21:
            if count1>count2:
                print(f'Dealer wins')
                print(f'The player has {player_chips.starting_amount} chips')
                d=False
                break
            if count1<count2:
                print(f'Player wins')
                player_chips.starting_amount += 2*betting_amount
                print(player_chips.starting_amount)
                print(f'The player has {player_chips.starting_amount} chips')
                d=False
                break
            if count1==count2:
                print('Draw')
                d=False
                break















































