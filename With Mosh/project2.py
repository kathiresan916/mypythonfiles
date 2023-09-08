#Car Game:

help_game = "Start - to Start the car \nStop - to Stop the car \nQuit - to exit"

user_input = ""
started = False #Initiate car is not started.
while user_input.lower() != "quit":
    user_input = input("> ").lower()
    if user_input == "help":
        print(help_game)
    elif user_input == "start":
        if started: #If car started already this output will come
            print("Car already started..!")
        else:
            started = True #Now car is started
            print("Car Started... Ready to go..!")
    elif user_input == "stop":
        if not started: #First car not started. If you first enter stop. "Car already stop" message will given
            print("Car already stopped.")
        else:
            started = False #car started. User enter stop again the above if statemet will provide. Because not started boolean function is applied. 
            print("Car Stopped")
    elif user_input == "quit":
        break
else:
    print("I don't understand.")