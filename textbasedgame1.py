from IPython.terminal.interactiveshell import InteractiveShellABC
#rpg game using emojis and stuff
#13 functions
#7 areas
#10 items
#3 npc
from IPython.display import clear_output
import sys
clear_output(wait=True)
print("W e l c o m e   T o   T h e  G a m e")
command = input("             Type Start             ")

def inventory(inv):
  lb ='['
  rb = ']'
  space = ' '
  item1 = '🦴' #0
  item2 = '🦾' #1
  item3 = '🩸' #2
  item4 = '💣' #3
  item5 = '🔥' #4
  item6 = '💕' #5
  item7 = '🍔' #6
  item8 = '🦿' #7
  item9 = '⚔' #8
  item10 = '🌲' #9
  print(lb+item1*inv[0]+rb + space + lb+item2*inv[1]+rb + space + lb+item3*inv[2]+rb + space + lb+item4*inv[3]+rb + space + lb+item5*inv[4]+rb + space + lb+item6*inv[5]+rb + space + lb+item7*inv[8]+rb
        + space + lb+item8*inv[7]+rb + space + lb+item9*inv[8]+rb + space + lb+item10*inv[9]+rb + space)


def debug(time,inv,gold,hp):
     iput = input("Which debug? ")
     if(iput=='inv'):
      print("Giving you stuff") 
      for x in range(len(inv)):
        inv[x] = 1
      inv[0] = 0
     if(iput == 'area 1'):
       area1(4,4,time,inv,gold,hp) 
     if(iput == 'area 2'):
       area2(4,4,time,inv,gold,hp)   
     if(iput == 'area 3'):
       area3(16,2,time,inv,gold,hp)
     if(iput == 'area 4'):
       area4(8,8,time,inv,gold,hp)
     if(iput == 'area 5'):
       area5(8,8,time,inv,gold,hp)
     if(iput == 'shop'):
       merchant(time,inv,gold,hp)
     if(iput == 'dragon'):
       goldarea(time,inv,gold,hp) 
def healt(inv,hp):
  heart = '♥'
  health = hp + 2*inv[5] +2*inv[1]+2*inv[7]
  print(heart*health)
  if(health<0):
    gameover(inv, 1)
    
def money(amount):
  gold = '🥇' 
  print(gold, amount)
