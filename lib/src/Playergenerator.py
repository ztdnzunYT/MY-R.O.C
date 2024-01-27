import random
from mysqltestconnector import*
import Player_properties as pprops 
from Player_properties import pv 

class Names():
    first_names = pprops.pv.first_names
    last_names = pprops.pv.last_names

N = Names 

def Randomizer():
    global x,y
    x = random.randint(0,len(N.first_names)-1)
    y = random.randint(0,len(N.last_names)-1)

def Randname():
    global First_name, Last_name
    First_name = N.first_names[x]
    Last_name = N.last_names[y] 
    #print(f"{First_name} {Last_name}")  

for i in range(10):
    Randomizer()
    Randname()
    INSERT(First_name,Last_name)
DELETE()
SELECT()
SHOW()

#for i in range(10):
    #Newname()
   # Randname() 


  