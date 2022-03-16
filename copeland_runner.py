import numpy as np
import voting_methods.copeland as c

def load_files():
    files = ["450_utilities_wo_56.csv", "451_utilities_wo_56.csv", "452_utilities_wo_56.csv", "453_utilities_wo_56.csv", "454_utilities_wo_56.csv", "455_utilities_wo_56.csv", "456_utilities_wo_56.csv", "457_utilities_wo_56.csv", "458_utilities_wo_56.csv", "459_utilities_wo_56.csv", "460_utilities_wo_56.csv"]
    ballots = []
    for file in files:
        # ballot = np.genfromtxt("data/"+file, delimiter=",")[:,:-1]
        ballot = np.genfromtxt(file, delimiter=",")[:,:-1]
        print(ballot.shape)
        ballots.append(ballot)
    ballots = np.vstack(ballots)
    return ballots

if __name__ == "__main__":
    ballots = load_files()
    print(ballots.shape)
    candidates = ballots.shape[0]
    voters = ballots.shape[1]
    s_set = c.Copeland(ballots, candidates, voters)
    print(s_set)
    print(len(s_set))
