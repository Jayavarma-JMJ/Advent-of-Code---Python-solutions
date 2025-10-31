## AOC 2015 Day 2

Stringy = []
BWH = []
Area = 0
Ribbon = 0
with open('Specs.txt', 'r') as file:
    for line in file:
        Stringy = line.strip().split('x')
        for eachnum in Stringy:
            BWH.append(int(eachnum))
        BWH.sort()
        Area = (BWH[0]*BWH[1]) + (2*BWH[0]*BWH[1]) + (2*BWH[1]*BWH[2]) + (2*BWH[0]*BWH[2]) + Area
        Ribbon = (BWH[0]*BWH[1]*BWH[2]) + (2*(BWH[0]+BWH[1])) + Ribbon
        BWH = []
print(Area)
print(f'Ribbon= {Ribbon}')
