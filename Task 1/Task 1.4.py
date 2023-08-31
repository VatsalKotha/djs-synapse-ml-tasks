import random

class ChessPlayer:
    def __init__(self, name, age, elo, tenacity, is_boring):
        self.name = name
        self.age = age
        self.elo = elo
        self.tenacity = tenacity
        self.is_boring = is_boring
        self.score = 0
    
def simulateMatch(player1, player2):
    elo_diff = abs(player1.elo - player2.elo)
    
    if elo_diff > 100:
        if player1.elo > player2.elo:
            player1.score += 1
        else:
            player2.score += 1
    elif elo_diff >= 50:
        lower_elo_player = player1 if player1.elo < player2.elo else player2
        higher_elo_player = player2 if player1.elo < player2.elo else player1
        
        random_factor = random.randint(1, 10)
        tenacity_factor = random_factor * lower_elo_player.tenacity
        
        if tenacity_factor > higher_elo_player.elo:
            lower_elo_player.score += 1
        else:
            higher_elo_player.score += 1
    else:
        if player1.tenacity > player2.tenacity:
            player1.score += 1
        else:
            player2.score += 1
            
    if player1.is_boring and player2.is_boring and elo_diff <= 100:
        player1.score += 0.5
        player2.score += 0.5

# Create ChessPlayer instances
players = [
    ChessPlayer("Courage the Cowardly Dog", 25, 1000.39, 1000, False),
    ChessPlayer("Princess Peach", 23, 945.65, 50, True),
    ChessPlayer("Walter White", 50, 1650.73, 750, False),
    ChessPlayer("Rory Gilmore", 16, 1700.87, 500, False),
    ChessPlayer("Anthony Fantano", 37, 1400.45, 400, True),
    ChessPlayer("Beth Harmon", 20, 2500.34, 150, False)
]

# Simulate matches
for i in range(len(players)):
    for j in range(i+1, len(players)):
        for _ in range(2):
            simulateMatch(players[i], players[j])

# Print final results
print("Player\t\t\tScore")
print("==============================")
for player in players:
    print(f"{player.name}\t\t{player.score}")