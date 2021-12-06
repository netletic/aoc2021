from functools import lru_cache
from statistics import median

# INPUT_S = "16,1,2,0,4,2,7,1,2,14"
with open("input.txt") as f:
    INPUT_S = f.read()

positions = [int(n) for n in INPUT_S.split(",")]
positions_range = range(min(positions), max(positions))

# part 1
distance = sum([abs(median(positions) - n) for n in positions])
print(distance)

# part 2
def gauss(n):
    return int(n * (n + 1) / 2)


fuel_spent = []
for pos in positions_range:
    fuel_spent.append(
        sum([(abs(n - pos) * (abs(pos - n) + 1) // 2) for n in positions])
    )
print(min(fuel_spent))
