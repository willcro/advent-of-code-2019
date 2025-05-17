from functools import reduce
import math

def calculate_fuel(mass):
  return math.floor(mass / 3) - 2

sum = lambda a, b: a + b
lines = open("input.txt").read().split("\n");
modules = list(map(lambda str : int(str), lines))
fuel = list(map(calculate_fuel, modules))
fuel_sum = reduce(sum, fuel, 0)

print(fuel_sum)

# part 2

def calculate_fuel_total(mass):
  fuel = calculate_fuel(mass)
  if fuel <= 0:
    return 0
  return fuel + calculate_fuel_total(fuel)


fuel_total = list(map(calculate_fuel_total, modules))
fuel_total_sum = reduce(sum, fuel_total, 0)

print(fuel_total_sum)
