def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not
        if it is new, get the user's name
        if it is not a new game, thank the player
        for playing again and continue with the game
    """
    #meaning, if we do not already nave this user's name,
    # then they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again, {}!.".format(name))
    else:
        stop = True
        while stop:
          if name == "":
              name = input("\nWhat is your name? \n>>> ").capitalize() 
              if name != "":
                  print("\nWelcome, {}".format(name))
                  print("\nIn this game, you will be greated \nby several different people.  \nYou can choose to be nice or mean")
                  print("but at the end of the game, your fate\nwill be sealed by your actions.")
                  stop = False
                  return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\A stranger approaches you for a \nconversation.  Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling.")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nmenacingly and storms off.")
            mean = (mean + 1)
            stop = False
        score(nice,mean,name) # pass the three variables to the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
        #score function is being passed the values stored within the three variables
    if nice > 2:
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    # substitute the {} wildcards with our variavle values
    print("\nNice job {}, you win! \nEveryone loves you and you've made lots of friends along the way.".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("\nAhhh too bad, game over.  \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nGood riddance")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #notice the name variable has not been reset, as the same user has opted to play again
    start(nice,mean,name)


if __name__ == "__main__":
           start()
    