def merchant(time, inv,gold,hp):
  area = 'merchant'
  while(area=='merchant'):
   inventory(inv)
   healt(inv,hp)
   money(gold)
   print('     🧱🧱🧱🧱🧱')
   print('     🧱???????🧱')
   print('     🧱???????🧱')
   print('🧱🧱🧱🧱🧱🧱')
   print('🚪🐱‍👤🎅' + '💕'*(1-inv[5]) + '🕸'*(inv[5]) + '🍔'*(1-inv[6]) + '🕸'*(inv[6]) + '🥇')
   print('🧱🧱🧱🧱🧱🧱')
   clear_output(wait = True) 
   command = input("What do you want to buy/sell? ")
   if(command == 'ask nicely'):
     print('You seem like a nice fellow, have this: 💕')
     inv[5] = 1
   if(command == 'threaten'):
     if(inv[8]==1):
       if(inv[5] == 1 and inv[6] == 1):
        print("I have nothing left to take... except my gold")
        gold+=1
        inv[10] -=2
       else:  
        print('You could have just asked me really nicely! Fine, take this: ' + '💕' * (1-inv[5]) + '🍔'*(1-inv[6]))
        inv[5] =1
        inv[6] = 1
        inv[10] -= 50
     else:
       print('nah')
   if(command == 'move left'):
     area3(18,1,time,inv,gold,hp)
   if(command =='ask really nicely'):
     if(inv[8]==1):
       print('Sure, have these: '+ '💕' * (1-inv[5]) + '🍔'*(1-inv[6]))
       inv[5] =1
       inv[6] = 1
       inv[10] += 9
     else:
       print('No way, not even if you had one sword.')           
   if(command == 'sell'):
     if(inv[9]==1):
      print('I will take that branch off your hands')
      gold+=5
      inv[9] = 0
      inv[10] += 1 
     else:
       print("Not interested in anything") 
   if(command=='help'):
     print("You can buy health, healing, secrets, and enhancements. This secret is for free. (6 items attainable)")    
   if(command=='buy'):
     ip = input("What are you looking to buy?")
     if(ip == 'healing'):
      if(inv[6] == 0 and gold > 4):
       print('You look hungry. Take this for 5 coins.' + '🍔'*(1-inv[6]))
       inv[6] = 1
       gold -= 5
       inv[10] +=5
      else:
        if(inv[6] ==1):
         print("You have that already") 
        else:
          print("You are broke")   
     if(ip == 'health'):
      if(inv[5] == 0 and gold > 9):
        print('You look unhealthy. Take this for 10 coins' + '💕')
        inv[5] = 1
        gold -= 10
        inv[10] +=5
      else:
        if(inv[5] ==1):
         print("You have that already") 
        else:
          print("You are broke")  
     if(ip =='secrets'):
       if(gold> 9 and inv[4] == 0):
         print("You drive a hard bargin.")
         inv[4] = 1
         gold -=10
         inv[10] += 30
       if(gold > 29 and inv[3] == 0):
         print("I didn't think you would know about this.")
         inv[3] = 1
         gold -=30
         inv[10] -= 500  
       else:
         print("Asking to buy secrets with only " , gold, " gold ? What a joke.")
     if(ip=='enhancements'):
       if(inv[1]==1 and inv[7]==1):
         print("You have everything. No more.")
       else:  
        ip2 = input("Arms or Legs? Both\'ll cost you 10 gold. ")
        if(ip2=='arms' and gold > 9 and inv[1] == 0):
          inv[1] = 1
          gold -=10
          inv[10] +=10
        if(ip2=='legs' and gold > 9 and inv[7] == 0):
          inv[7] = 1
          gold -=10 
          inv[10] +=10
        else:
          print("You are crazy")   


     else:
       print("I don't have something for that.")       

def area1(spaceleft, spaceright,time,inv,gold,hp):
  t = time
  for x in range(100):
   print((t+x), " ", spaceleft, spaceright)
   inventory(inv)
   healt(inv,hp)
   money(gold)
   print(" " + "🌲"*14)
   print("🌲"+"   "*spaceleft + "🐱‍👤"+"   "*spaceright +"🚪")
   print("🌲"*5+"   "*4 +"🌲"*4)
   clear_output(wait=True)
   command = input("What do you want to do? ")
   if(command=='help'):
     print('list of possible commands: move down/left/right/up, 0 items attainable, access to 3 areas ')
   if(command=='end'):
       gameover(inv,0)
   if(command=='move right'):
     spaceright -=1
     spaceleft+=1
     if(spaceright==-1):
       print("You've discovered a new area!")
       area = 2
       area2(0,8,(x+t),inv,gold,hp)
   if(command=='move left'):
     spaceright +=1
     spaceleft-=1
   if(command == 'move up'):
     if(inv[4] == 1):
       goldarea((x+t),inv,gold,hp)
     else:  
      print("There are trees above you...")
   if(command == 'move down'):
     if(spaceleft>=3 and spaceright>=2):
       print("You found a new area!")
       area = 3
       area3(5,13,(x+t),inv,gold,hp)   
     else:
      print("There are trees below you...") 
   if(command == 'debug'):
     iput = input("which debug?")
     if(iput=='inv'):
      print("Giving you stuff") 
      for x in range(len(inv)):
        inv[x] = 1
      inv[0] = 0
     if(iput == 'area 1'):
       area1(4,4,(x+t),inv,gold,hp) 
     if(iput == 'area 2'):
       area2(4,4,(x+t),inv,gold,hp)   
     if(iput == 'area 3'):
       area3(16,2,(x+t),inv,gold,hp)
     if(iput == 'area 4'):
       area4(8,8,(x+t),inv,gold,hp)
     if(iput == 'area 5'):
       area5(8,8,(x+t),inv,gold,hp)
     if(iput == 'shop'):
       merchant((x+t),inv,gold,hp)
     if(iput == 'dragon'):
       goldarea((x+t),inv,gold,hp)            
