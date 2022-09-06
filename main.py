from tkinter import *
from functools import partial
import random
import sys

sngle_creds = 500  # Intial value of credits
sngle_bets = 5  # and bets

dble_creds_1 = 500  # Intial value of credits for player one
dble_bets_1 = 5  # and their bets
      
dble_creds_2 = 500  # Intial value for credits for player two
dble_bets_2 = 5  # and their bets

root = Tk()
root.title("Blackjack") # Screen Title

home_frame = Frame(root, width=500, height=300, bg="maroon") # Frame for the home screen
home_frame.grid()

home_header = Label(home_frame,   # Header for the home screen
                    text="Blackjack",
                    font=("Times 16 bold"),
                    bg="gold",
                    padx=270,
                    pady=10,
                    justify=CENTER)
home_header.place(x=-70, y=0)


def Single_Username():
    sngle_usrnme_win = Toplevel(root)

    sngle_but.config(state=DISABLED)
    dble_but.config(state=DISABLED)
    sngle_scores_button.config(state=DISABLED)

    def close_sngle_usrnme():  # If either the back button or window is closed
        sngle_but.config(
            state=NORMAL)  # revert the single player button back to normal
        dble_but.config(state=NORMAL)
        sngle_scores_button.config(state=NORMAL)
        sngle_usrnme_win.destroy()

    sngle_usrnme_win.protocol("WM_DELETE_WINDOW", partial(close_sngle_usrnme))

    sngle_usrnme_frame = Frame(sngle_usrnme_win,
                               width=600,
                               height=600,
                               bg="maroon")
    sngle_usrnme_frame.grid()

    sngle_usrnme_header = Label(sngle_usrnme_frame,
                                text="Enter in a username",
                                font="arial 14 bold",
                                justify=CENTER,
                                width=40,
                                bg="orange",
                                wrap=250)
    sngle_usrnme_header.grid(row=0)

    def Single_Player():
        sngle_play_win = Toplevel(sngle_usrnme_frame)

        sngle_frame = Frame(sngle_play_win, width=700, height=500,
                            bg="green")  # Window Frame
        sngle_frame.grid()

        dealer_side = Label(
            sngle_frame,
            text="Dealer",
            font="Times 14 bold",  # Dealer's Side 
            bg="#733f19",
            fg="white",
            padx=330,
            pady=12)  # of the table
        dealer_side.place(x=-10, y=0)

        def sngle_credits_add():
            global sngle_creds  # Get the credits count
            sngle_cred_add = sngle_bets  # Variable that stores players bets
            sngle_creds += sngle_cred_add  # Add the bets to the credits
            sngle_creds_counter.set(
                "Credits: ${:.2f}".format(sngle_creds))  # Format
            # it into the counter
            print("To play again, confirm your bets or press exit to exit game\n")

        def sngle_credits_sub():
            global sngle_creds  # Get credits count
            # sngle_scred_sub = sngle_bets
            sngle_creds -= sngle_bets  # Subtract the bet amount from the credits
            sngle_creds_counter.set(
                "Credits: ${:.2f}".format(sngle_creds))  # Format it
            # it into counter
            print("To play again, confirm your bets or press exit to exit game\n")

        def sngle_bets_add():  # For adding bets
            global sngle_bets  # get the intitial value
            sngle_bet_add = sngle_bet_add_sub_var.get(
            )  # assign the add subtract intvar to a variable
            sngle_bets += sngle_bet_add  # Add five (sngle_bet_add) to current bet value
            sngle_bets_counter.set("Bets: ${:.2f}".format(
                sngle_bets))  # format the value into the counter
            sngle_bet_add_sub_var.set(
                5)  # Makes sure that this variable is set to 5

        def sngle_bets_sub():  # For removing bets
            global sngle_bets
            sngle_bet_sub = sngle_bet_add_sub_var.get()
            sngle_bets -= sngle_bet_sub  # Subtract five from the current bet value
            sngle_bets_counter.set("Bets: ${:.2f}".format(
                sngle_bets))  # format value into counter
            sngle_bet_add_sub_var.set(5)

        sngle_creds_counter = StringVar()
        sngle_creds_counter.set("Credits: $500.00")
        sngle_creds_dsiplay = Label(
            sngle_frame,
            textvariable=sngle_creds_counter,
            bg="orange",
            font="Times 10")  # Makes the credits counter display
        sngle_creds_dsiplay.place(x=560, y=70)

        sngle_bets_counter = StringVar()  # Sets variable as a string varible
        sngle_bets_counter.set("Bets: $5.00")  # Sets the text of the string
        sngle_bets_display = Label(
            sngle_frame,
            textvariable=sngle_bets_counter,
            bg="orange",
            font="Times 10")  # Makes the bets counter display
        sngle_bets_display.place(x=580, y=100)

        sngle_bet_add_sub_var = IntVar()  # Assigns this as an intger variable
        sngle_bet_add_sub_var.set(5)  # Sets a numerical value
        sngle_bet_add_but = Button(sngle_frame,
                                   text="Add bets",
                                   bg="gold",
                                   bd=1,
                                   command=sngle_bets_add)
        sngle_bet_add_but.place(x=604, y=150)  # Button for adding bets
        sngle_bet_sub_but = Button(sngle_frame,
                                   text="Remove bets",
                                   bg="gold",
                                   bd=1,
                                   command=sngle_bets_sub)
        sngle_bet_sub_but.place(x=580, y=180)  # Button for removing bets

      
        def sngle_bets_check():
          if 4<sngle_bets<101:
            sngle_generate()
          else:
            print("Bets can only be min $5 or max $100 \n")

        def sngle_button_state():
            sngle_hit_button.config(state=DISABLED)  # disable action buttons
            sngle_stay_button.config(state=DISABLED)
            sngle_double_button.config(state=DISABLED)
            sngle_bet_add_but.config(
                state=NORMAL)  # revert the buttons back to normal
            sngle_bet_sub_but.config(state=NORMAL)
            sngle_confirm_bet.config(state=NORMAL)

        def sngle_generate():  # Generate player and dealer cards
            global sngle_card_play_1
            global sngle_card_play_2
            global sngle_hit_card
            global sngle_card_play_ttl
            global sngle_card_deal_1
            global sngle_card_deal_2
            global sngle_card_deal_ttl
            sngle_card_play_1 = random.randint(
                1, 11)  # Make two random cards that
            sngle_card_play_2 = random.randint(
                1, 11)  # will be used for the player
            sngle_card_play_ttl = (sngle_card_play_1 + sngle_card_play_2
                                   )  # Total for player cards
            sngle_card_deal_1 = random.randint(1,
                                               11)  # Make two random cards for
            sngle_card_deal_2 = random.randint(1, 11)  # the dealer
            sngle_card_deal_ttl = (sngle_card_deal_1 + sngle_card_deal_2
                                   )  # Total for dealer cards
            sngle_cnfrm_bet()

        def sngle_cnfrm_bet():
            sngle_bet_add_but.config(state=DISABLED)  # Disbale add bets
            sngle_bet_sub_but.config(state=DISABLED)  # remove bets
            sngle_confirm_bet.config(state=DISABLED)  # and confirm bet buttons
            print("Your cards:", sngle_card_play_1,
                  sngle_card_play_2, "\n")  # Print the players cards
            if (sngle_card_play_ttl
                ) == 21:  # If the card total is equal to nine
                print("You win!!!!\n")  # print this statement
                sngle_bet_add_but.config(
                    state=NORMAL)  # revert the buttons back to normal
                sngle_bet_sub_but.config(state=NORMAL)
                sngle_confirm_bet.config(state=NORMAL)
                sngle_credits_add()  # Add bets to credits
            if (sngle_card_play_ttl) > 21:  # If the card total is over nine
                print("Busted, You lose\n")  # print this
                sngle_bet_add_but.config(
                    state=NORMAL)  # revert the buttons back to normal
                sngle_bet_sub_but.config(state=NORMAL)
                sngle_confirm_bet.config(state=NORMAL)
                sngle_credits_sub()  # Take away bets amount from credits
            if (sngle_card_play_ttl) < 21:  # If the total is less than nine
                print("Choose an action at the bottom of the screen\n")
                sngle_hit_button.config(
                    state=NORMAL)  # Enables the action buttons
                sngle_stay_button.config(state=NORMAL)
                sngle_double_button.config(state=NORMAL)
                pass  # Continue the game using actions

        def sngle_play():
            sngle_hit_button.config(state=DISABLED)  # Disable action buttons
            sngle_stay_button.config(state=DISABLED)
            sngle_double_button.config(state=DISABLED)
            print("Dealer's Cards:", sngle_card_deal_1,
                  sngle_card_deal_2, "\n")  # Print the dealers cards
            if sngle_card_deal_ttl == 21:
              print("Dealer wins\n")
              sngle_credits_sub()
            if sngle_card_play_ttl > sngle_card_deal_ttl:  # If the players total exceeds deealers ttl
                if sngle_card_play_ttl <= 21:  # and is less than 21
                    print("You win\n")  # they win
                    sngle_credits_add()  # and add winnings to credits
                if sngle_card_play_ttl > 21:  # or is more than 21
                    print("You lose\n")  # they lose
                    sngle_credits_sub()  # and takes away credits
            if sngle_card_play_ttl < sngle_card_deal_ttl:  # If the dealers total exceeds the players ttl
                print("You lose\n")  # they lose
                sngle_credits_sub()  # and takes away credits
            if sngle_card_play_ttl == sngle_card_deal_ttl:  # If both totals are the same
                print("Draw\n")  # Call a draw
            sngle_bet_add_but.config(
                state=NORMAL)  # revert the buttons back to normal
            sngle_bet_sub_but.config(state=NORMAL)
            sngle_confirm_bet.config(state=NORMAL)

        def sngle_hit():
            global sngle_card_play_ttl  # Get the player card total
            sngle_hit_card = random.randint(1, 11)  # Used for hit
            sngle_extra_crd = sngle_hit_card
            sngle_card_play_ttl += sngle_extra_crd  # Add another card to it
            print("Your card:", sngle_extra_crd, "\n")  # print the cards
            if sngle_card_play_ttl == 21:  # if the players cards total nine
                print("You win\n")  # They win
                sngle_credits_add(
                )  # and get their winnings added to their credits
                sngle_button_state()  # change the button states
            if sngle_card_play_ttl > 21:  # if the total is over nine
                print("Busted, You lose\n")  # they lose
                sngle_credits_sub()  # their credits are subtracted
                sngle_button_state()  # and the button states are changed
            if sngle_card_play_ttl < 21:  # If the total is under nine
                print("Press an action button to continue\n")
                pass  # continue the game

        def sngle_dbledwn():
            global sngle_bets  # Get player bets
            sngle_bets *= 2  # Multiply it by two
            sngle_bets_counter.set(
                "Bets: ${:.2f}".format(sngle_bets))  # and format it
            # sngle_play()

        sngle_confirm_bet = Button(sngle_frame,
                                   text="Confirm bets",
                                   bg="orange",
                                   command=sngle_bets_check)
        sngle_confirm_bet.place(x=580, y=220)  # Confirm bet button

        sngle_hit_button = Button(sngle_frame,
                                  text="Hit",
                                  bg="white",
                                  bd=1,
                                  command=sngle_hit)  # Hit button
        sngle_hit_button.place(x=250, y=335)

        sngle_stay_button = Button(sngle_frame,
                                   text="Stay",
                                   bg="white",
                                   bd=1,
                                   command=sngle_play)  # Stay button
        sngle_stay_button.place(x=375, y=335)

        sngle_double_button = Button(sngle_frame,
                                     text="Double",
                                     bg="white",
                                     bd=1,
                                     command=sngle_dbledwn)  # Double button
        sngle_double_button.place(x=300, y=375)

        sngle_hit_button.config(
            state=DISABLED
        )  # When the programe starts, disable the action buttons
        sngle_stay_button.config(state=DISABLED)
        sngle_double_button.config(state=DISABLED)

        def sngle_rules():
          sngle_rules_win = Toplevel(sngle_frame)
          sngle_rules_but.config(state=DISABLED)
          
          def close_sngle_rules():  # If either the back button or window is closed
                sngle_rules_but.config(state=NORMAL)
                sngle_rules_win.destroy()

          sngle_rules_win.protocol("WM_DELETE_WINDOW",
                                    partial(close_sngle_rules))

          sngle_rules_frme = Frame(sngle_rules_win, width=685, height=420, bg="maroon")
          sngle_rules_frme.grid()

          sngle_rules_lbl = Label(sngle_rules_frme, text="Rules", font="Times 14", justify=CENTER, bg="gold", padx=400)
          sngle_rules_lbl.place(x=-100,y=0)

          sngle_rules_txt = Label(sngle_rules_frme, text='''
          * Aim: The aim of the game is win by one of the following ways:
          Have 21 from your card total (Instant win)
          Have a higher card total then the dealer (who you play against)
          The dealer is busted (their card total goes over 21)
          * The Game: Start off by adding or removing bets using the buttons and when you are happy with 
            your amount, continue the game by pressing confirm bets.
            The game will then deal out your cards. If they total 21, you instantly win, if they total over 21, 
            you instantly lose, otherwise you move on to the next phase where you can choose your action.
            You have three actions to choose from:
            - Hit: Gain an extra card
            - Stay: Move on to face the dealer
            - Double: Double the amount of bets
            After pressing stay, you will move on to face the dealer. The game will compare the 
            totals of your cards. You are now faced with the following scenarios:
            If the dealer’s cards totals 21, you lose
            If the dealer’s cards goes over 21, they are busted and you win
            If the dealer has a higher card total than you and is under 21, you lose
            If the you have a higher card total than the dealer, you win
            If you draw, no one wins
          * End: If you win, your bets will be added to your credits, if you lose, your bets will be taken from 
            your credits.
            You can either exit or continue the game''', font="Times 10", justify=LEFT,bg="lawn green")
          sngle_rules_txt.place(x=-30,y=25)

        sngle_rules_but = Button(sngle_frame, text="Rules", bg="orange", bd=1, command=sngle_rules)
        sngle_rules_but.place(x=580, y=370)

        def sngle_exit():
            # sngle_exit_win = Toplevel(root)
            sngle_exit_win = Toplevel(sngle_frame)

            sngle_exit_but.config(state=DISABLED)

            def close_sngle_exit( # For closing single player mode
            ):  # If either the back button or window is closed
                sngle_exit_but.config(
                    state=NORMAL
                )  # revert the single player button back to normal
                sngle_exit_win.destroy()

            sngle_exit_win.protocol("WM_DELETE_WINDOW",
                                    partial(close_sngle_exit))

            sngle_exit_frame = Frame(sngle_exit_win,
                                     width=200,
                                     height=100,
                                     bg="maroon")
            sngle_exit_frame.grid()

            sngle_exit_text = Label(sngle_exit_frame,
                                    text="Are you sure?",
                                    font="Times 14",
                                    justify=CENTER,
                                    bg="gold", padx=35)
            sngle_exit_text.place(x=0, y=0)

            def sngle_scre_enter():
              sngle_scre_entr_win = Toplevel(sngle_exit_frame)
              
              sngle_scre_entr_frme = Frame(sngle_scre_entr_win, width=305, height=100, bg="maroon")
              sngle_scre_entr_frme.grid()
              
              sngle_scre_entr_lbl = Label(sngle_scre_entr_frme, 
                                          text="Would you like to enter your \nscore into the high scores list?",
                                          font="Times 14",
                                          justify=CENTER,
                                          bg="gold", padx=10)
              sngle_scre_entr_lbl.place(x=0,y=0)

              def scre_enter_info():
                global sngle_username
                global sngle_creds
                sngle_scre_cred = str(sngle_creds)
                f = open("Single_Player_Scores.txt", "a")
                info_enter = ("\n"+sngle_username + "  " + "$" + sngle_scre_cred)
                f.write(info_enter)
                # print(f.read(),"\n")
                f.close()
                sngle_exit_y()

              sngle_scre_entr_y = Button(sngle_scre_entr_frme, text="Yes", command=scre_enter_info)
              sngle_scre_entr_y.place(x=70, y=60)
              sngle_scre_entr_n = Button(sngle_scre_entr_frme, text="No", command=sngle_exit_y)
              sngle_scre_entr_n.place(x=190, y=60)

            def sngle_exit_y():
                sngle_exit_but.config(state=NORMAL)
                sngle_play_win.destroy()
                sngle_exit_win.destroy()

            sngle_ext_y_but = Button(sngle_exit_frame,
                                     text="Yes",
                                     font="Times 10",
                                     bd=1,
                                     command=sngle_scre_enter)
            sngle_ext_y_but.place(x=20, y=50)

            sngle_ext_n_but = Button(sngle_exit_frame,
                                     text="No",
                                     font="Times 10",
                                     bd=1,
                                     command=close_sngle_exit)
            sngle_ext_n_but.place(x=130, y=50)

        sngle_exit_but = Button(sngle_frame,
                                text="Exit",
                                bg="orange",
                                bd=1,
                                command=sngle_exit)
        sngle_exit_but.place(x=580, y=400)

    def prnt_sngle_usrnme():  # Carries out defintion if confirm is pushed
        global sngle_username
        sngle_username = sngle_usrnme_entry_box.get(
        )  # Stores the input text from the entry field in this variable as string
        print("Hello", sngle_username)  # and prints it out
        print("If you need help, click rules\n")
        Single_Player()

    sngle_usrnme_entry_box = Entry(sngle_usrnme_frame,
                                   width=20,
                                   font="arial 14")  # Creates the entry box
    sngle_usrnme_entry_box.grid(row=2, pady=10)

    sngle_usrnme_back = Button(
        sngle_usrnme_frame,
        text="Back",
        width=10,
        bg="orange",  # Creates back button
        font="arial 10 bold",
        command=partial(close_sngle_usrnme))
    sngle_usrnme_back.grid(row=6, pady=10)

    sngle_usrnme_confirm = Button(
        sngle_usrnme_frame,
        text="Confirm",
        bg="gold",
        font="arial 10 bold",  # Creates
        command=prnt_sngle_usrnme)  # confirm button
    sngle_usrnme_confirm.grid(row=4, pady=10)


