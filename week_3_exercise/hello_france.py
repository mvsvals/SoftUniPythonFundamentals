# You want to go to France by train, and the train ticket costs exactly 150$.
# You do not have enough money, so you decide to buy some items within your budget and then sell them at a higher price – with a 40% markup.

# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
# If the price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have to reduce the budget with its price value. If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate if the budget after selling all the items is enough to buy the train ticket.
# Input / Constraints
#     • On the 1st line, you will receive the items with their prices in the format described above – real numbers in the range [0.00……1000.00]
#     • On the 2nd line, you are going to be given the budget – a real number in the range [0.0….1000.0]
# Output
#     • First, print the list with the bought item’s new prices, formatted to the second decimal point in the following format:
# "{price1} {price2} {price3} … {priceN}"
#     • Second, print the profit, formatted to the second decimal point in the following format:
# "Profit: {profit}"
#     • Finally:
#         ◦ If the budget is enough to buy the train ticket, print: "Hello, France!"
#         ◦ Otherwise, print: "Not enough money."

item_markup = 1.4
train_ticket_price = 150

items_input = input().split('|')
total_budget = float(input())
remaining_budget = total_budget
final_list = []

for item in items_input:
    individual_item = item.split('->')
    if individual_item[0] == 'Clothes' and float(individual_item[1]) <= 50 and remaining_budget >= float(individual_item[1]):
        remaining_budget -= float(individual_item[1])
        final_list.append(float(individual_item[1]) * item_markup)
    elif individual_item[0] == 'Shoes' and float(individual_item[1]) <= 35.00 and remaining_budget >= float(individual_item[1]):
        remaining_budget -= float(individual_item[1])
        final_list.append(float(individual_item[1]) * item_markup)
    elif individual_item[0] == 'Accessories' and float(individual_item[1]) <= 20.50 and remaining_budget >= float(individual_item[1]):
        remaining_budget -= float(individual_item[1])
        final_list.append(float(individual_item[1]) * item_markup)

total_profit = sum(final_list) + remaining_budget - total_budget

final_list = [f'{item:.2f}' for item in final_list]

print(*final_list)
print(f'Profit: {total_profit:.2f}')

if total_budget + total_profit > train_ticket_price:
    print("Hello, France!")
else:
    print('Not enough money.')
