# Create a program that checks if you can save money for a Disneyland's journey.
# You have a certain number of months during which you can collect the money.
# At the end of each month, you save 25% of the cost of the journey.
# At the beginning of every odd month (except the first one) you spent 16% of the money collected so far on clothes and shoes.
# Every 4th (fourth) month at the beginning of the month your boss gives you а bonus. It is 25% of the money collected so far.
# If you save enough money for the journey, calculate how much money will be left for the souvenirs. Then print the following:
# "Bravo! You can go to Disneyland and you will have {money}lv. for souvenirs."
# If the money saved is less, you need to calculate how much money you need. Then print the following:
# "Sorry. You need {money}lv. more."
# Both numbers should be formatted to the 2nd decimal place.



journey_cost = float(input())
months_to_collect_money = int(input())
funds_saved_per_month = 0.25 * journey_cost
total_funds_saved = 0

for month in range(1, months_to_collect_money + 1):
    if month % 2 != 0 and month != 1:
        total_funds_saved *= 0.84
    if month % 4 == 0:
        total_funds_saved *= 1.25
    total_funds_saved += funds_saved_per_month

if total_funds_saved >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {abs(total_funds_saved - journey_cost):.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {journey_cost - total_funds_saved:.2f}lv. more.")
