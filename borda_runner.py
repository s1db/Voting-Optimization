import numpy as np
import voting_methods.borda as b

def load_files():
    files = ["148_utilities_wo_56.csv", "149_utilities_wo_56.csv"]
    ballots = []
    for file in files:
        ballot = np.loadtxt("data/"+file, delimiter=',')
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