def area2(spaceleft, spaceright,time,inv,gold,hp):
  t = time
  th = 0
  for x in range(100):
   #print("[] "*9+"[🌲]"*inv[9]+" "+str(t+x))
   print((t+x), " ", spaceleft, spaceright)
   inventory(inv)
   healt(inv,hp)
   money(gold)
   print(" " + "🌲"*14)
   print("🚪"+"   "*spaceleft + "🐱‍👤"+"   "*spaceright +"🌲")
   print("🌲"*5+"   "*4 +"🌲"*4)
   clear_output(wait = True) 
   command = input("What do you want to do? ")
   if(command=='help'):
     print('list of possible commands: move down/left/right/up, 1 item attainable, access to 2 areas')
   if(command=='end'):
       gameover(inv,0)
   if(command=='move right'):
     spaceright -=1
     spaceleft+=1
     if(spaceright==-1):
       print("You've hit a tree! It sounds weak.")
       th+=1
       spaceright +=1
       spaceleft -=1
       if(th>=3):
         print("You've broken off a springy branch from the tree")
         inv[9] = 1
   if(command=='move left'):
     spaceright +=1
     spaceleft-=1
     if(spaceleft==-1):
       area1(8,0,(x+t),inv,gold,hp)
   if(command == 'move up'):
     print("There are trees above you...")
   if(command == 'move down'):
     if(spaceleft>=3 and spaceright>=2):
       print("You found a new area!")
       area = 3
       area3(16,2,(x+t),inv,gold,hp)  
     else:
      print("There are trees below you...")
   if(command == 'debug'):
     debug((x+t),inv,gold,hp)   
   
def area3(spaceleft, spaceright,time,inv,gold,hp):
    area = 3
    x = 0
    while(area == 3):
      x+=1
      print((time+x), " ", spaceleft, spaceright)
      inventory(inv)
      healt(inv,hp)
      money(gold)
      print(("🌲"*5+"   "*4 +"🌲"*4)*2)
      print("🚪"+"   "*spaceleft + "🐱‍👤"+"   "*spaceright +"🚪")
      print(" "+"🌲"*14 + "🌵"+"🌲"*13)
      clear_output(wait = True) 
      command = input("What do you want to do? ")
      if(command=='help'):
       print('list of possible commands: move down/left/right/up, no items attainable, access to 5 areas')
      if(command=='end'):
       gameover(inv,0)
      if(command=='move right'):
       spaceright -=1
       spaceleft+=1
       if(spaceright<=-1):
         print('You have entered the shop')
         merchant((time+x),inv,gold,hp)
      if(command=='move left'):
       spaceright +=1
       spaceleft-=1
       if(spaceleft==-1):
        area5(15,0,(x+time),inv,gold,hp)
      if(command == 'move up'):
       if(8>spaceleft>2):
         print("You've gone back to Area 1")
         area1(4,4,(x+time),inv,gold,hp) 
       if(17>spaceleft>13):
         print("You've gone to Area 2")
         area2(4,4,(x+time),inv,gold,hp)  
       else:
         print("There are trees above you...")
      if(command == 'move down'):
       if(spaceleft>=8 and spaceright>=8 and inv[9] == 1):
        print("You found a new area!")
        area = 4
        area4(8,8,(x+time),inv,gold,hp)  
       else:
        print("If only you had something to vault over the cactus...")
      if(command == 'debug'):
       debug((x+time),inv,gold,hp)  
