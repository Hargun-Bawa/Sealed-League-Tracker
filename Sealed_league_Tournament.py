import sqlite3
from tkinter import *
from tkinter import messagebox

"""THIS PROGRAM IS MEANT TO KEEP TRACK OF PLAYERS IN A WEEKLY TOURNAMENT THAT DEVIDES THE PLAYERS INTO PODS OF FOUR. 
IT WILL KEEP TRACK OF POINT TOTALS, WEEKLY RECORDS, AND WEEKLY MATCHES. """

# Connect or create a database for the sealed league information to be stored
conn = sqlite3.connect('sealed_leagues.db')

# Create a cursor to interact with the database
c = conn.cursor()


# On creation of a new League creates a window for user to enter up to 16 names, and then commits them to the database.
def enter_players():
    players = []

    # Takes the user input and puts it into a list, when the list hits maximum capacity for the tourney promts user
    # to close the windows And commits the list to the database
    def save_player():

        if len(players) < 15:
            new_player = player_entry.get()
            players.append(new_player)
            player_entry.delete(0, END)
        else:
            messagebox.showinfo("Max players reached", "Close all windows and load the league!")
            new_player = player_entry.get()
            players.append(new_player)
            player_entry.delete(0, END)
            for i in players:
                c.execute("INSERT INTO league (player_name) VALUES(?)", (i,))
                conn.commit()

    win2 = Toplevel()
    win2.title("Enter Players")

    label = Label(win2, text='enter player names, max of 16')
    label.grid(row=0, column=0)
    player_entry = Entry(win2)
    player_entry.grid(row=1, column=0)

    save_button = Button(win2, text="save", command=save_player)
    save_button.grid(row=2, column=0)


# If a league already exists, it drops the table and creates a new empty table with the same name. Creates columns
# for player name, weekly scores, weekly records, and total point score. Then commits the new table to the database
# and asks user for player names.

def make_table():
    c.execute("DROP TABLE league")
    c.execute("""CREATE TABLE league (
        player_name text,
        week_one_scores integer,
        week_one_results text,
        week_two_scores integer,
        week_two_results text,
        week_three_scores integer,
        week_three_results text,
        week_four_scores integer,
        week_four_results text,
        week_five_scores integer,
        week_five_results text,
        week_six_scores integer,
        week_six_results text,
        total_score integer
        
    )""")

    conn.commit()
    enter_players()


# Creates a window for the navigation menu of an in progress league.
def load_league():
    players_screen = Toplevel()
    player_button = (Button(players_screen, text="Players", padx=29, pady=5))
    player_button.grid(row=0, column=0, padx=15, pady=5)

    standings_button = (Button(players_screen, text="Standings", padx=21, pady=5))
    standings_button.grid(row=1, column=0, padx=15, pady=5)

    week_one_button = (Button(players_screen, text="Week One", padx=19, pady=5))
    week_one_button.grid(row=2, column=0, padx=15, pady=5)

    week_two_button = (Button(players_screen, text="Week Two", padx=19, pady=5))
    week_two_button.grid(row=3, column=0, padx=15, pady=5)

    week_three_button = (Button(players_screen, text="Week Three", padx=15, pady=5))
    week_three_button.grid(row=4, column=0, padx=15, pady=5)

    week_four_button = (Button(players_screen, text="Week Four", padx=20, pady=5))
    week_four_button.grid(row=5, column=0, padx=15, pady=5)

    week_five_button = (Button(players_screen, text="Week Five", padx=20, pady=5))
    week_five_button.grid(row=6, column=0, padx=15, pady=5)


# Prompts user to confirm the creation of a new league. Creating a new league will drop the information of the
# previous league hence the forewarning
def new_league():
    win = Toplevel()
    win.title("new league")

    label = (Label(win, text='Are you sure?\nCreating a new league will delete the old one.'))
    label.grid(row=0, column=0, columnspan=2, padx=30)

    yes_button = (Button(win, text='Yes', command=make_table))
    yes_button.grid(row=2, column=0, pady=15)

    no_button = (Button(win, text='No', command=win.destroy))
    no_button.grid(row=2, column=1, pady=15)


# Creates the opening window for the application prompting either the loading of an old league, or the creation of a
# new one.

root = Tk()
root.title("Sealed League")

header = Label(root, text="House of Cards Sealed Leagues", pady=25)
header.config(font=50)

header.grid(row=0, column=0)

new_league_button = (Button(root, text="New", pady=15, padx=40, command=new_league))
new_league_button.grid(row=1, column=0, pady=10)

load_league_button = (Button(root, text="Load", pady=15, padx=39, command=load_league))
load_league_button.grid(row=2, column=0, pady=10)

root.mainloop()
