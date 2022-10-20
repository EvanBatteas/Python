#from math import *
import random
import matplotlib.pyplot as plt
#random walk 2d
origin = [0,0]
pathx = [0]
pathy = [0]
chosen = random.randint(1,4)
if(chosen==1):
  origin[0] +=1
elif(chosen==2):
  origin[1] +=1
elif(chosen==3):
  origin[0] -= 1
elif(chosen==4):
  origin[1] -=1 
else:
  print("Out of Range")
print(origin)
pathx.append(origin[0])
pathy.append(origin[1])
atorigin = True  
multiplier = 1
x=0
try:
 while(atorigin):
  distance = (origin[0] **2 + origin[1] **2)**.5 - 100 * multiplier
  if(distance > 100):
    multiplier = 2 +x
    x+=1
  elif(distance < 100):
    multiplier = 1 
    x = 0
  chosen = random.randint(1,4)
  if(chosen==1):
   origin[0] +=1 * multiplier
  elif(chosen==2):
   origin[1] +=1 * multiplier
  elif(chosen==3):
   origin[0] -= 1* multiplier
  elif(chosen==4):
   origin[1] -=1 * multiplier
  else:
   print("Out of Range")
  pathx.append(origin[0])
  pathy.append(origin[1])
  #plt.plot(pathx,pathy) 
  if(origin[0] == 0 and origin[1] == 0):
    atorigin = False 
  #print(origin)
except KeyboardInterrupt:
     plt.plot(pathx,pathy,'green') #if it takes too long to retun, i can stop it and it will plot
     plt.plot(0,0,'.',color='red')
plt.plot(pathx,pathy,'green')
plt.plot(0,0,'.',color='red')
