import csv
import datetime
import sqlite3


print("Welcome to Stranalyzer. Your only strategy analyser")


def trade():
    current_date = datetime.date.today()
    stras = ["SNR + Stochastic Oscillator",
             "TradingView STO RSI,STO DMI,Bollinger"]
    for number, stra in enumerate(stras):
        print(number, stra)

    stra_index = int(input("What strategy did you use today: "))
    stra_name = stras[stra_index]
    print(f"You have selected {stra_name}")
    trades = int(
        input("Please input the number of trades you have taken today: "))
    won = int(input("How many did you win today: "))
    if won > trades:
        print("You cannot win more than you traded. Use your head")
    else:
        percentage = int((won/trades)*100)
        print(f"Your strategy is {percentage}% accurate")
        if percentage >= 80:
            print("Keep doing what you doing. It's working")
        elif percentage <= 50:
            print("Change your strategy. It's bad")
        else:
            print("Please work on your strategy")
    with open('stranalyzed.csv', 'a') as stranalyzer:
        thefile = csv.writer(stranalyzer)
        # thefile.writerow(["Date", "Strategy Name", "Percentage"])
        thefile.writerow(
            [current_date, stra_name, percentage])
        print("File updated successfully")
    # Working with Sqlite
# Writing to the database

    with sqlite3.connect("Stranalyze_db.sqlite3") as conn:
        #conn.execute("CREATE TABLE Strategy(date,stra_name,percent)")
        command = "INSERT INTO Strategy VALUES(?, ?, ?)"
        conn.execute(command,
                     (current_date, stra_name, percentage))
        conn.commit()
        print("Databse updated")

        # reading from the database
    with sqlite3.connect("Stranalyze_db.sqlite3") as conn:
        command = "SELECT stra_name,avg(percent) as Percent FROM Strategy GROUP BY stra_name"
        cursor = conn.execute(command)
        for row in cursor:
            print(row)


trade()
