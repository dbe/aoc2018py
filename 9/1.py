from collections import deque

def run(lines):
    games = [
        (9, 25),
        (10, 1618),
        (13, 7999),
        (17, 1104),
        (21, 6111),
        (30, 5807),
        (403, 71920)
    ]

    for game in games:
        score = play_game(game[0], game[1])
        print(f"For game with {game[0]} players ending on marble {game[1]} the best score is {score}")

    return play_game(403, 71920)

def play_game(players, last_marble):
    scores = [0] * players
    circle = deque([0])

    for turn in range(1, last_marble + 1):
        score = play(circle, turn)
        scores[(turn - 1) % players] += score

    return max(scores)


def play(circle, turn):
    if(turn % 23 == 0):
        score = turn

        circle.rotate(7)
        score += circle.popleft()

        return score
    else:
        circle.rotate(-2)
        circle.appendleft(turn)

        return 0
