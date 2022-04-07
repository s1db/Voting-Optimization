import numpy as np
import voting_methods.borda as b

def load_files():
    files = [f"{i}_utilities_random_1.csv" for i in range(162, 170)]
    ballots = []
    for file in files:
        ballot = np.genfromtxt(file, delimiter=",")[:,:-1]
        ballots.append(ballot)
    ballots = np.vstack(ballots)
    return ballots

if __name__ == "__main__":
    ballots = load_files()
    print(ballots.shape)
    candidates = ballots.shape[0]
    voters = ballots.shape[1]
    b_set = b.Borda(ballots, candidates, voters)
    print(b_set)
