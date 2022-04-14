##optx = str(input(""))
##optx = optx.lower()
##if optx == "":
global study
global workout
global breakfast
global endings

workout = "n"
study = "n"


def rData():
    global endings
    eFile = open("GameEndings.txt")
    endings = eFile.readlines()
    eFile.close()
    endings[0] = "Hero Ending: No\n"
    endings[1] = "Balanced Ending: No\n"
    endings[2] = "'Dang Bro That's Like Insanely Unlucky' Ending: No\n"
    endings[3] = "4.0 GPA Ending: No\n"
    endings[4] = "3.0 GPA Ending: No\n"
    eFile = open("GameEndings.txt", "w")
    aEndings = "".join(endings)
    eFile.write(aEndings)
    eFile.close()
    print("")
    print("Data reset!")
        

def gStart():
    global workout
    workout = "n"
    opt1 = str(input("You wake up Monday morning a few hours before class. Do you go to the (Gym), eat (Breakfast), or play (Games) before class? "))
    opt1 = opt1.lower()
    if opt1 == "gym":
        opt2 = str(input("You head to the gym for a sick workout! But do you listen to (Music), a motivational (Audiobook), or (Nothing) "))
        opt2 = opt2.lower()
        if opt2 == "music":
            print("Your workout goes great! ")
            workout = "y"
            print("You arrive at school on time! ")
            print("")
            gSchool()
        elif opt2 == "audiobook":
            print("You get so motivated that you decide to quit school and start a business re-selling NFTs. (Bad Ending?)")
            doanother = input("Press 'Enter' to restart! ")
            print("")
            gStart()
        elif opt2 == "nothing":
            print("You don't listen to anything while working out? You are a psychopath. (Bad Ending)")
            doanother = input("Press 'Enter' to restart! ")
            print("")
            gStart()
        else:
            error = input("You entered an invalid input! Press 'Enter' to try again: ")
            gStart()
                
    elif opt1 == "breakfast":
        print("You make some okay-tasting eggs and head to school. ")
        print("You arrive at school on time! ")
        print("")
        gSchool()
            
    elif opt1 == "games":
        print("You lose track of time and miss class! (Bad Ending)")
        doanother = input("Press 'Enter' to restart! ")
        print("")
        gStart()

    else:
        error = input("You entered an invalid input! Press 'Enter' to try again: ")
        gStart()
               

def gSchool():
    global endings
    global study
    eFile = open("GameEndings.txt")
    endings = eFile.readlines()
    eFile.close()
    study = "n"
    opt1 = str(input("You arrive at school half an hour before your math class starts. Do you (Study) before class or take a (Walk)? "))
    opt1 = opt1.lower()
    if opt1 == "study":
        print("You study the day's material ahead of time. Because of this, you perfectly understand it by the end of class. Nice!")
        study = "y"
        print("")
        gSchool2()
            
    elif opt1 == "walk":
        opt2 = str(input("You decide to take a walk around campus before class. It's a nice day out, but you come across a fellow student who is getting beat up! Do you (Fight) the bully, (Call) campus security, or keep (walking)? "))
        opt2 = opt2.lower()
        if opt2 == "fight" and workout == "y":
            print("All that exercise is finally coming in handy! You nimbly dodge the bully's haymaker before knocking them out with a single punch, saving the student from getting a beat-down.")
            print("The Dean later contacts you and awards you with a PHD in Psychology with a focus on Anti-Bullying Tactics (Hero Ending. Nice!)")
            endings[0] = "Hero Ending: Yes!\n"
            eFile = open("GameEndings.txt", "w")
            aEndings = "".join(endings)
            eFile.write(aEndings)
            eFile.close()
        elif opt2 == "fight" and workout == "n":
            print("You approach the bully and end up getting beat up also. You wake up in the hospital and realize that you missed class! If only you had been stronger. (Bad Ending!)")
            doanother = input("Press 'Enter' to restart! ")
            print("")
            gStart()
                
        elif opt2 == "call":
            print("You dial campus security on your phone, and they rush to the area and take care of the issue. You hurry back inside and get to class on time.")
            print("")
            gSchool2()
                
        elif opt2 == "walking":
            print("You ignore the blatant bullying out of fear or cowardice. You suck. (Bad Ending!)")
            doanother = input("Press 'Enter' to restart! ")
            print("")
            gStart()
        else:
            error = input("You entered an invalid input! Press 'Enter' to try again: ")
            gSchool()
    else:
        error = input("You entered an invalid input! Press 'Enter' to try again: ")
        gSchool()


