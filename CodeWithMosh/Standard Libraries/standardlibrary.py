import sqlite3
import json
import csv
from pathlib import Path
from zipfile import ZipFile

path = Path(r"C:\Users\Alexis\Documents\Python Scripts\CodeWithMosh")
# print(path.name)

paths = [p for p in path.iterdir() if p.is_dir()]
pyfiles = [p for p in path.rglob("*.py")]
# print(paths)
# print(pyfiles)

# with ZipFile("files.zip", "w") as zip:
#    for path in Path(r"C:\Users\Alexis\Documents\Python Scripts\CodeWithMosh").rglob("*.*"):
#        zip.write(path)


# Working with CSV files. Addd ", w" for write mode if you want to edit
with open("../data.csv") as file:
    #writer = csv.writer(file)
    #writer.writerow(["trx_id", "trx_number", "price"])
    #writer.writerow([1300, 145, 3020])
    #writer.writerow([3100, 545, 6300])
    #writer.writerow([8100, 435, 4300])
    reader = csv.reader(file)
    for row in reader:
        print(row)

# working with JSON

#data = Path("../movies.json").read_text()
#movies = json.loads(data)
#print(movies[0]["title"])


# Working with Sqlite
# Writing to the database

# with sqlite3.connect("MyFirstSQLiteDB.sqlite3") as conn:
 #   command = "INSERT INTO Movies VALUES(?, ?, ?)"
 #   for movie in movies:
  #      conn.execute(command, tuple(movie.values()))
  #  conn.commit()

#reading from the database
with sqlite3.connect("MyFirstSQLiteDB.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor  = conn.execute(command)
    for row in cursor:
        print(row)

#Opening web browsers

#import webbrowser

#print("Deployment completed")
#webbrowser.open("http://www.google.com")

