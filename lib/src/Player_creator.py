import random
import Player_properties as pprops
from Player_properties import pv
from simple_colors import*
from Player_database_connector import*

#THIS FILE GENERATES RANDOM PLAYERS AND PLAYER INFO 

class Player_creator():
    
    class Player_info_vars():

        def player_info_vars_creator(position,star_rating,ai_height,ai_weight):

            global values
            first_name = pv.first_names[random.randrange(0,len(pv.first_names))]
            last_name = pv.last_names[random.randrange(0,len(pv.last_names))]   
            age = random.randint(pv.age[0],pv.age[1])
            position = position #pv.positions[0]  #pv.positions[(random.randrange(0,len(pv.positions)))] 
            moral = pv.morals[random.randrange(0,len(pv.morals))] 
            star_rating = star_rating #random.randint(pv.star_rating[0],pv.star_rating[4])  #pv.star_rating[4]
            roots = pv.roots[random.randrange(0,len(pv.roots))]
            trait = pv.traits[random.randrange(0,len(pv.traits))]
            injured = pv.injured[0]
            recovery_days = pv.recovery_days[0]
            overall =  star_rating * pv.star_multiplier 

            if  star_rating * pv.star_multiplier > 99:
                overall = 99

            if star_rating < pv.star_rating[4]:
                potential = random.randint(int(star_rating),pv.star_rating[4])
            else:
                potential = star_rating #pv.star_rating[4]

            #Height calculator -- 
            if position == pv.positions[0]:
                height = pv.pg_heights[random.randrange(0,len(pv.pg_heights))]
            elif position == pv.positions[1]:
                height = pv.sg_heights[random.randrange(0,len(pv.sg_heights))]
            elif position == pv.positions[2]:
                height = pv.sf_heights[random.randrange(0,len(pv.sf_heights))]
            elif position == pv.positions[3]:
                height = pv.pf_heights[random.randrange(0,len(pv.pf_heights))]
            elif position == pv.positions[4]:
                height = pv.c_heights[random.randrange(0,len(pv.c_heights))]

            #Weight calculator -- 
            if position == pv.positions[0]:
                if height <= pv.pg_heights[1]:
                    weight = random.randrange(pv.guard_weight[0],pv.guard_weight[1])
                else:
                    weight = random.randrange(pv.guard_weight[1],pv.guard_weight[2])
            elif position == pv.positions[1]:
                if height == pv.sg_heights[0]:
                    weight = random.randrange(pv.guard_weight[0],pv.guard_weight[1])
                else:
                    weight = random.randrange(pv.guard_weight[1],pv.guard_weight[2])
            elif position == pv.positions[2]:
                if height == pv.sf_heights[0]:
                    weight = random.randrange(pv.spf_weight[0],pv.spf_weight[1])
                else:
                    weight = random.randrange(pv.spf_weight[1],pv.spf_weight[2])
            elif position == pv.positions[3]:
                if height <= pv.pf_heights[1]:
                    weight = random.randrange(pv.spf_weight[0],pv.spf_weight[1])
                else:
                    weight = random.randrange(pv.spf_weight[1],pv.spf_weight[2])
            elif position == pv.positions[4]:
                if height <= pv.c_heights[1]:
                    weight = random.randrange(pv.center_weight[0],pv.center_weight[1])
                else:
                    weight = random.randrange(pv.center_weight[1],pv.center_weight[2])
            
            
            if ai_height == None:
                pass
            else:
                height = ai_height
            if ai_weight == None:
                pass
            else:
                weight = ai_weight
            

            #Max Attribute and skillset by build calculator ( by height and weight ) -- BUILD SYSTEM!!
            if position == pv.positions[0]: #PG builds
                if weight <= pv.guard_weight[1] and (height == pv.pg_heights[0] or height == pv.pg_heights[1]):
                    build = pv.builds[0]
                    max_three_pointer = pv.star_attribute_rating[4]
                    max_midrange = pv.star_attribute_rating[3]
                    max_layup = pv.star_attribute_rating[3]
                    max_dunk = pv.star_attribute_rating[0]  
                    max_ball_handle = pv.star_attribute_rating[4]
                    max_passing = pv.star_attribute_rating[3]
                    max_speed = pv.star_attribute_rating[4]
                    max_stamina = pv.star_attribute_rating[4]
                    max_steal = pv.star_attribute_rating[1]
                    max_block = pv.star_attribute_rating[0]
                    max_rebounding = pv.star_attribute_rating[0]
                    max_strength = pv.star_attribute_rating[0]
                    max_interior_defense = pv.star_attribute_rating[0]
                    max_perimeter_defense = pv.star_attribute_rating[2]
                    skill_set = random.choice([pv.skill_set[0],pv.skill_set[1],pv.skill_set[2]])
                else:
                    build = pv.builds[1]
                    max_three_pointer = pv.star_attribute_rating[0]
                    max_midrange = pv.star_attribute_rating[0]
                    max_layup = pv.star_attribute_rating[3]
                    max_dunk = pv.star_attribute_rating[3]
                    max_ball_handle = pv.star_attribute_rating[3]
                    max_passing = pv.star_attribute_rating[2]
                    max_speed = pv.star_attribute_rating[4]
                    max_stamina = pv.star_attribute_rating[3]
                    max_steal = pv.star_attribute_rating[2]
                    max_block = pv.star_attribute_rating[1]
                    max_rebounding = pv.star_attribute_rating[1]
                    max_strength = pv.star_attribute_rating[2]
                    max_interior_defense = pv.star_attribute_rating[2]
                    max_perimeter_defense = pv.star_attribute_rating[3]
                    skill_set = random.choice([pv.skill_set[3],pv.skill_set[5]])
            elif position == pv.positions[1]: #SG builds
                build = pv.builds[3]
                if weight <= pv.guard_weight[1] and height == pv.sg_heights[0]:
                    max_three_pointer = pv.star_attribute_rating[3]
                    max_midrange = pv.star_attribute_rating[4]
                    max_layup = pv.star_attribute_rating[2]
                    max_dunk = pv.star_attribute_rating[1]
                    max_ball_handle = pv.star_attribute_rating[3]
                    max_passing = pv.star_attribute_rating[3]
                    max_speed = pv.star_attribute_rating[3]
                    max_stamina = pv.star_attribute_rating[3]
                    max_steal = pv.star_attribute_rating[1]
                    max_block = pv.star_attribute_rating[1]
                    max_rebounding = pv.star_attribute_rating[1]
                    max_strength = pv.star_attribute_rating[1]
                    max_interior_defense = pv.star_attribute_rating[1]
                    max_perimeter_defense = pv.star_attribute_rating[2]
                    skill_set = random.choice([pv.skill_set[3],pv.skill_set[7],pv.skill_set[8]])
                else:
                    build = pv.builds[2]
                    max_three_pointer = pv.star_attribute_rating[1]
                    max_midrange = pv.star_attribute_rating[1]
                    max_layup = pv.star_attribute_rating[4]
                    max_dunk = pv.star_attribute_rating[4]
                    max_ball_handle = pv.star_attribute_rating[1]
                    max_passing = pv.star_attribute_rating[4]
                    max_speed = pv.star_attribute_rating[2]
                    max_stamina = pv.star_attribute_rating[4]
                    max_steal = pv.star_attribute_rating[2]
                    max_block = pv.star_attribute_rating[0]
                    max_rebounding = pv.star_attribute_rating[0]
                    max_strength = pv.star_attribute_rating[3]
                    max_interior_defense = pv.star_attribute_rating[1]
                    max_perimeter_defense = pv.star_attribute_rating[2]
                    skill_set = random.choice([pv.skill_set[4],pv.skill_set[5]])
            elif position == pv.positions[2]: #SF builds
                build = pv.builds[4]
                if weight <= pv.spf_weight[1] and height == pv.sf_heights[0]:
                    max_three_pointer = pv.star_attribute_rating[1]
                    max_midrange = pv.star_attribute_rating[2]
                    max_layup = pv.star_attribute_rating[1]
                    max_dunk = pv.star_attribute_rating[1]
                    max_ball_handle = pv.star_attribute_rating[2]
                    max_passing = pv.star_attribute_rating[2]
                    max_speed = pv.star_attribute_rating[2]
                    max_stamina = pv.star_attribute_rating[1]
                    max_steal = pv.star_attribute_rating[3]
                    max_block = pv.star_attribute_rating[3]
                    max_rebounding = pv.star_attribute_rating[1]
                    max_strength = pv.star_attribute_rating[2]
                    max_interior_defense = pv.star_attribute_rating[1]
                    max_perimeter_defense = pv.star_attribute_rating[3]
                    skill_set = random.choice([pv.skill_set[2],pv.skill_set[3]])
                else:
                    build = pv.builds[5]
                    max_three_pointer = pv.star_attribute_rating[1]
                    max_midrange = pv.star_attribute_rating[1]
                    max_layup = pv.star_attribute_rating[3]
                    max_dunk = pv.star_attribute_rating[2]
                    max_ball_handle = pv.star_attribute_rating[1]
                    max_passing = pv.star_attribute_rating[2]
                    max_speed = pv.star_attribute_rating[2]
                    max_stamina = pv.star_attribute_rating[2]
                    max_steal = pv.star_attribute_rating[2]
                    max_block = pv.star_attribute_rating[1]
                    max_rebounding = pv.star_attribute_rating[2]
                    max_strength = pv.star_attribute_rating[1]
                    max_interior_defense = pv.star_attribute_rating[2]
                    max_perimeter_defense = pv.star_attribute_rating[2]
                    skill_set = random.choice([pv.skill_set[3],pv.skill_set[4]])
            elif position == pv.positions[3]: #PF builds
                if weight <= pv.spf_weight[1] and height == pv.pf_heights[0] or height == pv.pf_heights[1]:
                    build = pv.builds[6]
                    max_three_pointer = pv.star_attribute_rating[3]
                    max_midrange = pv.star_attribute_rating[3]
                    max_layup = pv.star_attribute_rating[1]
                    max_dunk = pv.star_attribute_rating[0]
                    max_ball_handle = pv.star_attribute_rating[2]
                    max_passing = pv.star_attribute_rating[3]
                    max_speed = pv.star_attribute_rating[2]
                    max_stamina = pv.star_attribute_rating[2]
                    max_steal = pv.star_attribute_rating[0]
                    max_block = pv.star_attribute_rating[2]
                    max_rebounding = pv.star_attribute_rating[3]
                    max_strength = pv.star_attribute_rating[1]
                    max_interior_defense = pv.star_attribute_rating[3]
                    max_perimeter_defense = pv.star_attribute_rating[1]
                    skill_set = random.choice([pv.skill_set[0],pv.skill_set[7]])
                else:
                    build = pv.builds[7]
                    max_three_pointer = pv.star_attribute_rating[0]
                    max_midrange = pv.star_attribute_rating[1]
                    max_layup = pv.star_attribute_rating[3]
                    max_dunk = pv.star_attribute_rating[3]
                    max_ball_handle = pv.star_attribute_rating[1]
                    max_passing = pv.star_attribute_rating[2]
                    max_speed = pv.star_attribute_rating[1]
                    max_stamina = pv.star_attribute_rating[1]
                    max_steal = pv.star_attribute_rating[1]
                    max_block = pv.star_attribute_rating[3]
                    max_rebounding = pv.star_attribute_rating[2]
                    max_strength = pv.star_attribute_rating[2]
                    max_interior_defense = pv.star_attribute_rating[3]
                    max_perimeter_defense = pv.star_attribute_rating[0]
                    skill_set = random.choice([pv.skill_set[3],pv.skill_set[6]])
            elif position == pv.positions[4]: #Center builds
                build = pv.builds[8]
                if weight <= pv.center_weight[1] and height == pv.c_heights[0] or height == pv.c_heights[1]:
                    max_three_pointer = pv.star_attribute_rating[0]
                    max_midrange = pv.star_attribute_rating[1]
                    max_layup = pv.star_attribute_rating[3]
                    max_dunk = pv.star_attribute_rating[1]
                    max_ball_handle = pv.star_attribute_rating[2]
                    max_passing = pv.star_attribute_rating[1]
                    max_speed = pv.star_attribute_rating[1]
                    max_stamina = pv.star_attribute_rating[1]
                    max_steal = pv.star_attribute_rating[0]
                    max_block = pv.star_attribute_rating[4]
                    max_rebounding = pv.star_attribute_rating[4]
                    max_strength = pv.star_attribute_rating[3]
                    max_interior_defense = pv.star_attribute_rating[4]
                    max_perimeter_defense = pv.star_attribute_rating[1]
                    skill_set = random.choice([pv.skill_set[3],pv.skill_set[6]])
                else:
                    build = pv.builds[9]
                    max_three_pointer = pv.star_attribute_rating[0]
                    max_midrange = pv.star_attribute_rating[0]
                    max_layup = pv.star_attribute_rating[3]
                    max_dunk = pv.star_attribute_rating[4]
                    max_ball_handle = pv.star_attribute_rating[0]
                    max_passing = pv.star_attribute_rating[0]
                    max_speed = pv.star_attribute_rating[0]
                    max_stamina = pv.star_attribute_rating[0]
                    max_steal = pv.star_attribute_rating[0]
                    max_block = pv.star_attribute_rating[4]
                    max_rebounding = pv.star_attribute_rating[3]
                    max_strength = pv.star_attribute_rating[4]
                    max_interior_defense = pv.star_attribute_rating[4]
                    max_perimeter_defense = pv.star_attribute_rating[0]
                    skill_set = random.choice([pv.skill_set[4],pv.skill_set[6]])
            
            #Attribute (star_rating * multiplier) 
            if max_three_pointer > star_rating * pv.star_multiplier:
                three_pointer =  star_rating * pv.star_multiplier
            else:
                three_pointer = max_three_pointer
            if max_midrange >  star_rating * pv.star_multiplier:
                midrange =  star_rating * pv.star_multiplier
            else:
                midrange = max_midrange
            if max_layup >  star_rating * pv.star_multiplier:
                layup =  star_rating * pv.star_multiplier
            else:  
                layup = max_layup
            if max_dunk > star_rating * pv.star_multiplier:
                dunk =  star_rating * pv.star_multiplier
            else:
                dunk = max_dunk
            if max_ball_handle >  star_rating * pv.star_multiplier:
                ball_handle =  star_rating * pv.star_multiplier
            else:
                ball_handle = max_ball_handle
            if max_passing >  star_rating * pv.star_multiplier:
                passing = star_rating * pv.star_multiplier
            else:
                passing = max_passing
            if max_speed >  star_rating * pv.star_multiplier:
                speed =  star_rating * pv.star_multiplier
            else:
                speed = max_speed
            if max_stamina >  star_rating * pv.star_multiplier:
                stamina =   star_rating * pv.star_multiplier
            else:
                stamina = max_stamina
            if max_steal > star_rating * pv.star_multiplier:
                steal =  star_rating * pv.star_multiplier
            else:
                steal = max_steal
            if max_block >  star_rating * pv.star_multiplier:
                block = star_rating * pv.star_multiplier
            else:
                block = max_block
            if max_rebounding > star_rating * pv.star_multiplier:
                rebounding =  star_rating * pv.star_multiplier
            else:
                rebounding = max_rebounding
            if max_strength >  star_rating * pv.star_multiplier:
                strength =  star_rating * pv.star_multiplier
            else:
                strength = max_strength
            if max_interior_defense > star_rating * pv.star_multiplier:
                interior_defense =  star_rating * pv.star_multiplier
            else:
                interior_defense = max_interior_defense
            if max_perimeter_defense >  star_rating * pv.star_multiplier:
                perimeter_defense = star_rating * pv.star_multiplier
            else:
                perimeter_defense = max_perimeter_defense

            offense = int((three_pointer+ midrange + layup + dunk + ball_handle + passing + speed + stamina) / 6)
            defense = int((speed + stamina + steal + block + rebounding + strength + interior_defense + perimeter_defense) / 6)
            
            if offense > 99:
                offense = 99
            if defense > 99:
                defense = 99
        
            print(first_name, last_name)
            print(f"{int(star_rating)} star player") 
            print("Potential",potential,"star")
            print(cyan(build))
            print(position)
            print(height)
            print(weight)
            print("Age", age)
            print(roots)
            if trait != "":
                print(trait)
            print(injured)
            print("recovery days",recovery_days)
            print(skill_set,"skill set")
            print(overall,(yellow("ovr")))
            print(offense, (green("offense")))
            print(defense, (red("defense")))
            print(three_pointer,"three pointer")
            print(midrange,"midrange")
            print(layup,"layup")
            print(dunk,"dunk")
            print(ball_handle,"ball_handle")
            print(passing,"passing")
            print(speed,"speed")
            print(stamina,"stamina")
            print(steal,"steal")
            print(block,"block")
            print(rebounding,"rebounding")
            print(strength,"strength")
            print(interior_defense,"interior defense")
            print(perimeter_defense,"perimeter defense")
            print(moral)

            values = (first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,
                injured,recovery_days,potential,overall,offense,defense,roots,three_pointer,midrange,
                layup,dunk,ball_handle,speed,stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block)
            


        
            

    class Player_hub_inserter():
        def hub_player_inserter():
            mycursor.execute("""INSERT INTO player_hub (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            print("no errors")
            Player_creator.insert()

    
      
    class My_team_inserter():
        def my_team_player_inserter():
            Player_creator.create_ai_player(0,4,pv.pg_heights[random.randint(0,1)],random.randrange(pv.guard_weight[0],pv.guard_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO my_team (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(1,4,pv.sg_heights[0],random.randrange(pv.guard_weight[0],pv.guard_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO my_team (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(4,4,pv.c_heights[random.randint(0,1)],random.randrange(pv.center_weight[0],pv.center_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO my_team (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)
            Player_creator.insert()
            
    
            
    

    class Ai_team_inserter():
        # INSERT THIS (position,star rating,height,weight)
        def ai_team_1_inserter():
            Player_creator.create_ai_player(0,0,pv.pg_heights[random.randint(0,1)],random.randrange(pv.guard_weight[0],pv.guard_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_1 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(1,0,pv.sg_heights[0],random.randrange(pv.guard_weight[0],pv.guard_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_1 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(4,0,pv.c_heights[random.randint(0,1)],random.randrange(pv.center_weight[0],pv.center_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_1 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)   
            Player_creator.insert()

        def ai_team_2_inserter():
            Player_creator.create_ai_player(1,1,pv.sg_heights[0],random.randrange(pv.guard_weight[0],pv.guard_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_2 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(2,1,pv.sf_heights[0],random.randrange(pv.spf_weight[0],pv.spf_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_2 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(3,1,pv.pf_heights[random.randint(0,1)],random.randrange(pv.spf_weight[0],pv.spf_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_2 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)   
            Player_creator.insert()

        def ai_team_3_inserter():
            Player_creator.create_ai_player(0,2,pv.pg_heights[random.randint(0,1)],random.randrange(pv.guard_weight[0],pv.guard_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_3 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(2,2,pv.sg_heights[0],random.randrange(pv.spf_weight[0],pv.spf_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_3 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(4,2,pv.c_heights[0],random.randrange(pv.spf_weight[0],pv.spf_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_3 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)  
            Player_creator.insert()

        def ai_team_4_inserter():
            Player_creator.create_ai_player(1,3,pv.sg_heights[0],random.randrange(pv.guard_weight[0],pv.guard_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_4 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(2,3,pv.sf_heights[0],random.randrange(pv.spf_weight[0],pv.spf_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_4 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(3,3,pv.c_heights[random.randint(0,1)],random.randrange(pv.center_weight[0],pv.center_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_4 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)
            Player_creator.insert()

        def ai_team_5_inserter():
            Player_creator.create_ai_player(0,4,pv.pg_heights[random.randint(0,1)],random.randrange(pv.guard_weight[0],pv.guard_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_5 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(1,4,pv.sg_heights[0],random.randrange(pv.guard_weight[0],pv.guard_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_5 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(4,4,pv.c_heights[random.randint(0,1)],random.randrange(pv.center_weight[0],pv.center_weight[1])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_5 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)
            Player_creator.insert()

        def ai_team_6_inserter():
            Player_creator.create_ai_player(0,0,pv.pg_heights[2],random.randrange(pv.guard_weight[1],pv.guard_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_6 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(2,0,pv.sf_heights[1],random.randrange(pv.spf_weight[1],pv.spf_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_6 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(3,0,pv.pf_heights[2],random.randrange(pv.spf_weight[1],pv.spf_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_6 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)
            Player_creator.insert()
   
        def ai_team_7_inserter():
            Player_creator.create_ai_player(0,1,pv.sg_heights[1],random.randrange(pv.guard_weight[1],pv.guard_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_7 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(1,1,pv.sg_heights[1],random.randrange(pv.guard_weight[1],pv.guard_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_7 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(4,1,pv.c_heights[2],random.randrange(pv.center_weight[1],pv.center_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_7 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)
            Player_creator.insert()

        def ai_team_8_inserter():
            Player_creator.create_ai_player(1,2,pv.sg_heights[1],random.randrange(pv.guard_weight[1],pv.guard_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_8 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(2,2,pv.sf_heights[1],random.randrange(pv.spf_weight[1],pv.spf_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_8 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(3,2,pv.pf_heights[2],random.randrange(pv.spf_weight[1],pv.spf_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_8 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)
            Player_creator.insert()

        def ai_team_9_inserter():
            Player_creator.create_ai_player(0,3,pv.pg_heights[2],random.randrange(pv.guard_weight[1],pv.guard_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_9 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(1,3,pv.sg_heights[1],random.randrange(pv.guard_weight[1],pv.guard_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_9 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(4,3,pv.c_heights[2],random.randrange(pv.center_weight[1],pv.center_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_9 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)
            Player_creator.insert()
    
        def ai_team_10_inserter():
            Player_creator.create_ai_player(1,4,pv.sg_heights[1],random.randrange(pv.guard_weight[1],pv.guard_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_10 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(2,4,pv.sf_heights[1],random.randrange(pv.spf_weight[1],pv.spf_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_10 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)    
            Player_creator.insert()
            Player_creator.create_ai_player(3,4,pv.pf_heights[2],random.randrange(pv.spf_weight[1],pv.spf_weight[2])) #INSERT PLAYER POSITION AND RATING 
            mycursor.execute("""INSERT INTO ai_team_10 (
            first_name,last_name,age,height,weight,star_rating,position,build,moral,trait,skill_set,injured,recovery_days, 
            potential,overall,offense,defense,roots,three_pointer,midrange,layup,dunk,ball_handle, speed,
            stamina,passing,strength,rebounding,interior_defense,perimeter_defense,steal,block
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",values)
            Player_creator.insert()
    
    def insert():
        try:
            conn.commit()
            print("Inserted successfully")
        except:
            print("Insert unccesssful")
            conn.close()

    
   
    def create_player(position,rating,ai_height,ai_weight):
        Player_creator.Player_info_vars.player_info_vars_creator(pv.positions[position],pv.star_rating[rating],ai_height,ai_weight)
        Player_creator.Player_hub_inserter.hub_player_inserter()
        print("-------------")
    
   
    def create_ai_player(position,rating,ai_height,ai_weight):
        Player_creator.Player_info_vars.player_info_vars_creator(pv.positions[position],pv.star_rating[rating],ai_height,ai_weight)



def run():

    Player_creator.My_team_inserter.my_team_player_inserter()


    Player_creator.Ai_team_inserter.ai_team_1_inserter()                                                                                                                                                               
    Player_creator.Ai_team_inserter.ai_team_2_inserter()                                                                                                                                                              
    Player_creator.Ai_team_inserter.ai_team_3_inserter()                                                                                                                                                            
    Player_creator.Ai_team_inserter.ai_team_4_inserter()                                                                                                                                                              
    Player_creator.Ai_team_inserter.ai_team_5_inserter()                                                                                                                                                              
    Player_creator.Ai_team_inserter.ai_team_6_inserter()                                                                                                                                                              
    Player_creator.Ai_team_inserter.ai_team_7_inserter()                                                                                                                                                               
    Player_creator.Ai_team_inserter.ai_team_8_inserter()                                                                                                                                                               
    Player_creator.Ai_team_inserter.ai_team_9_inserter()                                                                                                                                                              
    Player_creator.Ai_team_inserter.ai_team_10_inserter()


    position_player_amount = 5
    player_position = 0
    player_rating = 0

    for i in range(5):
        for i in range(10):
            if player_rating > 4:
                player_rating = 0
            for i in range(position_player_amount):
                Player_creator.create_player(player_position,player_rating,None,None)
            player_rating +=1
        player_position +=1
        player_rating = 0    


run()


 

































