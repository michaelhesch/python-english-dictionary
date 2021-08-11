import mysql.connector

# connect to external mysql database with mysql connector library
# database credentials removed for git commit
connection = mysql.connector.connect(
  user = "#",
  password = "#",
  host = "#",
  database = "#"
)

# create cursor to interact with db
cursor = connection.cursor()

# take in user input 
word = input("Please enter a word: ")

# pass sql selection to server with word input by user and return results
query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
results = cursor.fetchall()

# loop over results tuples to print out only the definitions
for result in results:
  print(result[1])