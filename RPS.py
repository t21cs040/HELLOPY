import random

def get_hand_name(hand):
    if hand == 0:
        return "グー"
    elif hand == 1:
        return "チョキ"
    elif hand == 2:
        return "パー"

def determine_winner(hand_a, hand_b):
    if hand_a == hand_b:
        return "引き分け"
    elif (hand_a == 0 and hand_b == 1) or (hand_a == 1 and hand_b == 2) or (hand_a == 2 and hand_b == 0):
        return "Aの勝ち"
    else:
        return "Bの勝ち"

# AとBの手をランダムに決定
hand_a = random.randint(0, 2)
hand_b = random.randint(0, 2)

hand_a_name = get_hand_name(hand_a)
hand_b_name = get_hand_name(hand_b)
winner = determine_winner(hand_a, hand_b)

# 結果を表示
print(f"Aの手︓{hand_a_name} v.s. Bの手︓{hand_b_name} → {winner}")

