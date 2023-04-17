def load_players(file):
    lastnames = []
    averages = []
    with open(file, 'r') as f:
        for line in f:
            name, avg = line.strip().split(',')
            lastnames.append(name)
            averages.append(float(avg))
    return lastnames, averages

def display_players(lastnames, averages):
    print("Player Names and Batting Averages:")
    for i in range(len(lastnames)):
        print(f"{lastnames[i]} - {averages[i]}")

def search_player(lastname, lastnames, averages):
    for i in range(len(lastnames)):
        if lastnames[i] == lastname:
            return f"{lastnames[i]} - {averages[i]}"
    return "Player not found."

# load player data from file
file = "players.txt"
lastnames, averages = load_players(file)

# display player data
display_players(lastnames, averages)

# search for a player's batting average based on user input
while True:
    lastname = input("Enter a player's last name to search for their batting average (or 'quit' to exit): ")
    if lastname == 'quit':
        break
    result = search_player(lastname, lastnames, averages)
    print(result)