sngle_but = Button(home_frame,
                   text="Single-player",
                   font="arial 10 bold",
                   bd=1,
                   bg="orange",
                   command=Single_Username)
sngle_but.place(x=190, y=100)


def Double_Username():
    dble_usrnme_win = Toplevel(root)

    sngle_but.config(state=DISABLED)
    dble_but.config(state=DISABLED)
    sngle_scores_button.config(state=DISABLED)

    def close_dble_usrnme():  # If either the back button or window is closed
        dble_but.config(
            state=NORMAL)  # revert the single player button back to normal
        sngle_but.config(state=NORMAL)
        sngle_scores_button.config(state=NORMAL)
        dble_usrnme_win.destroy()

    dble_usrnme_win.protocol("WM_DELETE_WINDOW", partial(close_dble_usrnme))

    dble_usrnme_frame = Frame(dble_usrnme_win,
                              width=500,
                              height=300,
                              bg="maroon")
    dble_usrnme_frame.grid()

    dble_usrnme_header = Label(dble_usrnme_frame,
                               text="Enter in two usernames",
                               font="Times 14 bold",
                               justify=CENTER,
                               bg="gold",
                               padx=270,
                               pady=10)
    dble_usrnme_header.place(x=-140, y=0)


    def Double_Player():
      dble_play_win = Toplevel(dble_usrnme_frame)
      
      dble_frame = Frame(dble_play_win, width=700, height=500, bg="green")  # Window frame
      dble_frame.grid()
      
      dealer_side = Label(    #Dealer's Side,
          dble_frame,
          text="Dealer",
          font="Times 14 bold", 
          bg="#733f19",
          fg="white",
          padx=330,
          pady=12) 
      dealer_side.place(x=-10, y=0)
          
      
      def dble_add_creds_1():  # Adding credits for Player 1
          global dble_creds_1
          dble_creds_1 += dble_bets_1
          dble_creds_1_counter.set("Credits: ${:.2f}".format(dble_creds_1))
      
      
      def dble_sub_creds_1(): # Taking credits from Player 1
          global dble_creds_1
          dble_creds_1 -= dble_bets_1
          dble_creds_1_counter.set("Credits: ${:.2f}".format(dble_creds_1))
      
      
      def dble_add_creds_2():  # Adding credits for Player 2
          global dble_creds_2
          dble_creds_2 += dble_bets_2
          dble_creds_2_counter.set("Credits: ${:.2f}".format(dble_creds_2))
      
      
      def dble_sub_creds_2():  # Taking credits from Player 1
          global dble_creds_2
          dble_creds_2 -= dble_bets_2
          dble_creds_2_counter.set("Credits: ${:.2f}".format(dble_creds_2))
      
      
      def dble_bets_add_1():  # Adding bets to Player 1's current bets
          global dble_bets_1
          dble_bet_add_1 = dble_bet_add_sub_var.get()
          dble_bets_1 += dble_bet_add_1
          dble_bets_1_counter.set("Bets: ${:.2f}".format(dble_bets_1))
          dble_bet_add_sub_var.set(5)
      
      
      def dble_bets_sub_1():  # Taking bets from Player 1's current bets
          global dble_bets_1
          dble_bet_add_1 = dble_bet_add_sub_var.get()
          dble_bets_1 -= dble_bet_add_1
          dble_bets_1_counter.set("Bets: ${:.2f}".format(dble_bets_1))
          dble_bet_add_sub_var.set(5)
      
      
      def dble_bets_add_2():  # Adding bets to Player 1's current bets
          global dble_bets_2
          dble_bet_add_2 = dble_bet_add_sub_var.get()
          dble_bets_2 += dble_bet_add_2
          dble_bets_2_counter.set("Bets: ${:.2f}".format(dble_bets_2))
          dble_bet_add_sub_var.set(5)  # Set intial bet add/sub value back to 5
      
      
      def dble_bets_sub_2():  # Taking bets from Player 2's current bets
          global dble_bets_2
          dble_bet_sub_2 = dble_bet_add_sub_var.get()
          dble_bets_2 -= dble_bet_sub_2
          dble_bets_2_counter.set("Bets: ${:.2f}".format(dble_bets_2))
          dble_bet_add_sub_var.set(5)
      
      
      dble_creds_1_counter = StringVar()  # Sets variable as a string variable
      dble_creds_1_counter.set("Credits: $500.00")  # Set the counter variable to display $500
      dble_creds_1_display = Label(dble_frame,  # Display the current credits
                                   textvariable=dble_creds_1_counter,
                                   bg="orange",
                                   font="Times 10")
      dble_creds_1_display.place(x=25, y=70)  # Puts the label onto the frame
      
      dble_bets_1_counter = StringVar()  # Sets variable as a string variable
      dble_bets_1_counter.set("Bets: $5.00")  # Set bet counter variable to $5
      dble_bets_1_display = Label(dble_frame, # Create the display for the counter
                                  textvariable=dble_bets_1_counter,
                                  bg="orange",
                                  font="Times 10")
      dble_bets_1_display.place(x=25, y=100)  # Put the label onto the frame
      
      dble_creds_2_counter = StringVar()
      dble_creds_2_counter.set("Credits: $500.00")
      dble_creds_2_display = Label(dble_frame,
                                   textvariable=dble_creds_2_counter,
                                   bg="orange",
                                   font="Times 10")
      dble_creds_2_display.place(x=557, y=70)
      
      dble_bets_2_counter = StringVar()
      dble_bets_2_counter.set("Bets: $5.00")
      dble_bets_2_display = Label(dble_frame,
                                  textvariable=dble_bets_2_counter,
                                  bg="orange",
                                  font="Times 10")
      dble_bets_2_display.place(x=592, y=100)
      
      dble_bet_add_sub_var = IntVar()  # Set this varibale as an integer variable
      dble_bet_add_sub_var.set(5)  # Set the vairable to 5
      dble_bet_add_but_1 = Button(dble_frame,  # Create a button to add bets (Player 1)
                                  text="Add bets",
                                  bg="gold",
                                  bd=1,
                                  command=dble_bets_add_1)
      dble_bet_add_but_1.place(x=20, y=150)
      dble_bet_sub_but_1 = Button(dble_frame,  # Create a button to remove bets (Player 1)
                                  text="Remove bets",
                                  bg="gold",
                                  bd=1,
                                  command=dble_bets_sub_1)
      dble_bet_sub_but_1.place(x=20, y=180)
      
      dble_bet_add_but_2 = Button(dble_frame,  # Create a button to add bets (Player 2)
                                  text="Add bets",
                                  bg="gold",
                                  bd=1,
                                  command=dble_bets_add_2)
      dble_bet_add_but_2.place(x=604, y=150)
      dble_bet_sub_but_2 = Button(dble_frame,  # Create a button to remove bets (Player 1)
                                  text="Remove bets",
                                  bg="gold",
                                  bd=1,
                                  command=dble_bets_sub_2)
      dble_bet_sub_but_2.place(x=580, y=180)
      
      def dble_bet_check():
        if 4<dble_bets_1<101 and 4<dble_bets_2<101:  # If both player's bets are between this range
          dble_buttons_state_play()  # Carry on with the process
        else:
          print("You cannot have bets below $5 and above $100 \n") # Otherwise ask them to change it
      
      
      def dble_buttons_state_play():  # Disabled the buttons associated with changing bets
          dble_bet_add_but_1.config(state=DISABLED)
          dble_bet_sub_but_1.config(state=DISABLED)
          dble_bet_add_but_2.config(state=DISABLED)
          dble_bet_sub_but_2.config(state=DISABLED)
          dble_confirm_bets.config(state=DISABLED)
          dble_cnfrm_bets()
      
      
      def dble_cnfrm_bets(): 
          global dble_play_1_crd_1
          global dble_play_1_crd_2
          global dble_play_1_ttl
          global dble_play_2_crd_1
          global dble_play_2_crd_2
          global dble_play_2_ttl
          dble_play_1_crd_1 = random.randint(1, 11) # Generate the players cards
          dble_play_1_crd_2 = random.randint(1, 11)
          dble_play_1_ttl = (dble_play_1_crd_1+dble_play_1_crd_2)  # Add player 1 cards to give their total
          dble_play_2_crd_1 = random.randint(1, 11)
          dble_play_2_crd_2 = random.randint(1, 11)
          dble_play_2_ttl = (dble_play_2_crd_1+dble_play_2_crd_2)  # Add player 2 cards to give their total
          print("Player 1 cards: ", dble_play_1_crd_1, dble_play_1_crd_2) # Print players cards
          print(dble_play_1_ttl, "\n")
          print("Player 2 cards: ", dble_play_2_crd_1, dble_play_2_crd_2)
          print(dble_play_2_ttl, "\n")
          if dble_play_1_ttl == 21:  # If player 1's cards total to 21
              print("Player 1 wins!!") # They win
              dble_bet_add_but_1.config(state=NORMAL) # Enable the bet buttons for both players
              dble_bet_sub_but_1.config(state=NORMAL)
              dble_bet_add_but_2.config(state=NORMAL)
              dble_bet_sub_but_2.config(state=NORMAL)
              dble_confirm_bets.config(state=NORMAL)
              dble_add_creds_1()  # Add credits to player 1
              dble_sub_creds_2()  # Take credist from player 2
          if dble_play_1_ttl > 21:  # If Player 1's card total go over 21
              print("Player 1 loses")  # They lose
              dble_sub_creds_1()  # Take p1's credits
              dble_hit_but_2.config(state=NORMAL)
              dble_stay_but_2.config(state=NORMAL)
              dble_double_but_2.config(state=NORMAL)
          if dble_play_2_ttl == 21: # If player 2's cards total to 21
              print("Player 2 wins!!")  # They win
              dble_bet_add_but_1.config(state=NORMAL)
              dble_bet_sub_but_1.config(state=NORMAL)
              dble_bet_add_but_2.config(state=NORMAL)
              dble_bet_sub_but_2.config(state=NORMAL)
              dble_confirm_bets.config(state=NORMAL)
              dble_add_creds_2()
              dble_sub_creds_1()
          if dble_play_2_ttl > 21:
              print("Player 2 loses")
              dble_sub_creds_2()
              dble_hit_but_1.config(state=NORMAL)
              dble_stay_but_1.config(state=NORMAL)
              dble_double_but_1.config(state=NORMAL)
          if dble_play_1_ttl and dble_play_2_ttl < 21: # Play on if both players cards are below 21
              print("Choose an action (player 1 goes first) \n")
              dble_hit_but_1.config(state=NORMAL)
              dble_stay_but_1.config(state=NORMAL)
              dble_double_but_1.config(state=NORMAL)
      
      dble_confirm_bets = Button(dble_frame, # Create button for confirming both players' bets
                                 text="Confirm bets",
                                 bg="orange",
                                 bd=1,
                                 command=dble_bet_check)
      dble_confirm_bets.place(x=300, y=450)
      
      
      def dble_crd_check():  # Check which players takes on the dealer
          dble_hit_but_2.config(state=DISABLED)
          dble_stay_but_2.config(state=DISABLED)
          dble_double_but_2.config(state=DISABLED)
          dble_cnfrm_crds_but.config(state=DISABLED)
          global dble_play_1_ttl
          global dble_play_2_ttl
          if dble_play_1_ttl > dble_play_2_ttl:
              print("Player 2 is out \n")
              dble_sub_creds_2()
              dble_play_1_v_deal()
          if dble_play_1_ttl < dble_play_2_ttl:
              print("Player 1 is out \n")
              dble_sub_creds_1()
              dble_play_2_v_deal()
          if dble_play_1_ttl == dble_play_2_ttl:
              print("Its a draw \n")
              dble_bet_add_but_1.config(state=NORMAL)
              dble_bet_sub_but_1.config(state=NORMAL)
              dble_bet_add_but_2.config(state=NORMAL)
              dble_bet_sub_but_2.config(state=NORMAL)
              dble_confirm_bets.config(state=NORMAL) 
              
      
      
      # Player 1 vs Dealer
      def dble_play_1_v_deal():
          dble_crd_1_deal = random.randint(1, 11)
          dble_crd_2_deal = random.randint(1, 11)
          dble_deal_crd_ttl = (dble_crd_1_deal + dble_crd_2_deal)
          print("Dealer cards", dble_crd_1_deal, dble_crd_2_deal, "\n")
          if dble_deal_crd_ttl == 21:
              print("Dealer wins \n")
              dble_sub_creds_1()
          if dble_deal_crd_ttl > 21:
              print("Player 1 wins \n")
              dble_add_creds_1()
          if dble_deal_crd_ttl > dble_play_1_ttl:
              print("Dealer wins \n")
              dble_sub_creds_1()
              dble_bet_add_but_1.config(state=NORMAL)
              dble_bet_sub_but_1.config(state=NORMAL)
              dble_bet_add_but_2.config(state=NORMAL)
              dble_bet_sub_but_2.config(state=NORMAL)
              dble_confirm_bets.config(state=NORMAL)
          if dble_deal_crd_ttl < dble_play_1_ttl:
              print("Player 1 wins \n")
              dble_add_creds_1()
              dble_bet_add_but_1.config(state=NORMAL)
              dble_bet_sub_but_1.config(state=NORMAL)
              dble_bet_add_but_2.config(state=NORMAL)
              dble_bet_sub_but_2.config(state=NORMAL)
              dble_confirm_bets.config(state=NORMAL)
          if dble_deal_crd_ttl == dble_play_1_ttl:
                print("Its a draw")
                dble_bet_add_but_1.config(state=NORMAL)
                dble_bet_sub_but_1.config(state=NORMAL)
                dble_bet_add_but_2.config(state=NORMAL)
                dble_bet_sub_but_2.config(state=NORMAL)
                dble_confirm_bets.config(state=NORMAL)
      
      # Player 2 vs Dealer
      def dble_play_2_v_deal():
          dble_crd_1_deal = random.randint(1, 11)
          dble_crd_2_deal = random.randint(1, 11)
          dble_deal_crd_ttl = (dble_crd_1_deal + dble_crd_2_deal)
          dble_crd_hit_1 = random.randint(1, 11)
          dble_crd_hit_2 = random.randint(1, 11)
          print("Dealer cards", dble_crd_1_deal, dble_crd_2_deal, "\n")
          if dble_deal_crd_ttl == 21:
              print("Dealer wins \n")
              dble_sub_creds_2()
          if dble_deal_crd_ttl > 21:
              print("Player 2 wins \n")
              dble_add_creds_2()
          if dble_deal_crd_ttl > dble_play_2_ttl:
              print("Dealer wins \n")
              dble_sub_creds_2()
              dble_bet_add_but_1.config(state=NORMAL)
              dble_bet_sub_but_1.config(state=NORMAL)
              dble_bet_add_but_2.config(state=NORMAL)
              dble_bet_sub_but_2.config(state=NORMAL)
              dble_confirm_bets.config(state=NORMAL)
          if dble_deal_crd_ttl < dble_play_2_ttl:
              print("Player 2 wins \n")
              dble_add_creds_2()
              dble_bet_add_but_1.config(state=NORMAL)
              dble_bet_sub_but_1.config(state=NORMAL)
              dble_bet_add_but_2.config(state=NORMAL)
              dble_bet_sub_but_2.config(state=NORMAL)
              dble_confirm_bets.config(state=NORMAL)
          if dble_deal_crd_ttl == dble_play_2_ttl:
              print("Its a draw")
              dble_bet_add_but_1.config(state=NORMAL)
              dble_bet_sub_but_1.config(state=NORMAL)
              dble_bet_add_but_2.config(state=NORMAL)
              dble_bet_sub_but_2.config(state=NORMAL)
              dble_confirm_bets.config(state=NORMAL)
      
      # Hit function for P1
      def dble_hit_1():
          global dble_play_1_ttl
          global dble_crd_hit_1
          dble_crd_hit_1 = random.randint(1, 11)
          dble_play_1_ttl += dble_crd_hit_1
          print("Player 1 hit card: ", dble_crd_hit_1)
          print(dble_play_1_ttl, "\n")
          if dble_play_1_ttl == 21:
              print("Player 1 wins")
              dble_add_creds_1()
              dble_cnfrm_crds_but.config(state=DISABLED)
          if dble_play_1_ttl > 21:
              print("Player 1 is busted")
              dble_sub_creds_1()
              dble_hit_but_2.config(state=DISABLED)
              dble_stay_but_2.config(state=DISABLED)
              dble_double_but_2.config(state=DISABLED)
              dble_play_2_v_deal()
              dble_cnfrm_crds_but.config(state=DISABLED)
          if dble_play_1_ttl < 21:
              print("Play on \n")
              dble_hit_but_1.config(state=DISABLED)
              dble_stay_but_1.config(state=DISABLED)
              dble_double_but_1.config(state=DISABLED)
              dble_hit_but_2.config(state=NORMAL)
              dble_stay_but_2.config(state=NORMAL)
              dble_double_but_2.config(state=NORMAL)
      
      # Doubles bets of P1
      def dble_double_1():
          global dble_bets_1
          dble_bets_1 *= 2
          dble_bets_1_counter.set("Bets: ${:.2f}".format(dble_bets_1))
          dble_hit_but_1.config(state=DISABLED)
          dble_stay_but_1.config(state=DISABLED)
          dble_double_but_1.config(state=DISABLED)
          dble_hit_but_2.config(state=NORMAL)
          dble_stay_but_2.config(state=NORMAL)
          dble_double_but_2.config(state=NORMAL)
      
      # Stay action for P1
      def dble_stay_1():
          print("Player 1 stays \n")
          dble_hit_but_1.config(state=DISABLED)
          dble_stay_but_1.config(state=DISABLED)
          dble_double_but_1.config(state=DISABLED)
          dble_hit_but_2.config(state=NORMAL)
          dble_stay_but_2.config(state=NORMAL)
          dble_double_but_2.config(state=NORMAL)
      
      
      dble_hit_but_1 = Button(dble_frame, # P1 Hit button
                              text="Hit",
                              bg="white",
                              bd=1,
                              command=dble_hit_1)
      dble_hit_but_1.place(x=62, y=340)
      
      dble_stay_but_1 = Button(dble_frame, # P1 Stay button
                               text="Stay",
                               bg="white",
                               bd=1,
                               command=dble_stay_1)
      dble_stay_but_1.place(x=20, y=380)
      
      dble_double_but_1 = Button(dble_frame, # P1 Double Button
                                 text="Double",
                                 bg="white",
                                 bd=1,
                                 command=dble_double_1)
      dble_double_but_1.place(x=90, y=380)
      
      
      def dble_hit_2():  # P2 hit function
          global dble_play_2_ttl
          global dble_crd_hit_2
          dble_crd_hit_2 = random.randint(1,11)
          dble_play_2_ttl += dble_crd_hit_2
          print("Player 2 hit card: ", dble_crd_hit_2)
          print(dble_play_2_ttl, "\n")
          if dble_play_2_ttl == 21:
              print("Player 2 wins")
              dble_add_creds_2()
              dble_cnfrm_crds_but.config(state=DISABLED)
          if dble_play_2_ttl > 21:
              print("Player 2 is busted")
              dble_sub_creds_2()
              dble_hit_but_2.config(state=DISABLED)
              dble_stay_but_2.config(state=DISABLED)
              dble_double_but_2.config(state=DISABLED)
              dble_cnfrm_crds_but.config(state=DISABLED)
              dble_play_1_v_deal()
          if dble_play_2_ttl < 21:
              print("Play on \n")
              dble_hit_but_1.config(state=NORMAL)
              dble_stay_but_1.config(state=NORMAL)
              dble_double_but_1.config(state=NORMAL)
              dble_cnfrm_crds_but.config(state=NORMAL)
            
      
      
      def dble_double_2():  # P2 double bets function
          global dble_bets_2
          dble_bets_2 *= 2
          dble_bets_2_counter.set("Bets: ${:.2f}".format(dble_bets_2))
          dble_hit_but_2.config(state=DISABLED)
          dble_stay_but_2.config(state=DISABLED)
          dble_double_but_2.config(state=DISABLED)
          dble_hit_but_1.config(state=NORMAL)
          dble_stay_but_1.config(state=NORMAL)
          dble_double_but_1.config(state=NORMAL)
          dble_cnfrm_crds_but.config(state=NORMAL)
      
      def dble_stay_2():  # P2 stay function
          print("Player 2 stays \n")
          dble_hit_but_2.config(state=DISABLED)
          dble_stay_but_2.config(state=DISABLED)
          dble_double_but_2.config(state=DISABLED)
          dble_hit_but_1.config(state=NORMAL)
          dble_stay_but_1.config(state=NORMAL)
          dble_double_but_1.config(state=NORMAL)
          dble_cnfrm_crds_but.config(state=NORMAL)
      
      
      dble_hit_but_2 = Button(dble_frame,  # P2 hit button
                              text="Hit",
                              bg="white",
                              bd=1,
                              command=dble_hit_2)
      dble_hit_but_2.place(x=583, y=340)
      
      dble_stay_but_2 = Button(dble_frame,  # P2 stay button
                               text="Stay",
                               bg="white",
                               bd=1,
                               command=dble_stay_2)
      dble_stay_but_2.place(x=540, y=380)
      
      dble_double_but_2 = Button(dble_frame,  # P2 double bets button
                                 text="Double",
                                 bg="white",
                                 bd=1,
                                 command=dble_double_2)
      dble_double_but_2.place(x=610, y=380)
      
      # Confirms cards
      dble_cnfrm_crds_but = Button(dble_frame, text="Confirm Cards", bg="orange", bd=1, command=dble_crd_check)
      dble_cnfrm_crds_but.place(x=295, y=400)
      
      dble_hit_but_1.config(state=DISABLED)  # Disables card action buttons at start
      dble_stay_but_1.config(state=DISABLED)
      dble_double_but_1.config(state=DISABLED)
      dble_hit_but_2.config(state=DISABLED)
      dble_stay_but_2.config(state=DISABLED)
      dble_double_but_2.config(state=DISABLED)
      dble_cnfrm_crds_but.config(state=DISABLED)
      

      def dble_rules():
        dble_rules_win = Toplevel(dble_frame)
        dble_rules_but.config(state=DISABLED)
          
        def close_dble_rules():  # If window is closed
                dble_rules_but.config(state=NORMAL)
                dble_rules_win.destroy()

        dble_rules_win.protocol("WM_DELETE_WINDOW",
                                    partial(close_dble_rules))

        dble_rules_frme = Frame(dble_rules_win, width=665, height=435, bg="maroon")
        dble_rules_frme.grid()

        dble_rules_lbl = Label(dble_rules_frme, text="Rules", font="Times 14", justify=CENTER, bg="gold", padx=400)
        dble_rules_lbl.place(x=-100,y=0)

        dble_rules_txt = Label(dble_rules_frme, text='''
        * Aim: The aim of the game is win by one of the following ways:
          Have 21 from your card total (Instant win)
          Have a higher card total then the dealer (who you play against)
          The dealer is busted (their card total goes over 21)
        * The Game: Both players start off by adding or removing bets using the buttons and when you are 
          happy with your amount, continue the game by pressing confirm bets.
          The game will then deal out your cards. If a player’s cards total 21, they instantly win, if a player’s 
          cards total over 21, they instantly lose, otherwise both players move on to the next 
          phase where you can choose your action.
          Players have three actions to choose from:
          - Hit: Gain an extra card
          - Stay: Do nothing
          - Double: Double the amount of bets
        	After pressing confirm cards, the game will check the cards total. Which ever player   
          has the highest total will move on to face the dealer. The game will compare the 
          totals of the player’s cards. They are now faced with the following scenarios:
          - If the dealer’s cards totals 21, both players lose
          - If the dealer’s cards goes over 21, they are busted and that player wins
          - If the dealer has a higher card total than the player and is under 21, players lose
          - If the you have a higher card total than the dealer, that player wins win
          - If you draw, no one wins
        * End: If a player wins, their bets will be added to their credits, if they lose, their bets will be taken 
          from their credits.
          You can either exit or continue the game
        ''', font="Time 10", justify=LEFT, bg="lawn green")
        dble_rules_txt.place(x=-30, y=25)
        
      dble_rules_but = Button(dble_frame, text="Rules", bg="orange", bd=1, command=dble_rules)  # Rules buttons
      dble_rules_but.place(x=580, y=430)
      
      
      def dble_exit():  # Exit button
          dble_exit_win = Toplevel(root)
      
          dble_exit_but.config(state=DISABLED)
      
          def close_dble_exit():  # If either the back button or window is closed
              dble_exit_but.config(
                  state=NORMAL)  # revert the exit player button back to normal
              sngle_exit_win.destroy()
      
          dble_exit_win.protocol("WM_DELETE_WINDOW", partial(close_dble_exit))
      
          dble_exit_frame = Frame(dble_exit_win,
                                   width=200,
                                   height=100,
                                   bg="lawngreen")
          dble_exit_frame.grid()
      
          dble_exit_text = Label(dble_exit_frame,
                                  text="Are you sure?",
                                  font="Times 14",
                                  justify=CENTER,
                                  bg="lawngreen")
          dble_exit_text.place(x=10, y=0)
      
          def dble_exit_y():  # Exits programn
              dble_exit_but.config(state=NORMAL)
              dble_play_win.destroy()
              dble_exit_win.destroy()
      
          dble_ext_y_but = Button(dble_exit_frame,
                                   text="Yes",
                                   font="Times 10",
                                   bd=1,
                                   command=dble_exit_y)
          dble_ext_y_but.place(x=20, y=50)
      
          dble_ext_n_but = Button(dble_exit_frame,
                                   text="No",
                                   font="Times 10",
                                   bd=1,
                                   command=close_dble_exit)
          dble_ext_n_but.place(x=130, y=50)
      
      
      dble_exit_but = Button(dble_frame,  # Exit button
                              text="Exit",
                              bg="orange",
                              bd=1,
                              command=dble_exit)
      dble_exit_but.place(x=589, y=460)


    def prnt_dble_usrnme():  # When confirmed is pushed...
        dble_username1 = dble_usrnme_entry_box1.get()  # Store the usr input in
        dble_username2 = dble_usrnme_entry_box2.get()  # these two variables
        print("Hello", dble_username1, "&",
              dble_username2)  # and print this statement in the terminal
        print("If you need help, click rules\n")
        Double_Player()

    dble_usrnme_entry_box1 = Entry(dble_usrnme_frame,
                                   width=20,
                                   font="arial 12")  # Make two
    dble_usrnme_entry_box1.place(x=130, y=100)  # entry
    dble_usrnme_entry_box2 = Entry(dble_usrnme_frame,
                                   width=20,
                                   font="arial 12")  # boxes
    dble_usrnme_entry_box2.place(x=130, y=150)

    dble_usrnme_confirm = Button(
        dble_usrnme_frame,
        text="Confirm",
        bg="gold",  # Confirm button for
        font="arial 10 bold",
        command=prnt_dble_usrnme)  # username input
    dble_usrnme_confirm.place(x=185, y=200)

    dble_usrnme_back = Button(
        dble_usrnme_frame,
        text="Back",
        bg="orange",  # Creates back button
        font="arial 10 bold",
        command=partial(close_dble_usrnme))
    dble_usrnme_back.place(x=195, y=240)


