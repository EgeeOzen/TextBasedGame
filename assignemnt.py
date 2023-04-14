import tkinter 
import random
import linecache

main_window = tkinter.Tk()
main_window.title("Text-based adventure game")
main_window.geometry("400x400")
name = input("Enter your name please >>>")
money = random.randint(50,310)
point = 0
health = 1000000

inventory=[]


top_frame = tkinter.Frame(main_window)
top_frame.pack(anchor = "n")

name_label = tkinter.Label(top_frame, text = "Name: "+name,font=("Calibri,16"))
name_label.grid(row=0, column=0)
health_label = tkinter.Label(top_frame, text = "Health: "+str(health),font=("Calibri,16"))
health_label.grid(row=1, column=0)
money_label = tkinter.Label(top_frame, text = "Money: "+str(money),font=("Calibri,16"))
money_label.grid(row=0, column=1)
point_label = tkinter.Label(top_frame, text = "Point: "+str(point),font=("Calibri,16"))
point_label.grid(row=1, column=1)

def change_labels(health, money, point):   
    health_label.configure(text="Health: "+str(health))     
    money_label.configure(text="Money: "+str(money))
    point_label.configure(text="Point: "+str(point))
    
    
def change_health(file_name,new_health):
    my_file = open(file_name+".txt","r")
    whole_text = my_file.readlines()
    for idx, item in enumerate(whole_text):
        if "enemy" in item.lower():
            temp = whole_text[idx+1].strip().split(",")
            temp[2] = str(new_health)
            whole_text[idx+1] = ",".join(temp)+"\n"
            break
    my_file.close()
         
    my_file = open(file_name+".txt","w")
    for item in whole_text:
        my_file.write(item)
    my_file.close()

bottom_frame = tkinter.Frame(main_window)
bottom_frame.pack(anchor="s")


def Room1():
    with open('Room1.txt', 'r') as f:
        if len(f.read()) < 5:
            print("You Have Been In This Room, Please Choose Other One")
        else:
            with open('Room1.txt', 'r') as f:
                global money, point, health, inventory
                text_lines = f.readlines()
                print(text_lines[0].strip())
                print(text_lines[1].strip())
                enemy_line = text_lines[4].strip()
                name, damage, enemyhealth = enemy_line.split(',')
                enemy1 = {'name':(name), 'damage': int(damage), 'health': int(enemyhealth)}          
                print("Enemy Name->",enemy1['name'], "Enemy Damage->",enemy1['damage'], "Enemy Health->",enemy1['health'])
            
                print(inventory)
                a = int(input("Please Choose a weapon from your inventory: "))
                wepon = inventory[a]
                
                armor_choice = int(input("If you want to use armour please select it, if you don't want, type 9 -->"))
                if armor_choice != 9 :
                    wepon = inventory[armor_choice]
                    enemy1["damage"]=int(enemy1["damage"])/int(wepon["property"])
                    print(enemy1["damage"])
                else:
                    pass
                        
                while health > 0 or int(enemy1['health']) > 0 :
                    enemy1['health'] -= wepon["property"]
                    health -= enemy1["damage"]            
                    
                    if health <= 0 :
                        print("You Lost The Battle")
                        point -= 2
                        health = (0)
                        inventory[:]=[]
                        newhealthenemy = (enemy1["health"])
                        change_health("Room1", newhealthenemy)
                                                    
                    elif enemy1["health"] <= 0:
                        print("Congrats You Win")
                        money += 250
                        point += 5
                        with open('Room1.txt', 'r') as f:
                            map_lines = f.readlines()
                            weapon_line = map_lines[10].strip()
                            name, damage, price = weapon_line.strip().split(',')
                            weapon1 = {'name':str(name),'damage': int(damage), 'price': int(price)}
                            inventory.append(weapon1)
                            print(inventory)
                            
                            chest=input("You Win in this Room, Do You Want to Open The Treassure Chest?  yes/no--->")
                            if chest == "yes":
                                chestline = map_lines[16].strip()
                                code,chestpoint = chestline.strip().split(',')
                                chest1 = {'code':int(code),'point':int(chestpoint)}
                                keyselect=int(input("Please Select The Key From Your Inventory-->"))
                                keyeee=inventory[keyselect]
                                if keyeee["property"] == chest1["code"]:
                                    point += chest1["point"]
                                else:
                                    print("This Key Belongs to Another Chest, Please Use the Correct Key")
                                    pass
                            else:
                                pass
                            
                            with open("Room1.txt","w") as f:
                                f.truncate(0)
                                
                    else:         
                        continue
                    break
                change_labels(health, money, point)        
                if point < 0:
                    print("YOU LOST THE GAME")
                elif point >= 10:
                    print("YOU WIN THE GAME")
                
                
                
            pass

