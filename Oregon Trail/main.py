##Quiyoshi Begay & Kade Loertscher
##The Oregon Trail
##2021
import random

creator = "Quiyoshi Begay & Kade Loertscher"
tm = "10//2021"
from LOGO import *
def letterchoice():
    while True:
        choice = input("what is your choice (Y or N)")
        if choice.lower() == "y":
            return choice.lower()
        elif choice.lower() == "n":
            return choice.lower()
        else:
            print("thats not a choice")
def vaildchoice(maxnumber):
    while True:

        choice = input("what is your choice")
        if choice.isnumeric():
            if int(choice)<= maxnumber:
                choice = int(choice)
                return choice
            else:
                print("thats not a choice")
        else:
            print("your choice needs to be a number")


def splash_screen():
    print(LOGO)
    print("t\t" + creator)
    print("t\t" + tm)
    print()
    print()
    print()
    print()

def shop(money, food, ammo, clothes, parts, oxen):
    bill = 0
    partsInventory = []
    spentOnItems = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
    choices = ["Oxen", "Food", "Ammunition", "Clothes", "Wagon Parts", "Check Out"]
    print("Before leaving Independence you should buy equipment and supplies.")
    print(str.format("You have ${:.2f} in cash to make this trip.",money))
    print("Remember you can buy supplies along the way so you don't have to spend it all now")
    input("press enter to continue")
    while True:
        spentOnItems[len(spentOnItems)-1] = bill
        print("Welcome to Eric's General Store")
        print("Here is a list of things you can buy:")
        for i in range(len(choices)-1):
            print(str.format("\t{}.{:<20} ${:<10.2f}",i+1,choices[i],spentOnItems[i]))
        print(str.format("\t{}.{:<20}","6", choices[5]))
        print(str.format("Total Bill so far ${:.2f}",bill))
        print(str.format("Total funds availble: ${:.2f}",money-bill))
        print("what would you like to buy")
        choice = vaildchoice(6)
        if choice == 1:
            #Buying oxen
            bill -= spentOnItems[0]
            oxen = 0
            spentOnItems[0] = 0.00
            print("""
            There are 2 oxen in a yoke;
            I recommend at least 3 yokes.
            I charge $40 a yoke
            """)
            print(str.format("Total Bill so far ${:.2f}", bill))
            print("how many oxes do you want(MAX 9)")
            answer = vaildchoice(9)
            cost = answer*40
            oxen = answer*2
            bill += cost
            spentOnItems[0] = cost
        elif choice == 2:
            #Buying Food
            bill -= spentOnItems[1]
            food = 0
            spentOnItems[1] = 0.00
            print("""
            I recommend you take at least 200 pounds
            of food for each person in your family.
            You'll need flour, sugar, bacon, and coffee.
            My price is 20 cents a pound. 
            """)
            print(str.format("Total Bill so far ${:.2f}", bill))
            print("how many pounds do you want(Max 9999)")
            food = vaildchoice(9999)
            foodCost = food*0.20
            bill += foodCost
            spentOnItems[1] = foodCost
        elif choice == 3:
            #Buying Ammo
            bill -= spentOnItems[2]
            ammo = 0
            spentOnItems[2] = 0.00
            print("I sell ammunition in boxes of 20 bullets. Each box costs $2.")
            print(str.format("Total Bill so far ${:.2f}", bill))
            print("how many boxes do you want(Max 99)")
            ammoAnswer = vaildchoice(99)
            ammoCost = 2*ammoAnswer
            ammo = 20*ammoAnswer
            bill += ammoCost
            spentOnItems[2] = ammoCost
        elif choice == 4:
            #Buying Clothes
            bill -= spentOnItems[3]
            clothes = 0
            spentOnItems[3] = 0.00
            print("""
            You'll need warm clothing in the mountains.
            I recommend taking at least 2 sets of clothes
            per person. Each set is $10.
            """)
            print(str.format("Total Bill so far ${:.2f}", bill))
            print("how many sets of clothes do you want(max 99)")
            clothes = vaildchoice(99)
            clothesCost = clothes*10
            bill += clothesCost
            spentOnItems[3] = clothesCost
        elif choice == 5:
            bill -= spentOnItems[4]
            spentOnItems[4] = 0.00
            #Buying Parts
            partsInventory = []
            partsBill = 0.00
            parts = ["Wagon Wheel", "Wagon Axle", "Wagon Tongue", "Back to Main Shop"]
            partsCost = [10.00, 20.00, 50.00, partsBill]
            while True:
                partsCost[len(partsCost)-1] = partsBill
                #Print our menu
                for i in range(len(parts)-1):
                    print(str.format("\t{}.{:<20} ${:<10.2f}", i + 1, parts[i], partsCost[i]))
                print(str.format("\t{}.{:<20}", "4", parts[3]))
                print("You're buying:",partsInventory)
                print(str.format("Total Bill so far ${:.2f}", bill+partsBill))
                #Get the users choice
                partChoice = vaildchoice(4)
                #Check user choice
                if partChoice == 1:
                    print("how wagon wheels do you want(max 9)")
                    answer = vaildchoice(9)
                    for i in range(answer):
                        partsInventory.append("Wagon Wheel")
                    partsBill += partsCost[0]*answer
                elif partChoice == 2:
                    print("how many axles do you want(max 9)")
                    answer = vaildchoice(9)
                    for i in range(answer):
                        partsInventory.append("Wagon Axle")
                    partsBill += partsCost[1] * answer
                elif partChoice == 3:
                    print("how many tougunes do you want(max 9)")
                    answer = vaildchoice(9)
                    for i in range(answer):
                        partsInventory.append("Wagon Tongue")
                    partsBill += partsCost[2] * answer
                elif partChoice == 4:
                    bill += partsBill
                    spentOnItems[4] = partsBill
                    break
                else:
                    print("Something went wrong")
        elif choice == 6:
            if bill <= money:
                money-= bill
                return oxen,food,ammo,clothes,parts,money
            else:
                print("You don't have enough money, change your shopping list.")
        else:
            print("Something went wrong")
