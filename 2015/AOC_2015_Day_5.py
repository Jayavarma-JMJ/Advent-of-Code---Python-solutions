vowel = 0
rep = 0
twice = 0
naughty = 0
nice = 0
phrase = ""

with open('Nicenaughty.txt','r') as file:
    for phrasespace in file:
        twice = 0
        rep = 0
        phrase = phrasespace.strip()
        phraseitr = (len(phrase))-1
        for x in range(0,phraseitr-2):
            for z in range(x+2,phraseitr):
                #print(f'{phrase[x:x+2]} == {phrase[z:z+2]}')
                if phrase[x:x+2] == phrase[z:z+2]:
                    ans = f'{phrase} with {phrase[x:x+2:]} in {x} and {phrase[z:z+2:]} in {z} '
                    twice += 1
        for l in range(0,phraseitr-1):
            if phrase[l] == phrase[l+2]:
                rep += 1
                ans2= f"{phrase} with {phrase[l+2]} in {l} and {l+2}"
                #print(ans2)
        if twice>=1 and rep>=1:
            nice +=1
            print(ans + ans2)
print(nice)
            
                    
## Code for part 1
##        for i in range(0,len(phrase)):
##            if i < len(phrase)-1 and f'{phrase[i]}{phrase[i+1]}' in ["ab", "cd", "pq", "xy"] :
##                naughty += 1
##                #print(f"Naughty", end="-")
##                break
##            else:
##                if phrase[i] in ['a','e','i','o','u']:
##                    vowel += 1
##                if i < len(phrase)-1 and phrase[i] == phrase[i+1]:
##                    twice += 1
##                if i == len(phrase)-1:
##                    if vowel < 3 or twice < 1:
##                        naughty += 1
##                        #print("Naughty", end="-")
##                        break
##                    if vowel >= 3 and twice >= 1:
##                        nice += 1
##                        print(f"Nice-{vowel}-{twice}---{phrase}")
##                        break
##                
##                
##       # print(f'{vowel}-{twice}---{phrase}')
##        vowel = 0
##        twice = 0