dble_but = Button(home_frame,
                  text="Two Players",
                  font="arial 10 bold",
                  bd=1,
                  bg="orange",
                  command=Double_Username)
dble_but.place(x=195, y=155)


def scre_window():
    sngle_scores_win = Toplevel(root)

    sngle_but.config(state=DISABLED)
    dble_but.config(state=DISABLED)
    sngle_scores_button.config(state=DISABLED)

    def close_sngle_scores():  # If either the back button or window is closed
        f.close()
        sngle_scores_button.config(
            state=NORMAL)  # revert the single player button back to normal
        sngle_but.config(state=NORMAL)
        dble_but.config(state=NORMAL)
        sngle_scores_win.destroy()

    sngle_scores_win.protocol("WM_DELETE_WINDOW", partial(close_sngle_scores))

    sngle_scores_frame = Frame(sngle_scores_win,
                              width=300,
                              height=500,
                              bg="maroon")
    sngle_scores_frame.grid()

    sngle_scores_header = Label(sngle_scores_frame,
                               text="Single Player Scores",
                               font="Times 14 bold",
                               justify=CENTER,
                               bg="gold",
                               padx=170,
                               pady=10)
    sngle_scores_header.place(x=-140, y=0)

    f = open("Single_Player_Scores.txt", "r")
  
    sngle_scores_txt = Label(sngle_scores_frame,
                            text=f.read(),
                            font="Times 10",
                            justify=LEFT,
                            bg="orange",
                            padx=75)
    sngle_scores_txt.place(x=-10,y=45)

    sngle_scores_back = Button(
        sngle_scores_frame,
        text="Back",
        bg="orange",  # Creates back button
        font="arial 10 bold",
        command=partial(close_sngle_scores))
    sngle_scores_back.place(x=95, y=240)

sngle_scores_button = Button(home_frame, text="Singleplayer Scores", font="arial 10 bold", bg="orange", command=scre_window) # Singleplayer scores button
sngle_scores_button.place(x=165, y=210)

root.mainloop()  # Loops the program until stopped/exited