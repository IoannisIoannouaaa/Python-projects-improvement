def main():
    difficulty = input('Difficult or casual?').strip().lower()
    players = input('Multiplayer or single-player?').strip().lower()
    
    if difficulty == 'difficult':
        if players == 