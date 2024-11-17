
import re

demon_names = [name.strip() for name in input().split(',')]
demon_names.sort()

health_pattern = r'[^0-9+\-\*\.\/]'
damage_pattern = r'-?\d+\.?\d*'
adjuster_pattern = r'[\*\/]'
adjuster_value = 2

for demon in demon_names:
    health_match = re.findall(health_pattern, demon)
    health = sum(ord(x) for x in health_match)

    damage_match = re.findall(damage_pattern, demon)
    damage = sum(float(x) for x in damage_match)

    adjusters_match = re.findall(adjuster_pattern, demon)
    for adjuster in adjusters_match:
        damage = eval(f'{damage}{adjuster}{adjuster_value}')

    print(f'{demon} - {health} health, {damage:.2f} damage')