def gSchool2():
    global endings
    eFile = open("GameEndings.txt")
    endings = eFile.readlines()
    eFile.close()
    opt1 = str(input("You get back home after class. Do you make a (Snack), take a (Shower), or get started on (Homework)? "))
    opt1 = opt1.lower()
    if opt1 == "snack":
        print("You make some popcorn and watch a few YouTube videos before getting started on your homework. Today was pretty good. (Balanced Ending)")
        endings[1] = "Balanced Ending: Yes!\n"
        eFile = open("GameEndings.txt", "w")
        aEndings = "".join(endings)
        eFile.write(aEndings)
        eFile.close()
            
    elif opt1 == "shower" and workout == "y":
        print("You're still a little gross from your workout this morning, so the shower is welcome. However, after you finish showering you start posing in the mirror and get distracted. You forget your homework (Bad Ending!)")
        doanother = input("Press 'Enter' to restart! ")
        print("")
        gStart()
    elif opt1 == "shower" and workout == "n":
        print("You take a relaxing shower but slip and break your elbow! You spend the rest of the day at the doctor's office and don't get your homework done. ('Dang Bro That's Like Insanely Unlucky' Ending")
        endings[2] = "'Dang Bro That's Like Insanely Unlucky' Ending: Yes!\n"
        eFile = open("GameEndings.txt", "w")
        aEndings = "".join(endings)
        eFile.write(aEndings)
        eFile.close()
            
    elif opt1 == "homework" and study == "y":
        print("Being the dedicated student you are, your schoolwork always comes first. (4.0 GPA Ending!)")
        endings[3] = "4.0 GPA Ending: Yes!\n"
        eFile = open("GameEndings.txt", "w")
        aEndings = "".join(endings)
        eFile.write(aEndings)
        eFile.close()
            
    elif opt1 == "homework" and study == "n":
        print("Since you didn't do much work at school, you figure you better get started on your homework right away so you can pass your class. (3.0 GPA Ending) ")
        endings[4] = "3.0 GPA Ending: Yes!\n"
        eFile = open("GameEndings.txt", "w")
        aEndings = "".join(endings)
        eFile.write(aEndings)
        eFile.close()
    else:
        error = input("You entered an invalid input! Press 'Enter' to try again: ")
        gSchool2()


eFile = open("GameEndings.txt")
endings = eFile.readlines()

eFile = open("GameEndings.txt")
endings = eFile.readlines()
eFix = []


print("Welcome to College Sim 7! This is a text-based Choose Your Own Adventure game!")
print("Instructions: The options will be surrounded by parenthesis, and you'll need to type the text inside the parenthesis.")
instructions = input("For example, if you want to select an option that says '(Play) this game,' you'd need to type and enter 'Play': ")
doanother = "y"
while doanother == "y":
    print("")
    print("")
    print("")
    gStart()
    doanother = str(input("Would you like to play again? (y/n) "))
    doanother = doanother.lower()

print("")
print("")
print("")



end = str(input("Press 'Enter' to see Achievements"))
for x in endings:
    eFix.append(x.replace("\n",""))
print("Endings : " + str(eFix))

reset = str(input("To reset Endings data, enter 'Reset': "))
reset = reset.lower()
if reset == "reset":
    rData()

print("Thanks for playing! :)")
    
    






