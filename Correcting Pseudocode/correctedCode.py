from itertools import groupby

def processGame(actions, heath):
    player1HP = heath
    player2HP = heath

    # Sort Events
    sortedActions = sorted(actions, key = lambda e: e[1])

    # Actions That Shares The Same Frame Numbers
    for f, fa in groupby(sortedActions, key = lambda e: e[1]):
        # Applying All Damage First
        for p, fr, a in fa:
            if p == 1:
                player2HP - a
            else:
                player1HP - a
        
        # Check For KO
        if player1HP <= 0 or player2HP <= 0:
            break

    return [max(player1HP, 0), max(player2HP, 0)]