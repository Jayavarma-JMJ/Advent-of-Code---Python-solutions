## AOC 2015 Day 3


field = {'0,0':1}
x=0
y=0
index = 1

def roam():
    val = f"{x},{y}"
    field.setdefault(val,0)
    field[val] += 1
    #print(field)

rule = input("Paste:")

santarule = rule[::2]
roborule = rule[1::2]
for i in santarule:
    if i == "^":
        y += 1
        roam()
    if i == "<":
        x -= 1
        roam()
    if i == ">":
        x += 1
        roam()
    if i == "v":
        y -= 1
        roam()

x=0
y=0

for i in roborule:
    if i == "^":
        y += 1
        roam()
    if i == "<":
        x -= 1
        roam()
    if i == ">":
        x += 1
        roam()
    if i == "v":
        y -= 1
        roam()

print(len(field))
