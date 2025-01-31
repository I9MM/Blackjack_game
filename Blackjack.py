import random

print(""" 

 .------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /  
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <   
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |                
      '------'                           |__/   

 """)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(card_list):
    score = sum(card_list)
    if 11 in card_list and score > 21:
        card_list[card_list.index(11)] = 1
        score = sum(card_list)
    return score


x = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if x == "y":
    def_cards = [random.choice(cards), random.choice(cards)]
    dealer_Cards = [random.choice(cards)]

    user_score = calculate_score(def_cards)
    dealer_score = calculate_score(dealer_Cards)

    print(f"Your cards: {def_cards} , Your Score: {user_score}")
    print(f"Dealer First Card is {dealer_Cards[0]}")

    while True:
        check = input("Type 'Hit' to get another card, type 'Deal' to pass: ").lower()

        if check == "hit":
            def_cards.append(random.choice(cards))
            user_score = calculate_score(def_cards)
            print(f"Your cards: {def_cards} , Your Score: {user_score}")

            if user_score > 21:
                print("You lose 😭 (Busted)")
                break
        else:
            while dealer_score < 17:
                dealer_Cards.append(random.choice(cards))
                dealer_score = calculate_score(dealer_Cards)

            print(f"Your Final Cards: {def_cards} , Your Score: {user_score}")
            print(f"Dealer Final Cards: {dealer_Cards} , Dealer Score: {dealer_score}")

            if dealer_score > 21:
                print("You win 😃 (Dealer Busted)")
            elif user_score > dealer_score:
                print("You win 😃")
            elif user_score < dealer_score:
                print("You lose 😭")
            else:
                print("Draw 😤")
            break

elif x == "n":
    print("Thx for playing ;] Don't forget to rate this game ")
else:
    print("Please Try again later")
