import random
#THIS FILE IS USED TO CREATE RANDOM PLAYER INFORMATION THAT WILL BE ENTERED INTO THE DATABASE



class Player_variables ():
    first_names = ("Jamar","Tyrell","Javon","Kameron","Aaron","Alonzo","Tay","Q","Colby","Jadyn","Polo","Kel","Lamonte","Kordell","Marcel","Malek","Quinn","Tevin","Von","Trell",
                   "Drae","Samuel","Nile","Demarcus","Justin","Jordan","Darius","Jt","Dee","Latavion","Damian","Gio","Quantavius","Cole","Mari","Kam","Tavon","Ed","Imani",
                   "Fredo","Davion","Kyree","Noel","Joe","Ken","Ramon","Uno","Ethan","Jaquan","Warren","Chris","Jack","Abner","Orion","Noah","Greg","Lucas","Peso","Pharell",
                   "Kyle","Favion","Zae","Spence","Rylo","Reggie","Davavion","Jakavious","Javarious","Pj","Dj","Zavarious","Rell","Rich","Michael","Kevin","Mo","Dontavion",
                   "Chase","Coop","Prince","Efa","Payton","Snupe","Dalvon","Oliver","Qez","Te","Ivan","Ron","Dundrel","Zay","West","Fin","Lj","Aj","Sam","Rajon","Kentrell",
                   "Camdon"," Yusef","Amarion","Flavel","Malachi","Kayten","Jaqurious","Travis","Trey","Kavarius","Wilt","Houston","Iann","Elijah","Bryson","Armon","Cid",
                   "Taylon","Pat","Po")
    
    last_names = ("Jackson","Christopher","Davis","Johnson","Parker","Palacious","Bond","Cambell","Roberts","Jefferson","Glendan","Smith","Brown","Lopez","Wilson","Roses",
                  "Taylor","Lee","Moore","Harris","Clark","Robinson","Lewis","Young","Allen","Hill","Green","Nelson","Baxter","Carter","Gomez","Adams","Evans","Parker",
                  "Cruz","Collins","Murphy","Cook","Rogers","Cooper","Howard","Cox","Wood","Bennet","Gray","Price","James","Ross","Foster","Sanders","Bills","Washington",
                  "Brax","Presely","Brunson","White","Lows","Kurr","Jefferson","Abner","Flyn","Porter","Sandler","Swift","Cage","Iverson","Bird","Frances","Paston","Suden",
                  "Luther","Freeman","Abernathy","Nash","Frezno","Mach","Maxwell","Wilks","Brands","Burrow","Kelts","Cresdan","Elain","Stakes","Heights","Sewell")
    


    age = (18,21)
    player_numbers  = (0,100)
    pg_heights = (5.6,5.7,5.8)
    sg_heights =  (5.9,'5.10') #string index turned into an int
    sf_heights = ('5.11',6.0) # sting index turned into an int 
    pf_heights  = (6.1,6.2,6.3)
    c_heights = (6.4,6.5,6.6)
    guard_weight = (130,155,180)
    spf_weight = (180,195,210) #small/power foward weight 
    center_weight = (210,235,260)
    star_rating = (1,2,3,4,5) #may be multiplied by multiplier in main program
    positions = ("PG","SG","SF","PF","C")
    builds = ("Playmaking Shooter","Perimeter-Protecting Slasher","Athletic Finisher","Inside Out Facilitator","Power Lockdown","2 Way Wing"
              ,"Stretch Four","Paint Protector","Glass Cleaning Playmaker","Back-Down Bigman")
    morals = ("Excelent","Good","Alright","Poor","Terrible")
    traits = ("","Leader","Fan favorite","Liability","Role player","Fit","Team sport") 
    team_names = ("Back Alley Ballers","High Fly Hoopers","South Side Shotcallers","Uptown Underdogs")
    skill_set = ("Sniper","Crafty","Vision","Lockdown","Hangtime","Acrobat","Board swiper","Midrange maestro","Floor general")
    years_signed = (0)
    injured = ("Not injured","Injured")
    recovery_days  = (0,5)   #Not sure how im going to do the recovery days but wil need to be added in the future 
    potentials = (1,5)
    overalls = ("",1,2,3,4,5)
    offense = (1,2,3,4,5)
    defense = (1,2,3,4,5)
    roots = ("Suburbs","Hood","Small Town","Big city","Foreigner")
    star_attribute_rating = (20,40,60,80,100)
    points = ()
    assists  = ()
    rebounds  = ()
    steals   = ()
    blocks  = ()
    turnovers = ()
    games_played  = ()
    points_per_game = ()
    assists_per_game  = ()
    steals_per_game  = ()
    blocks_per_game  = ()
    rebounds_per_game  = ()
    turnovers_per_game  = ()
    field_goal_percentage  = ()
    three_point_percentage  = ()
    star_multiplier = 20
pv = Player_variables




"""
    three = pv.star_attribute_rating[0]
    midrange = pv.star_attribute_rating[0]
    layup = pv.star_attribute_rating[0]
    dunk = pv.star_attribute_rating[0]
    handles = pv.star_attribute_rating[0]
    passing = pv.star_attribute_rating[0]
    speed = pv.star_attribute_rating[0]
    stamina = pv.star_attribute_rating[0]
    steal = pv.star_attribute_rating[0]
    block = pv.star_attribute_rating[0]
    rebounding = pv.star_attribute_rating[0]
    strength = pv.star_attribute_rating[0]
    interior_defense = pv.star_attribute_rating[0]
    perimeter_defense =  pv.star_attribute_rating[0]
"""


'''
overall = (( pv.star_rating[4] * pv.star_multiplier )-1)
print(overall)
'''