def Room2():
    with open('Room2.txt', 'r') as f:
        if len(f.read()) < 5:
            print("You Have Been In This Room, Please Choose Other One")
            with open('Room2.txt', 'r') as f:
                global money, point, health, inventory
                text_lines = f.readlines()
                print(text_lines[0].strip())
                print(text_lines[1].strip())
                enemy_line = text_lines[4].strip()
                name, damage, enemyhealth = enemy_line.split(',')
                enemy2 = {'name':(name), 'damage': int(damage), 'health': int(enemyhealth)}          
                print("Enemy Name->",enemy2['name'], "Enemy Damage->",enemy2['damage'], "Enemy Health->",enemy2['health'])
                
                print(inventory)
                a=int(input("Please Choose a weapon from your inventory: "))
                wepon = inventory[a]
                
                armor_choice = int(input("If you want to use armour please select it, if you don't want, type 9 -->"))
                if armor_choice != 9 :
                    wepon = inventory[armor_choice]
                    enemy2["damage"]=int(enemy2["damage"])/int(wepon["property"])
                    print(enemy2["damage"])
                else:
                    pass
                while health > 0 or int(enemy2['health']) > 0 :
                    enemy2['health'] -= wepon["property"]
                    health -= enemy2["damage"]            
                    
                    if health <= 0 :
                        print("You Lost The Battle")
                        point -= 2
                        health = (0)
                        inventory[:]=[]
                        newhealthenemy = (enemy2["health"])
                        change_health("Room2", newhealthenemy)
                        
                    elif enemy2["health"] <= 0:
                        print("Congrats You Win")
                        money += 50
                        point += 2
                        with open('Room2.txt', 'r') as f:
                            map_lines = f.readlines()
                            weapon2_line = map_lines[10].strip()
                            name, damage, price = weapon2_line.strip().split(',')
                            weapon2= {'name':str(name),'damage': int(damage), 'price': int(price)}
                            inventory.append(weapon2)
                            print(inventory)
                            chest=input("You Win in this Room, Do You Want to Open The Treassure Chest?  yes/no--->")
                            if chest == "yes":
                                chestline = map_lines[16].strip()
                                code,chestpoint = chestline.strip().split(',')
                                chest2 = {'code':int(code),'point':int(chestpoint)}
                                keyselect=int(input("Please Select The Key From Your Inventory-->"))
                                keyeee=inventory[keyselect]
                                if keyeee["property"] == chest2["code"]:
                                    point += chest2["point"]
                                else:
                                    print("This Key Belongs to Another Chest, Please Use the Correct Key")
                                    pass
                            else:
                                pass 
                            with open("Room2.txt","w") as f:
                                f.truncate(0)  
                    else:
                        continue
                    break
                change_labels(health, money, point)        
                if point < 0:
                    print("YOU LOST THE GAME")
                elif point >= 10:
                    print("YOU WIN THE GAME")
                
                
            pass                

def Room3():
    with open('Room3.txt', 'r') as f:
        if len(f.read()) < 5:
            print("You Have Been In This Room, Please Choose Other One")
            with open('Room3.txt', 'r') as f:
                global money, point, health, inventory
                text_lines = f.readlines()
                print(text_lines[0].strip())
                print(text_lines[1].strip())
                enemy_line = text_lines[4].strip()
                name, damage, enemyhealth = enemy_line.split(',')
                enemy3 = {'name':(name), 'damage': int(damage), 'health': int(enemyhealth)}          
                print("Enemy Name->",enemy3['name'], "Enemy Damage->",enemy3['damage'], "Enemy Health->",enemy3['health'])
            
                print(inventory)
                a=int(input("Please Choose a weapon from your inventory: "))
                wepon = inventory[a]
                
                armor_choice = int(input("If you want to use armour please select it, if you don't want, type 9 -->"))
                if armor_choice != 9 :
                    wepon = inventory[armor_choice]
                    enemy3["damage"]=int(enemy3["damage"])/int(wepon["property"])
                    print(enemy3["damage"])
                else:
                    pass
                        
                while health > 0 or int(enemy3['health']) > 0 :
                    enemy3['health'] -= wepon["property"]
                    health -= enemy3["damage"]            
                    
                    if health <= 0 :
                        print("You Lost The Battle")
                        point -= 2
                        health = (0)
                        inventory[:]=[]
                        newhealthenemy = (enemy3["health"])
                        change_health("Room3", newhealthenemy)
                        
                    elif enemy3["health"] <= 0:
                        print("Congrats You Win")
                        money += 100
                        point += 3
                        with open('Room3.txt', 'r') as f:
                            map_lines = f.readlines()
                            weapon3_line = map_lines[10].strip()
                            name, damage, price = weapon3_line.strip().split(',')
                            weapon3 = {'name':str(name),'damage': int(damage), 'price': int(price)}
                            inventory.append(weapon3)
                            print(inventory)
                            
                            healthpadline = map_lines[16].strip()
                            name,health,price = healthpadline.strip().split(',')
                            healthpad = {'name':str(name),'health': int(health), 'price': int(price)}
                            abc=input("YOU FOUND A HEALTHPAD, Do you want to use it or store it? use/store--->")
                            if abc == "use":
                                health += healthpad["health"]
                            elif abc == "store":
                                inventory.append(healthpad)
                            else:
                                pass
                            with open("Room3.txt","w") as f:
                                f.truncate(0)  
                            
                    else:
                        continue
                    break
                change_labels(health, money, point)        
                if point < 0:
                    print("YOU LOST THE GAME")
                elif point >= 10:
                    print("YOU WIN THE GAME")
                
                
                
            pass
        
