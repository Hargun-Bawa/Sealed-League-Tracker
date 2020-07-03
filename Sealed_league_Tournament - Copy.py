import sqlite3
from tkinter import *
from tkinter import messagebox

"""THIS PROGRAM IS MEANT TO KEEP TRACK OF PLAYERS IN A WEEKLY TOURNAMENT THAT DIVIDES THE PLAYERS INTO PODS OF FOUR. 
IT WILL KEEP TRACK OF POINT TOTALS, WEEKLY RECORDS, AND WEEKLY MATCHES. """

# Connect or create a database for the sealed league information to be stored
conn = sqlite3.connect('sealed_leagues.db')

# Create a cursor to interact with the database
c = conn.cursor()

# Creates constants that refer to specific players in the Database
c.execute("SELECT player_name FROM league WHERE rowid = 1")
player_1 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 2")
player_2 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 3")
player_3 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 4")
player_4 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 5")
player_5 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 6")
player_6 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 7")
player_7 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 8")
player_8 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 9")
player_9 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 10")
player_10 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 11")
player_11 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 12")
player_12 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 13")
player_13 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 14")
player_14 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 15")
player_15 = c.fetchall()[0]
c.execute("SELECT player_name FROM league WHERE rowid = 16")
player_16 = c.fetchall()[0]


def individual_page(player):
    c.execute("SELECT * FROM league WHERE player_name=(?)", player)
    player_info = c.fetchall()
    print(player_info)

def players_page():
    w5 = Toplevel()
    players = [player_1,
               player_2,
               player_3,
               player_4,
               player_5,
               player_6,
               player_7,
               player_8,
               player_9,
               player_10,
               player_11,
               player_12,
               player_13,
               player_14,
               player_15,
               player_16]

    rownum = 0
    for player in players:
        button = Button(w5, text=str(player[0]),command=lambda: individual_page(player))
        button.grid(sticky=W, row=rownum, column=0)
        rownum += 1


def show_standings():
    window_4 = Toplevel()
    players = [player_1,
               player_2,
               player_3,
               player_4,
               player_5,
               player_6,
               player_7,
               player_8,
               player_9,
               player_10,
               player_11,
               player_12,
               player_13,
               player_14,
               player_15,
               player_16]
    final = ""
    for player in players:
        c.execute("SELECT total_score FROM league WHERE player_name = (?)", player)
        score = c.fetchall()
        total = str(player[0]) + "\t" + str(score[0])
        final = final + "\n" + total

    tex = Text(window_4, height=50, borderwidth=0)
    tex.insert(1.0, final)
    tex.pack()
    tex.configure(state="disabled")


# CREATES A COPYABLE WINDOW WITH ALL OF THE PODS OF PLAYERS LISTED
def show_pods(pods):
    pod_num = 1
    final_string = ""
    for pod in pods:
        new_string = "Pod " + str(pod_num) + "\n\n"
        for player in pod:
            new_string = new_string + str(player[0]) + ",\n"
        final_string = final_string + "\n" + new_string
        pod_num += 1
    w3 = Toplevel()
    final = final_string
    tex = Text(w3, height=50, borderwidth=0)
    tex.insert(1.0, final)
    tex.pack()
    tex.configure(state="disabled")


# WORK IN PROGRESS, IS SUPPOSED TO MAKE A WINDOW THAT HAS MENUS FOR EACH MATCH, YOU SHOULD BE ABLE TO SELECT RECORD OF
# THE MATCH AND SAVE IT TO THE DATABASE
def report_pairings(pods):
    # THIS IS SUPPOSED TO BE THE ACTUAL SAVE BUTTON FUNCTION
    def update_score():
        pass

    w4 = Toplevel()
    matches = []
    # FROM EACH POD CREATES SIX PAIRS MADE OF EACH OF THE FOUR POD MEMBERS.
    for pod in pods:
        for player in pod:
            for player2 in pod:
                if player != player2:
                    new_list = [player[0], player2[0]]
                    new_list.sort()
                    if new_list not in matches:
                        matches.append(new_list)

    # REFORM PODS BUT THIS TIME WITH MATCHES NOT JUST PLAYERS
    pod_1 = matches[0:6]
    pod_2 = matches[6:12]
    pod_3 = matches[12:18]
    pod_4 = matches[18:24]
    match_pods = [pod_1, pod_2, pod_3, pod_4]
    for pod in match_pods:
        for match in pod:
            print(match)
    # WORK IN PROGRESS CREATES THE DROPDOWN MENUS FOR EACH PAIR AND SEPARATES THE PODS BY COLUMN
    col = -1
    podnum = 1
    for pod in match_pods:
        pod.sort()
        col += 1
        label2 = Label(w4, text="Pod " + str(podnum), padx=10, pady=25)
        label2.grid(row=0, column=col)
        r = 1
        podnum += 1

        # FILLS IN THE COLUMNS WITH THE MENUS, WORKING ON HOW TO RETRIEVE THE VALUES FROM THE MENUS AND UPDATE THE
        # DATABASE
        for match in pod:
            scores = [
                match[0] + "  0-0  " + match[1],
                match[0] + "  2-0  " + match[1],
                match[0] + "  2-1  " + match[1],
                match[0] + "  1-2  " + match[1],
                match[0] + "  0 -2  " + match[1]
            ]
            clicked = StringVar()
            clicked.set(match[0] + "  0-0  " + match[1])
            drop = OptionMenu(w4, clicked, *scores)
            drop.grid(column=col, row=r, padx=5, pady=10)

            r += 1
    # TRYING TO MAKE ONE BUTTON THAT UPLOADS ALL BOXES ONTO THE DATABASE
    #save_button = Button(w4, text="Update Results", command=update_score, padx=50)
    #save_button.grid(row=12, column=0, columnspan=4, pady=20)


# BREAKS THE 16 PLAYERS INTO PREDETERMINED PODS OF FOUR AND ALLOWS YOU TO NAVIGATE TO A PAGE WHERE THE PODS ARE
# LISTED TO BE COPIED, OR TO A PAGE WHERE YOU CAN INSERT THE RESULTS OF THE MATCHES FOR THE WEEK.
def week_one():
    w1 = Toplevel()
    pod_1 = [player_1, player_2, player_3, player_4]
    pod_2 = [player_5, player_6, player_7, player_8]
    pod_3 = [player_9, player_10, player_11, player_12]
    pod_4 = [player_13, player_14, player_15, player_16]
    pods = [pod_1, pod_2, pod_3, pod_4]

    show_pods_button = Button(w1, text="Show pods", command=lambda: show_pods(pods))
    show_pods_button.grid(row=1, column=0)

    report_scores_button = Button(w1, text="Report scores", command=lambda: report_pairings(pods))
    report_scores_button.grid(row=2, column=0)


# On creation of a new League creates a window for user to enter up to 16 names, and then commits them to the database.
def enter_players():
    players = []

    # Takes the user input and puts it into a list, when the list hits maximum capacity for the tourney prompts user
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
    player_button = (Button(players_screen, text="Players", padx=29, pady=5, command=players_page))
    player_button.grid(row=0, column=0, padx=15, pady=5)

    standings_button = (Button(players_screen, text="Standings", padx=21, pady=5, command=show_standings))
    standings_button.grid(row=1, column=0, padx=15, pady=5)

    week_one_button = (Button(players_screen, text="Week One", padx=19, pady=5, command=week_one))
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