def area4(spaceleft,spaceright,time,inv,gold,hp):
     area=4
     x = 0
     while(area==4):
      print((time+x), " ", spaceleft, spaceright)
      inventory(inv)
      healt(inv,hp)
      money(gold)
      print("🌲"*13+"🌵"+"🌲"*13)
      print("🌲"+"⚔"*(1-inv[8])+"   "*(inv[8]) +"   "*spaceleft + "🐱‍👤"+"   "*spaceright +"🌲")
      print(""+"🌲"*14 + ""+"🌲"*13) 
      clear_output(wait = True) 
      x+=1
      command = input("What do you want to do? ")
      if(command=='help'):
       print('list of possible commands: move down/left/right/up, 1 item attainable, access to 1 area')
      if(command=='end'):
       gameover(inv,0)
      if(command=='move right'):
       spaceright -=1
       spaceleft+=1
      if(command=='move left'):
       spaceright +=1
       spaceleft-=1
       if(spaceleft==-1):
        print("You picked up a sword and also another sword!")
        inv[8] = 1
      if(command == 'move up'):
       if(spaceleft>=8 and spaceright>=8 and inv[9] == 1):
         print("You went back to area 3")
         area3(9,9,(x+time),inv,gold,hp)
      if(command == 'move down'):
       print("Trees in the way")
      if(command == 'debug'):
       debug((x+time),inv,gold,hp)  
def area5(spaceleft, spaceright,time,inv,gold,hp):
  area=5
  x = 0
  while(area==5):
      print((time+x), " ", spaceleft, spaceright)
      inventory(inv)
      healt(inv,hp)
      money(gold)
      print(("🌲"*6+"🌲"*7)*2)
      print("🌲"+"☠"*(1-inv[0]) +  "   "*spaceleft + "🐱‍👤"+"   "*spaceright +"🚪")
      print(""+"🌲"*14 + ""+"🌲"*13) 
      clear_output(wait = True) 
      x+=1
      command = input("What do you want to do? ")
      if(command=='help'):
       print('list of possible commands: move down/left/right/up, 1 item attainable, access to 1 area')
      if(command=='end'):
       gameover(inv,0)
      if(command=='move right'):
       spaceright -=1
       spaceleft+=1
       if(spaceright == -1):
        area3(-1,18,(x+time), inv,gold,hp)
      if(command=='move left'):
       spaceright +=1
       spaceleft-=1
       if(spaceleft==-1):
        print("You have engaged in battle with a scary monster")
        battle((time+x),inv,gold,hp)
      if(command == 'move up'):
         print("There are trees above you...")
      if(command == 'move down'):
       print("Trees in the way")
      if(command == 'debug'):
       debug((x+time),inv,gold,hp)  
def battle(time,inv,gold,hp):
  print("Fight!")
  x = 0
  da = 0
  bonesdown = 0
  bones=[1,1,1,1]
  while((hp+2*inv[1]+2*inv[5]+2*inv[7])>0):
     x+=1
     
     
     
     if(da>=1):
      for x in range(len(bones)):
        if(bones[x]>=1 and da>=1):
          bones[x] = 0
          da-=1
          bonesdown +=1
     if(max(bones) == 0):
       print("You have defeated the monster and looted it!")
       inv[0] = 1
       gold += 3000 
       inv[10] += 100
       action = input("Continue? ")
       if(action =='no'): 
        gameover(inv,0)
       if(action=='yes'):
         area5(0,18,(time+x),inv,gold,hp)      
     print((time+x))
     inventory(inv)
     healt(inv,hp)
     money(gold)
     print("🦴"*bones[0]+"🦴"*bones[1]+"☠" + "🦴"*bones[2] + "🦴"*bones[3])
     print("            ")
     print("     🐱‍👤     ")
     command = input("Fight! ")
     clear_output(wait = True)
     if(command == 'help'):
       print("You can attack, defend, or use item") 
     if(command == 'attack'):
       if(inv[8]==1):
         print("You slash at the monster, dealing 1 bone of damage")
         print("However, it gets you back for one heart of damage")
         hp-=1
         da +=1
         if((hp+2*inv[1]+2*inv[5]+2*inv[7])<=0):
           gameover(inv,1)
       if(inv[8]==0):
         print("You punch the monster, dealing 3/4 bones of damage")
         print("However, the monster slaps you for one heart of damage")
         hp-=1
         da += 3/4
         if((hp+2*inv[1]+2*inv[5]+2*inv[7])<=0):
           gameover(inv,1)  
     if(command == 'defend'):
       print("You brace yourself as the monster hits you and deals... 0 damage")
     if(command == 'use item'):
       cm = input('Which Item? ')
       if(cm == '7'):
         if(inv[6]==1):
          hp+=2
          inv[6]  = 0
       if(cm =='3'):
         if(inv[2]==1):
           ip = input("Use Dragons Blood on yourself or the monster? ")
           if(ip =='myself'):
             hp+=20
           if(ip =='monster'):
             print("You have revived the dragon! What a noble deed.")
             inv[10] += 2500
             gameover(inv,0)
       
         else:
           print("You're out!") 
