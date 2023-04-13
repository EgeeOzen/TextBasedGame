import tkinter 
import random
import linecache

main_window = tkinter.Tk()
main_window.title("Text-based adventure game")
main_window.geometry("400x400")
name = input("Enter your name please >>>")
money = random.randint(50,310)
point = 0
health = 100
inventory=[]


# file = open('Room1.txt')
# content1 = file.readlines()
# print(content1)

# with open('Room1.txt', 'r') as file:
#     line_num = 1
#     for line in file:
#         if line_num == 11:
#             print(line)
#             break
#         line_num += 1

# with open('Room1.txt', 'r') as f:
#     map_lines = f.readlines()
#     weapon_line = map_lines[10].strip()
#     weapon_attrs = weapon_line.split(',')
    
#     print(weapon_attrs)

# with open('Room1.txt', 'r') as f:
#     map_lines = f.readlines()
#     weapon_line = map_lines[10].strip()
#     name, damage, price = weapon_line.strip().split(',')
#     weapon1 = {'name':str(name),'damage': int(damage), 'price': int(price)}
    
# with open('Room1.txt', 'r') as f:
#     text_lines = f.readlines()
#     enemy_line = text_lines[4].strip()
#     name, damage, health = enemy_line.split(',')
#     enemy1 = {'name':(name), 'damage': int(damage), 'health': int(health)}


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

# temp = int(input("Do you want to change points to 5?(yes-1 / no-0)"))
# if temp == 1:
#     point = 5
#     point_label.configure(text = "Point: "+str(point))

bottom_frame = tkinter.Frame(main_window)
bottom_frame.pack(anchor="s")


def Room1():
    with open('Room1.txt', 'r') as file:
        line_num = 1
        for line in file:
            print(line)
            line_num += 1
            if line_num > 2:
                break
        # print(enemy1) 
        with open('Room1.txt', 'r') as f:
            text_lines = f.readlines()
            enemy_line = text_lines[4].strip()
            name, damage, health = enemy_line.split(',')
            enemy1 = {'name':(name), 'damage': int(damage), 'health': int(health)}          
            print("Enemy Name->",enemy1['name'], "Enemy Damage->",enemy1['damage'], "Enemy Health->",enemy1['health'])
       
        global money, point, health
        health -= enemy1['damage']
        print("Your Health:", health)
        if health <= 0:
            print("You Died.")
        else:
            money -= 10
            point = 5
            change_labels(health, money, point)

        pass

def Room2():
    myfile = open("Room2.txt",'r')
    print(myfile.readline())
    print("Hello You are in Room2")
    point = 10
    change_labels(health, money, point)
    pass
def Room3():
    myfile = open("Room3.txt",'r')
    print(myfile.readline())
    print("Hello You are in Room3")
    point = 10
    change_labels(health, money, point)
    pass
def Room4():
    myfile = open("Room4.txt",'r')
    print(myfile.readline())
    print("Hello You are in Room4")
    point = 10
    change_labels(health, money, point)
    pass

def shop():
    
    weapons = {
        'knife': {'damage': 10, 'price': 50},
        'rifle': {'damage': 30, 'price': 150},
        'pistol': {'damage': 20, 'price': 100},
        'bomb': {'damage': 50, 'price': 300},
        'sniper': {'damage': 40, 'price': 250}
    }

    keys = {
        '0': {'price': 300}
    }

    healing_pads = {
        'HealingPad': {'health': 50, 'price': 100}
    }

    armours = {
        'armour1': {'durability': 2, 'price': 200},
        'armour2': {'durability': 3, 'price': 400}
    }

    print('Welcome to the shop!\n')

    print('Weapons:')
    for item in weapons:
        print(f'{item.capitalize()} - Damage: {weapons[item]["damage"]}, Price: {weapons[item]["price"]}')

    print('\nKeys:')
    for item in keys:
        print(f'{item.capitalize()} - Price: {keys[item]["price"]}')

    print('\nHealing pads:')
    for item in healing_pads:
        print(f'{item.capitalize()} - Health: {healing_pads[item]["health"]}, Price: {healing_pads[item]["price"]}')

    print('\nArmours:')
    for item in armours:
        print(f'{item.capitalize()} - Durability: {armours[item]["durability"]}, Price: {armours[item]["price"]}')

    return weapons, keys, healing_pads, armours
   
    
def Inventory():
    pass

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
inventory_btn = tkinter.Button(bottom_frame,text = "INVENTORY", command = inventory)
inventory_btn.grid(row=1, column=2)



main_window.mainloop()
