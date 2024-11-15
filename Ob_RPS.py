import random

class Player:
    '''
    プレイヤークラスのコンストラクタ
    引数： name プレイヤーの名前
    '''
    def __init__(self, name):
        self._name = name
        self._wincount = 0
    '''
    じゃんけんの手を出す関数：
    0, 1, 2 をランダムに出力する
    '''
    def show_hand(self):
        return random.randrange(3)
    
    '''
    審判から勝敗を聞く
    '''
    def notify_result(self, result):
        if True == result:
            self._wincount += 1
    '''
    自分の勝ちの数を答える
    '''
    def get_wincount(self):
        return self._wincount
    '''
    名前を答える（表示する）
    '''
    def get_name(self):
        return self._name
    

class Judge:

# 審判クラスのコンストラクタなし

    '''
    じゃんけんの手と数値の対応（クラス定数として定義）
    グー = 0
    チョキ = 1
    パー = 2
    '''

    def print_hand(self, hand):
        if hand == 0:
            return 'グー'
        elif hand == 1:
            return 'チョキ'
        elif hand == 2:
            return 'パー'
    
    '''
    じゃんけんを一回実行して、勝者を返す
    '''
    def judge_janken(self, player1, player2):
        winner = None
    
        player1Hand = player1.show_hand()
        player2Hand = player2.show_hand()
        print(player1.get_name(),'：',Judge.print_hand(self,player1Hand), \
            ' v.s. ', \
            player2.get_name(),'：',Judge.print_hand(self, player2Hand) )
        
        if (player1Hand == 0 and player2Hand == 1) or (player1Hand == 1 and player2Hand == 2) or \
        (player1Hand == 2 and player2Hand == 0):
            winner = player1
        elif (player2Hand == 0 and player1Hand == 1) or (player2Hand == 1 and player1Hand == 2) or \
        (player2Hand == 2 and player1Hand == 0):
            winner = player2
        
        return winner
    
    
    
    #続きは第2回2つ目の資料38ページから