def goldarea(time,inv,gold,hp):
  area = 'gold'
  x=0
  tl = 0
  dragon = 0
  print("You have discovered the ancient stash of a dragon using Dragon Breath! Time to loot")
  while(area=='gold'):
      print((time+x), " ", spaceleft, spaceright)
      inventory(inv)
      healt(inv,hp)
      money(gold)
      print("🌲🌲🌲🌲🌲🌲🌲")
      print("🌲🥇 "+"🐉"*dragon+"        🌲")
      print("🌲🥇 🐱‍👤 🥇 🌲")
      print("🌲🌲🌲🌲🌲🌲🌲") 
      clear_output(wait = True) 
      x+=1
      command = input("What do you want to do" +"? "*(1-dragon)+"! "*dragon)
      if(command=='loot' and dragon == 0):
        gold+=3
        tl +=1
        if(tl>5):
          print("You hear the beating of wings in the distance...")
        if(tl>10):
          ("The dragon has returned!!!!!!!!!!")
          dragon = 1
      if(command =='loot' and dragon ==1):
        print("The dragon will not let you continue looting")    
      if(command=='use item'):
        if(inv[3]==1):
          print("You throw the explosive at the dragon, destroying it.")
          inv[2]=1
          inv[3] = 0
          inv[10] -= 1000
          dragon = 0
        else:
          print('You have nothing of use')
      if(command=='attack'):
        print("You charge up to the dragon and get stomped")
        hp-=6
        if((hp+2*inv[1] + 2*inv[7] + 2*inv[5])>0):
          print("The dragon is fearful of your resilience and flys away")
          dragon = 0
          tl-=10

      if(command=='leave'):
        area1(4,4,(time+x),inv,gold,hp)
      if(command=='move down'):
        area1(4,4,(time+x),inv,gold,hp)               

def gameover(inv, dead):
  print("Game Over")
  if(dead == 0):
   if(inv[10] > 1000):
    print("You achieved the Good Ending: ending 1/5")
   elif(1000>inv[10] > 100):
    print("You achieved the Pretty Swell Person Ending: ending 2/5")
   elif( 10>inv[10]>-10):
    print("You have achieved the Neutral Ending: ending 3/5")
   elif(-10>inv[10]>-200):
    print("You have achieved the Not Cool Bro Ending: ending 4/5")
   elif(inv[10]<-1000):
    print("You have achieved the Evil Ending: ending 5/5")
   else:
     print("You have achived an ending?") 
   sys.exit()      
  else:
    print("You died with a karma value of ", inv[10]) 
    sys.exit()      
if(command == 'start'):
 inv =[0,0,0,0,0,0,0,0,0,0,0]
 area = 1
 spaceleft = 4
 spaceright = 4
 gold = 1
 hp = 4
 area1(spaceleft,spaceright,0,inv,gold,hp)
else:
  print("Huh?") 
#add skills, xp, levels