def currentDay(date,month):
    monthList = ("march", "april", "may", "june", "july",
                 "august", "september", "october", "november", "december", "january",
                 "february")
    if month == 1:
        month = "march"
    elif month == 2:
        month = "april"
    elif month == 3:
        month = "may"
    elif month == 4:
        month = "june"
    elif month == 5:
        month = "july"
    for i in range(len(monthList)):
        if month == monthList[i]:
            monthCount = i
            break
    date += 1
    if month.lower() == "march" or month.lower() == "may" or month.lower() == "july" or month.lower() == "september" or month.lower() == "november" or month.lower() == "january":
        dateMax = 31
    else:
        dateMax = 30
    if (date > dateMax):
        date -= dateMax
        monthCount += 1
        month = monthList[monthCount]
    print("It is " + str(month) + " " + str(date))
    return month, date
def getWeather():
    weatherList = ("good", "fair", "poor", "good", "fair", "good")
    weather = random.choice(weatherList)
    if weather == "good":
        weatherNum = 1
    elif weather == "fair":
        weatherNum = .5
    else:
        weatherNum = .25
    print("The weather is", weather)
    return weatherNum
def eat(newFood,party,ration):
    newFood -= 3 * ration * len(party)
    if newFood < 0:
        newFood = 0
    print("You have " + str(newFood) + " pounds of food left")
    return newFood
def newHealth(health,party,food,rations):
    newResult = newIllness(health, party)
    health = newResult[0]
    party = newResult[1]
    if food >= len(party) * rations:
        health -= len(party)
    else:
        health -= 5 * len(party)
    if health <= 0:
        dead = random.choice(party)
        party.remove(dead)
        print(dead + " died")
        health = 80
    if health >= 80:
        condition = 1
    elif health < 80 and health >= 50:
        condition = .5
    else:
        condition = .25
    return condition, health, party
def newIllness(health,party):
    victim = random.choice(party)
    illList = ("SB", "BA", "Dis", "None", "None", "None", "None", "None", "None")
    ill = random.choice(illList)
    if ill == "SB":
        health -= 25
        print(victim + " got a snake bite")
    elif ill == "BA":
        health -= 10
        print(victim + " broke their arm")
    elif ill == "Dis":
        health -= 5
        print(victim + " got dysentery")
    if health <= 0:
        party.remove(victim)
        print(victim + " died")
        health = 80
    return health, party
def travel(weather,condition,oxen,pace,milestraveled):
    tempmiles = oxen * pace
    tempmiles *= weather
    tempmiles *= condition
    milestraveled += tempmiles
    return milestraveled
def changeRation():
    print("""
    1. double rations
    2. normal rations
    3. half rations
    """)
    ration = vaildchoice(3)
    if ration == 1:
        return 2
    elif ration == 2:
        return 1
    elif ration == 3:
        return 0.5
def rest(health,food,party,ration):
    health += 15
    food = eat(food, party, ration)
    return health, food
