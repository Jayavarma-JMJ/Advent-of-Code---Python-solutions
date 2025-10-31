## AOC Day 1

clue = input("Paste:")
j = 0
counter = 0
for i in clue:
    if i == "(":
        j=j+1
    if i == ")":
        j=j-1
    counter += 1
    print(f"val {i} loop {j}")
    if j== -1:
        break
print(j)
print(counter)
