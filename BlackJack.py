import random 


# Attributes to build a deck of cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
             'Queen':10, 'King':10, 'Ace':11}

Playing = True


# Class to build single card
class Card():

    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        
    
    def __str__(self): 
        return  self.rank + ' of ' + self.suit
        

# Class to build deck using Card class
class Deck():
    
    
    def __init__(self):
        
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: \n '+ deck_comp
    

    def shuffle(self):
        random.shuffle(self.deck)
        
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card








# Hand calss that has attributes such as value of cards, and if there are aces 
class Hand():
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        # card passed in 
        # from Deck.deal() == single_card(suit,rank)
        
        self.cards.append(card)
        self.value += values [card.rank]
        
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self):
       
        # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE 
        # THAN CHANGE MY ACE TO BE A 1 INSTED OF 11
        while self.value > 21 and self.aces: # or self.aces > 0
            self.value -= 10
            self.aces -=1





# Chips to bet with
class Chips():
    
    def __init__(self):
        self.total = 100 # Any value you want
        self.bet = 0 
        
    def win_bet(self):
        self.total += self.bet
        
        
    def lose_bet(self):
        self.total -= self.bet


# Function to place bets
def take_bet(chips):
    
    while True:
        
        try:
            chips.bet = int(input('Please place bet: '))
        
        except:
            print('Sorry, bet must be an integer')
        
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you dont have enough chips. You only have {chips.total} to bet with.')

            else:
                break
    



# Function to hit (add card to hand)
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()



# Function that askes weather you want to hit or stand
def hit_or_stand(deck,hand):
    global Playing # to control upcoming while loop 
    
    while True:
        
        x = input('Hit or Stand? ')
        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif x[0].lower() == 's':
            print('Player Stands. Dealers Turn')
            Playing = False
            
        else:
            print('Sorry, Please enter hit or stand. ')
            continue
            
            
        break
        



# Show your cards and one of the dealers.
def show_some():
    print('\n Dealers hand: ')
    print(' <Card Hidden>')
    print('',dealer.cards[1])
    print ('\n Players hand: ', *player.cards,  sep='\n ')
    print('Players hand = ', player.value)
    
# Show all the cards
def show_all():
    print('\n Dealers hand: ', *dealer.cards, sep='\n ')
    print('Dealers hand = ', dealer.value)
    print('\n Players hand: ', *player.cards, sep='\n ')
    print('Players hand = ', player.value)
   


# Possible win or lose scenarios 
def player_busts(player,dealer,chips):
    chips.lose_bet()
    print('\nPlayer busts and has lost this hand.')

def player_wins(player,dealer,chips):
    chips.win_bet()
    print('\nPlayer has wone this hand!')

def dealer_busts(player,dealer,chips):
    chips.win_bet()
    print('\nDealer busts!\nPlayer Wins!')
    
def dealer_wins(player,dealer,chips):
    chips.lose_bet()
    print('\nDealer wins. Player has lost this hand.')
    
def push(player,dealer):
    print('\nPUSH. Dealer and Player tie. ')











           ######       Game Control ######




chips = Chips()

# Game loop where we keep playing untill the loop is broken.
while True:
    print('\n\nWelcome to BlackJack!! \n\
The goal is to beat the dealer by getting a hand as close to or euqual to 21\n\
If you go over 21 you bust!\nThe dealer must hit on anything less than 17\n\
Aces count as a 1 or 11\n\
You start with 100 chips and can bet as much or as little as you like \n\
Good Luck!!\n\n\n')
    
    
    print(f'\nPlayer has {chips.total} chips \n')
    
    # Create deck of cards for the game
    game_deck = Deck()
    game_deck.shuffle()
    
    player = Hand()
    dealer = Hand()
    
    # Deal cards to the player and dealer
    pulled_card = game_deck.deal()
    player.add_card(pulled_card)
    pulled_card = game_deck.deal()
    dealer.add_card(pulled_card)
    pulled_card = game_deck.deal()
    player.add_card(pulled_card)
    pulled_card = game_deck.deal()
    dealer.add_card(pulled_card)
    
    
    
    
    take_bet(chips)
    print('\n')
    
    
    show_some()
    print('\n')
    
    
    
    
    
    # Game loop where you hit or stand
    while Playing:
        
        hit_or_stand(game_deck,player)
        print('\n')
        
        show_some()
        print('\n')
        
        
        if player.value > 21:
            player_busts(player,dealer,chips)
            break
    
    
    if player.value <= 21:
        while dealer.value < 17:
            hit(game_deck,dealer)
            
            show_all()
            print('\n')

        # Check for possible win or lose scenarios
        if dealer.value > 21:
            dealer_busts(player,dealer,chips)

        elif player.value > dealer.value:
            player_wins(player,dealer,chips)
        
        elif dealer.value > player.value:
            dealer_wins(player,dealer,chips)

        elif player.value > 21:
            player_busts(player,dealer,chips)
            
        elif dealer.value == player.value:
            push(player,dealer)
            
            #break
            
        show_all()
        print('\n')
            
       
            
    print(f'\nPlayer has {chips.total} chips left ')

    if chips.total == 0:
        print('Looks like your out of chips! Sorry, Thanks for playing!')
        break 


    answer = input('Would you like to play again? \n')

    if answer[0].lower() == 'y':
        
        Playing = True
        chips.total = chips.total
        continue 


    else:
        print('\nThank you for playing!! ')
        break





 
		