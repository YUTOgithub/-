import random

def make_deck():
    suits = ['S','H','D','C']#スート（記号）の定義
    ranks = range(1,14)#ランク（数字）の定義
    deck = [(x,y) for x in ranks for y in suits]
    random.shuffle(deck)#シャッフルする
    return deck

def main ():
    turn = 1
    player_money = 100
    deck = make_deck()
    print(deck)
    while(player_money > 0):
        print("ターン：",turn)
        print("所持金：",player_money)
        turn += 1
        input("次のターンへ")
    print("ゲームオーバー")

if __name__ == "__main__":
    main()
