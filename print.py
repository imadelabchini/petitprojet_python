print("""
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█

""")
print("Welcom to my island! ")
print("There are two doors in front of you. 🏮 a red door 🔷 a blue door")
door_choice = input("which door do you want to open? ").lower()

#check user's choise
if door_choice == "blue" :
    print("oops! You choice the crocodile door.")
    print("Game over! 🐊🐊🐊")
elif door_choice == "red" :
    print("Great! now you entered a room.")
    print(" you found there Boxes: 📦 white, 📦 black, 📦 green")
    box_choice = input("Which box do you open? ").lower()

    #check user's choise for the first chest
    if box_choice =="white" :
        print("Oops! you opened a box filled with snakes 🐍🐍🐍")
    elif box_choice == "black" :
        print("Oops! you opened a box filled with spiders 🐞🐞🐞")
    elif box_choice == "green" :
        print("Congratulation! you found the treasure 💰💰💰")
    else :
        print("invalid choice! 😓😓😓") 

else :
    print("invalid choice! 😓😓😓")   