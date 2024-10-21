

# Calculate how much plunder the pirates manage to gather.
# Each day they gather the plunder.

# Keep in mind that they attack more ships every third day and add additional plunder to their total gain, which is 50% of the daily plunder.
# Every fifth day the pirates encounter a warship, and after the battle, they lose 30% of their total plunder.

# Output
#     •  In the end, print whether the plunder was successful or not, following the format described above.
# If the gained plunder is more or equal to the target, print the following:
# "Ahoy! {totalPlunder} plunder gained."
# If the gained plunder is less than the target. Calculate the percentage left and print the following:
# "Collected only {percentage}% of the plunder."
# Both numbers should be formatted to the 2nd decimal place.

days_of_plunder = int(input())
daily_plunder = int(input())
target_plunder = float(input())
total_plunder_gathered = 0

for day in range(1, days_of_plunder + 1):
    if day % 3 == 0:
        total_plunder_gathered += 0.50 * daily_plunder
    total_plunder_gathered += daily_plunder
    if day % 5 == 0:
        total_plunder_gathered -= 0.30 * total_plunder_gathered

if total_plunder_gathered >= target_plunder:
    print(f"Ahoy! {total_plunder_gathered:.2f} plunder gained.")
else:
    percentage = total_plunder_gathered / target_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
