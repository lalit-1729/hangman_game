import random

word_list =["admit","adult","attack","advice","arrange","attempt","august","autumn","border","breeze","brick","calm","canal","aasey","cast","chose","claws","coach","constant","contrast","cookies","customs","damage","danny","deeply","depth","discuss","doll","donkey","egypt","ellen","essential","exchange","exist","explanation","facing","film","finest","fireplace","floating","folks","fort","garage","grabbed","mother","habit","happily","harry","heading","hunter","illinois","image","dependent","instant","january","kids","label","lee","lungs","manufacture","martin","mathematics","melted","memory","mill","mission","monkey","mount","mysterious","neighbourhood","norway","nuts","occasion","official","ourself","palace","pennsylvania","philadelphia","plates","poetry","policeman","positive","possibly","practical","pride","promise","recall",'relationship','remarkable','require','rhyme','rocky','rubbed','rush','sale','satellites','satisfied','scared','selection','shake','shaking','shallow','shout','silly','simple','slight','slip','slope','soap','solar','species','spin','stiff','swung','tales','thumb','tobacco','toy','trap','treat','tune','universe','vapour','vessels','wealth','wolf','zoo']

print("~~~~Welcome to Hangman Game~~~~\nThis is the simpler version of the game\n~You can guess a word letter at a time\n~You have maximum of 10 unsuccessfull trial\n~You can more than one round if you want\nEnjoy the Game\nAnd Please use lower caps letter i.e. turn off your CapsLock")

#setting the game loop
play_again = "y"
while(play_again == "y"):
            
    word_choosed = random.choice(word_list)
    # remove commment tag from below for cheating prupose
    #print(word_choosed,"\n\n")
    dummy_word = word_choosed
    word = "_"*len(word_choosed)
    print("\nYour word is:", word)
    trials = 10
    guessed_letters = ""
    letters = set(list(word_choosed))
    
    #defining a function to display the word after every successfull guess
    def imp_fun(str1, str2):
        trs = list(str1)
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                trs[i] = word_choosed[i]
        return "".join(trs)
    
    #setting up the trials loop
    while(trials != 0):
        # if statement for winning
        if len(letters) == 0:
            print("**********You won the Game**********\n")
            play_again = input("Do you want to play Hangmam again (Y/N)?")
            break
                
        letter_guessed = input("Guess a letter:")
        guessed_letters += letter_guessed
        guessed_letters += " "
        
        #if statement to verify whether the guess is correct or not
        if letter_guessed in letters:
            dummy_word = dummy_word.replace(letter_guessed, "_")  ##srt2
            word = imp_fun(word, dummy_word)
            print("\n~Word in Progress:",word, "\n~Guessed Letters: ", guessed_letters)
            letters.remove(letter_guessed)
            
        else:
            trials -= 1
            print("\nNot in this word, You lost a trial;\nNo of trials left:", trials,"\nWord in Progress:", word, "\n~Guessed Letters: ", guessed_letters)
            
    # if statement for loosing the game.
    if trials == 0:
        print("\n**********Game Over**********\nYou lose**********\nThe word was:", word_choosed)
        play_again = input("Do you want to play Hangmam again(Y/N)?")