def trade(food,oxen,ammo,parts):
    option1 = ["oxen","wagon_wheels","wagon_axle","wagon_tongue"]
    option2 = ["food","ammo"]
    print("what would you like to trade for?")
    print("""
    1. oxen
    2. wagon wheels
    3. wagon axle
    4. wagon tongue
    """)
    choice = vaildchoice(4)
    if choice == 1:
        print("what would you like to trade?")
        print("""
        1. food
        2. ammo
        """)
        choice2 = vaildchoice(2)
        if choice2 == 1:
            food -= random.randint(100,250)
            oxen += 1
        else:
            ammo -= random.randint(150,300)
            oxen +=1
    if choice == 2:
        print("what would you like to trade?")
        print("""
                1. food
                2. ammo
                """)
        choice2 = vaildchoice(2)
        if choice2 == 1:
            food -= random.randint(50, 100)
            parts.apend("wagon_wheel")
        else:
            ammo -= random.randint(100,250)
            parts.apend("wagon_wheel")
    if choice == 3:
        print("what would you like to trade?")
        print("""
                1. food
                2. ammo
                """)
        choice2 = vaildchoice(2)
        if choice2 == 1:
            food -= random.randint(50, 100)
            parts.apend("wagon_axle")
        else:
            ammo -= random.randint(100, 250)
            parts.apend("wagon_axle")
    if choice == 4:
        print("what would you like to trade?")
        print("""
                1. food
                2. ammo
                """)
        choice2 = vaildchoice(2)
        if choice2 == 1:
            food -= random.randint(50, 100)
            parts.apend("wagon_tongue")
        else:
            ammo -= random.randint(100, 250)
            parts.apend("wagon_tongue")
def hunt(bullets,lbsFood):
    if bullets > 0:
        num = random.randint(0,100)
        if num >= 40:
            newfood = random.randint(20,100)
            lbsFood += newfood
            bullets -= random.randint(5,25)
            print("you got "+str(newfood)+" lbs of food")
        else:
            bullets -= random.randint(5, 25)
            print("you got no food")
    else:
        print("no bullets")
    return lbsFood,bullets
def newpace():
    print("""
        1. double pace
        2. normal pace
        3. half pace
        """)
    pace = vaildchoice(3)
    if pace == 1:
        return 2
    elif pace == 2:
        return 1
    elif pace == 3:
        return 0.5



