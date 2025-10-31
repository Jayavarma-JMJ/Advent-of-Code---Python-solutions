##Code for part 1

##import re
##
##lightgrid = {}
##print("Hi")
##
##def lightcommand(x,y):
##        lightgrid.setdefault(f'{x},{y}', False)
##        if instruct == ["toggle"]: 
##                lightgrid[f'{x},{y}'] = not lightgrid[f'{x},{y}']
##        if instruct == ["off"]:
##                lightgrid[f'{x},{y}'] = False
##        if instruct == ['on']:
##                lightgrid[f'{x},{y}'] = True
##
##with open("day6.txt", 'r') as file:
##        for phrase in file:
##                #print(phrase)
##                #phrase = phrasesp.strip()
##                x=0
##                y=0
##                coord = re.findall(r"\d+",phrase)
##                instruct = re.findall(r"^\w+",phrase)
##                #print(instruct)
##                if instruct == ["turn"]:
##                        instruct = re.sub(r"^\w+\s","",phrase)
##                        instruct = re.findall(r"^\w+",instruct)
##                       #print(instruct)
##                for i in range(0,len(coord)):
##                        coord[i] = int(coord[i])
##                #print(coord)
##                for j in range(coord[0],coord[2]+1):
##                        for k in range(coord[1],coord[3]+1):
##                                lightcommand(j,k)
##                #print(lightgrid)
##
##BulbsOn = list(lightgrid.values()).count(True)
##print(BulbsOn)

import re

lightgrid = {}
print("Hi")

def lightcommand(x,y):
        lightgrid.setdefault(f'{x},{y}', 0)
        if instruct == ["toggle"]: 
                lightgrid[f'{x},{y}'] += 2
        if instruct == ["off"] and lightgrid[f'{x},{y}']>=1 :
                lightgrid[f'{x},{y}'] -= 1
        if instruct == ['on']:
                lightgrid[f'{x},{y}'] += 1

with open("day6.txt", 'r') as file:
        for phrase in file:
                #print(phrase)
                #phrase = phrasesp.strip()
                x=0
                y=0
                coord = re.findall(r"\d+",phrase)
                instruct = re.findall(r"^\w+",phrase)
                #print(instruct)
                if instruct == ["turn"]:
                       instruct = re.sub(r"^\w+\s","",phrase)
                       instruct = re.findall(r"^\w+",instruct)
                       #print(instruct)
                for i in range(0,len(coord)):
                        coord[i] = int(coord[i])
                #print(coord)
                for j in range(coord[0],coord[2]+1):
                        for k in range(coord[1],coord[3]+1):
                                lightcommand(j,k)
                #print(lightgrid)

BulbsOn = list(lightgrid.values())
print(sum(BulbsOn))
        




                
        
                    
                
