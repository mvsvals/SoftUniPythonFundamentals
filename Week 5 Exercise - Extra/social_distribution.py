# On the first line, you will be given the population (numbers separated by comma and space ", ").
# On the second line, you will be given the minimum wealth.
# You should distribute the wealth so that no part of the population has less than the minimum wealth.
# To do that, you should always take wealth from the wealthiest part of the population.
# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible".

population_wealth = [int(number) for number in input().split(', ')]
minimum_wealth = int(input())

for index, person_wealth in enumerate(population_wealth, start=0):
    if sum(population_wealth) < (minimum_wealth * len(population_wealth)):
        print('No equal distribution possible')
        exit()
    if person_wealth < minimum_wealth:
            population_wealth[index] += minimum_wealth - person_wealth
            wealthiest_person_index = population_wealth.index(max(population_wealth))
            population_wealth[wealthiest_person_index] -= minimum_wealth - person_wealth


print(population_wealth)
