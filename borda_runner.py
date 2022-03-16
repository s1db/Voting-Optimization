import numpy as np
import voting_methods.borda as b

def load_files():
    files = ["450_utilities_wo_56.csv", "451_utilities_wo_56.csv", "452_utilities_wo_56.csv", "453_utilities_wo_56.csv", "454_utilities_wo_56.csv", "455_utilities_wo_56.csv"]
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