def play_menu():
    choice = 0
    playing = True
    while choice != 1:


        print(""" You may:
    1.Travel The trail
    2.Learn about the trail
    3.End
    """)
        choice = vaildchoice(3)
        if choice == 2:
            print("""Try taking a journey by covered wagon across 2000 miles of plains, rivers, and mountains. Try! On the plains, will you slosh your oxen through mud and water-filled ruts or will you plod through dust six inches deep?

How will you cross the rivers? If you have money, you might take a ferry (if there is a ferry). Or, you can ford the river and hope you and your wagon aren't swallowed alive!

What about supplies? Well, if you're low on food you can hunt. You might get a buffalo... you might. And there are bear in the mountains.

At the Dalles, you can try navigating the Columbia River but if running the rapids with a makeshift raft makes you queasy, better take the Barlow Road. 

If you for some reason you don't survive -- your wagon burns, or thieves steal your oxen, or you run out of provisions, or you die of cholera -- don't give up! Try again...and again.""")
            print()
        elif choice == 3:
            quit()

    choice2 = 4
    while choice2 == 4:
        print("Many kinds of people made the trip to Oregon")
        print("""You may:
              1. Be a banker from Boston
              2. Be a carperter from Ohio
              3. Be a farmer from Illinois
              4. Find out the diffences between these charaters""")

        choice2 = vaildchoice(4)
        if choice2 == 4:
            print("""If you're a banker, you'll have more money for supplies and services than a carpenter or a farmer.
The harder your choice, the more points you'll get.""")
            print()
    Job = choice2
    party = []
    print("how many people are with you(4 MAX)")
    players = vaildchoice(4)
    Name = input("What is the First name of the leader?")
    party.append(Name)
    print("What are the First names of your members in your party")
    print('1.' + Name)
    if players >= 1:
        Name2 = input('2.')
        if players >= 2:
            Name3 = input('3.')
            if players >= 3:
                Name4 = input('4.')
                if players >= 4:
                    Name5 = input('5')
    answer = letterchoice()
    if answer == "y":
        if players >= 1:
            party.append(Name2)
            if players >= 2:
                party.append(Name3)
                if players >= 3:
                    party.append(Name4)
                    if players >= 4:
                        party.append(Name5)
    while answer == "n":
        print("change which name")
        change = vaildchoice(players+1)
        while int(change) > players+1:
            change = input("thats not a player")
        if change == 1:
            Name = input("What is the First name of the leader")
            print("are these names correct")
            answer = letterchoice()
        if change == 2:
            Name2 = input("What is their name of the second person")
            print("are these names correct")
            answer = letterchoice()
        if change == 3:
            Name3 = input("What is their name of the third person")
            print("are these names correct")
            answer = letterchoice()
        if change == 4:
            Name4 = input("What is their name of the fourth person")
            print("are these names correct")
            answer = letterchoice()
        if change == 5:
            Name5 = input("What is their name of the fifth person")
            print("are these names correct")
            answer = letterchoice()
    if answer == "y":
        if players >= 1:
            party.append(Name2)
            if players >= 2:
                party.append(Name3)
                if players >= 3:
                    party.append(Name4)
                    if players >= 4:
                        party.append(Name5)
    print(""""It is 1848. your jumping off place for oregon is independance. missouri. you must decide which month to leave independance""")
    print("""
    1. march
    2. april
    3. may
    4. june
    5. july
    6. ask for advice""")
    month = vaildchoice(6)
    while month == 6:
        print("""You attend a public meeting held for "folks with the California-Oregon fever." You're told:
If you leave too early, there won't be any grass for your oxen to eat. If you leave too late, you may not get to Oregon
 before winter comes. If you leave at just the right time, there will be green grass and the weather will still be cool.""")
        print(
            """"It is 1848. your jumping off place for oregon is independance. missouri. you must decide which month to leave independance""")
        print("""
        1. march
        2. april
        3. may
        4. june
        5. july
        6. ask for advice""")

        month = vaildchoice(6)

    if Job == 1:
        money = 1600
    elif Job == 2:
        money = 800
    else:
        money = 400

    print("""Before leaving Independence you should buy equipment and supplies. You have $"""+str(money)+""" in cash, buy you don't have to spend it all now.
You can buy whatever you need Matt's General Store.

Hello, I'm Matt. So you're going to Oregon! I can fix you up with what you need:
-a team of oxen to pull your wagon
-clothing for both summer and winter
-plenty of food for the trip
-ammunition for your rifles
-spare parts for your wagon""")
    oxen = 0
    food = 0
    clothes = 0
    ammo = 0
    parts = []
    bought = shop(money,food,ammo,clothes,parts,oxen)
    #oxen,food,ammo,clothes,parts,money
    oxen = bought[0]
    food = bought[1]
    ammo = bought[2]
    clothes = bought[3]
    parts = bought[4]
    money = bought[5]
    milesTraveled = 0
    lengthOfTrail = 2200
    brokeDown = False
    rations = 1
    date = 0
    health = 80
    pace = 1
    while milesTraveled <= lengthOfTrail and len(party) > 0:
        day = currentDay(date,month)  # add to day
        month = day[0]
        date = day[1]
        weather = getWeather()  # pick weather condition
        food = eat(food,party,rations)  # adjust food
        healthneeds = newHealth(health,party,food,rations)  # adjust health
        health = healthneeds[1]
        condition = healthneeds[0]
        party = healthneeds[2]
        milesTraveled = travel(weather,condition,oxen,pace,milesTraveled)  # calc how many miles traveled
        print("you traveled "+str(milesTraveled)+" so far")
        while True:
            print("""
            1. Continue
            2. Change Rations
            3. Rest
            4. Trade
            5. Hunt
            6. change pace
            """)
            choice = vaildchoice(6)
            if choice == 1:
                if oxen > 0 and not brokeDown:
                    break
                else:
                    print("Can't travel at this time")
                    if oxen < 1:
                        print("You have no oxen")
                    else:
                        print("You are broken down")
                    continue
            elif choice == 2:
                rations = changeRation()
            elif choice == 3:
                healthfood = rest(health,food,party,rations)  # add to days and eat food
                health = healthfood[0]
                food = healthfood[1]
                break

            elif choice == 4:
                trade(food,oxen,ammo,parts)
            elif choice == 5:
               result=hunt(ammo,food)
               ammo = result[1]
               food = result[0]
               break
            elif choice == 6:
                pace = newpace()
            else:
                print("Not an option")
    if milesTraveled >= lengthOfTrail:
        print("Good job you made it to Oregon")
    else:
        print("All members of your party died")



def main():
    splash_screen()
    input("press enter to continue")
    playing = play_menu()
    while playing:
        print(playing)


print("end of game")

main()


