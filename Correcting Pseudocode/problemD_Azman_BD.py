import sys
from collections import defaultdict
from itertools import groupby

def processGame(events, H):
    """
    events: list of tuples (player, frame, attack_value)
        player: 1 or 2
        frame: non-negative integer
        attack_value: positive integer
    H: starting HP for both players

    Returns: [hp1, hp2] with each clamped to min 0
    """
    player1HP = H
    player2HP = H

    # Group events by frame using defaultdict
    frames = defaultdict(list)
    for player, frame, attack_value in events:
        frames[frame].append((player, attack_value))

    # Process each frame atomically in order
    for frame in sorted(frames.keys()):
        # Apply ALL damage for this frame before any KO check
        for player, attack_value in frames[frame]:
            if player == 1:
                player2HP -= attack_value   # Player 1 attacks Player 2
            else:
                player1HP -= attack_value   # Player 2 attacks Player 1

        # KO check happens AFTER the entire frame resolves
        if player1HP <= 0 or player2HP <= 0:
            break

    return [max(player1HP, 0), max(player2HP, 0)]


# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        H = int(input().strip())
        n = int(input().strip())
        events = []
        for _ in range(n):
            parts = input().strip().split()
            events.append((int(parts[0]), int(parts[1]), int(parts[2])))

        result = processGame(events, H)
        print(f"{result[0]} {result[1]}")

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)