def Room4():
    with open('Room3.txt', 'r') as f:
        if len(f.read()) < 5:
            print("You Have Been In This Room, Please Choose Other One")
            with open('Room3.txt', 'r') as f:
                global money, point, health, inventory
                text_lines = f.readlines()
                print(text_lines[0].strip())
                print(text_lines[1].strip())
                enemy_line = text_lines[4].strip()
                name, damage, enemyhealth = enemy_line.split(',')
                enemy4 = {'name':(name), 'damage': int(damage), 'health': int(enemyhealth)}          
                print("Enemy Name->",enemy4['name'], "Enemy Damage->",enemy4['damage'], "Enemy Health->",enemy4['health'])
            
                print(inventory)
                a=int(input("Please Choose a weapon from your inventory: "))
                wepon = inventory[a]
                
                armor_choice = int(input("If you want to use armour please select it, if you don't want, type 9 -->"))
                if armor_choice != 9 :
                    wepon = inventory[armor_choice]
                    enemy4["damage"]=int(enemy4["damage"])/int(wepon["property"])
                    print(enemy4["damage"])
                else:
                    pass
                        
                while health > 0 or int(enemy4['health']) > 0 :
                    enemy4['health'] -= wepon["property"]
                    health -= enemy4["damage"]            
                    
                    if health <= 0 :
                        print("You Lost The Battle")
                        point -= 2
                        health = (0)
                        inventory[:]=[]
                        newhealthenemy = (enemy4["health"])
                        change_health("Room4", newhealthenemy)
                        
                    elif enemy4["health"] <= 0:
                        print("Congrats You Win")
                        money += 100
                        point += 3
                        with open('Room4.txt', 'r') as f:
                            map_lines = f.readlines()
                            weapon4_line = map_lines[10].strip()
                            name, damage, price = weapon4_line.strip().split(',')
                            weapon4 = {'name':str(name),'damage': int(damage), 'price': int(price)}
                            inventory.append(weapon4)
                            print(inventory)
                            
                            key_line = map_lines[19].strip()
                            name,code,price = key_line.strip().split(',')
                            key1 = {'name':(name),'code':int(code),'price':int(price)}
                            inventory.append(key1)
                            print(inventory)
                            
                            healthpadline = map_lines[16].strip()
                            name,health,price = healthpadline.strip().split(',')
                            healthpad = {'name':str(name),'health': int(health), 'price': int(price)}
                            abc=input("YOU FOUND A HEALTHPAD, Do you want to use it or store it? use/store--->")
                            if abc == "use":
                                health += healthpad["health"]
                            elif abc == "store":
                                inventory.append(healthpad)
                            else:
                                pass
                            with open("Room2.txt","w") as f:
                                f.truncate(0)  
                            
                    else:
                        continue
                    break
                change_labels(health, money, point)        
                if point < 0:
                    print("YOU LOST THE GAME")
                elif point >= 10:
                    print("YOU WIN THE GAME")

            pass

def shop():
    global money,inventory,health
    buysell= input("Please select Wheter You Want to buy or sell-->")
    if buysell == "buy":
        shop_list=[]
        with open('Shop.txt', 'r') as f:
            lines = f.readlines()[7:16]  
            for line in lines:
                name, property, price = line.strip().split(',')
                shop1 = {'name':(name), 'property': int(property), 'price': int(price)}
                print(shop1)
                shop_list.append(shop1)  # append each item to the shop_list

        
            choice = int(input("Please Enter the Item you want to Buy 0-8---->"))
            userschoice = shop_list[choice]
        
        if money >= userschoice["price"]:
            money -= userschoice["price"]
            if choice == 6:
                health += 50
                print("Health Increased by 50")
            else:
                inventory.append(userschoice)
                print("The Item is Added to Your Inventory")

        else:
    
            print("You dont have enough Money")
    
    
    elif buysell == "sell":
        print(inventory)
        solditem = int(input("Please Select The Item You Want to Sell--->"))
        sellingitem = inventory[solditem]
        money += sellingitem["price"]
        del inventory[solditem]
    
    
    
    change_labels(health, money, point)
      
def Inventory():
    print(inventory)


R1_btn = tkinter.Button(bottom_frame,text = "Room 1", command = Room1)
R1_btn.grid(row=0, column=0)
R2_btn = tkinter.Button(bottom_frame,text = "Room 2", command = Room2)
R2_btn.grid(row=1, column=0)
R3_btn = tkinter.Button(bottom_frame,text = "Room 3", command = Room3)
R3_btn.grid(row=0, column=1)
R4_btn = tkinter.Button(bottom_frame,text = "Room 4", command = Room4)
R4_btn.grid(row=1, column=1)
shop_btn = tkinter.Button(bottom_frame,text = "SHOP", command = shop)
shop_btn.grid(row=0, column=2)
inventory_btn = tkinter.Button(bottom_frame,text = "INVENTORY", command = Inventory)
inventory_btn.grid(row=1, column=2)



main_window.mainloop()
