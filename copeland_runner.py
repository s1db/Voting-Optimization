import numpy as np
import voting_methods.copeland as c

def load_files():
    files = ["134_utilities_wo_56.csv","135_utilities_wo_56.csv","136_utilities_wo_56.csv","137_utilities_wo_56.csv","138_utilities_wo_56.csv","139_utilities_wo_56.csv","140_utilities_wo_56.csv","141_utilities_wo_56.csv","142_utilities_wo_56.csv"]
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
