# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

def sereja_and_dima(n, cards):
    left, right = 0, n - 1
    sereja_score, dima_score = 0, 0
    isSerejaTurn = True  # True -> Sereja's turn, False -> Dima's turn

    while left <= right:
        if cards[left] > cards[right]:  # Pick the larger of the two ends
            chosen_card = cards[left]
            left += 1
        else:
            chosen_card = cards[right]
            right -= 1

        if isSerejaTurn:
            sereja_score += chosen_card
        else:
            dima_score += chosen_card

        isSerejaTurn = not isSerejaTurn  # Switch turn

    print(sereja_score, dima_score)