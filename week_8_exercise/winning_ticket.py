tickets_list = [ticket.strip() for ticket in input().split(',')]
winning_symbols = ['@', '#', '$', '^']

for ticket in tickets_list:

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    first_half = ticket[:10]
    second_half = ticket[10:]

    best_symbol = None
    first_half_streak, second_half_streak = 0, 0

    current_symbol, current_streak = None, 0
    for char in first_half:
        if char in winning_symbols:
            if char != current_symbol:
                current_symbol = char
                current_streak = 0
            current_streak += 1
            if current_streak > first_half_streak:
                first_half_streak = current_streak
                best_symbol = current_symbol
        else:
            current_streak = 0

    current_symbol, current_streak = None, 0
    for char in second_half:
        if char in winning_symbols:
            if char != current_symbol:
                current_symbol = char
                current_streak = 0
            current_streak += 1
            if current_streak > second_half_streak:
                second_half_streak = current_streak
        else:
            current_streak = 0

    if first_half_streak >= 6 and second_half_streak >= 6 and best_symbol == current_symbol:
        min_streak_length = min(first_half_streak, second_half_streak)

        if min_streak_length == 10:
            print(f"ticket \"{ticket}\" - 10{best_symbol} Jackpot!")
        else:
            print(f"ticket \"{ticket}\" - {min_streak_length}{best_symbol}")
    else:
        print(f"ticket \"{ticket}\" - no match")
