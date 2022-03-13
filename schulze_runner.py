import numpy as np
import voting_methods.schulze as s

def load_files():
    files = ["134_ranks_wo_56.csv","135_ranks_wo_56.csv","136_ranks_wo_56.csv","137_ranks_wo_56.csv","138_ranks_wo_56.csv","139_ranks_wo_56.csv","140_ranks_wo_56.csv","141_ranks_wo_56.csv","142_ranks_wo_56.csv"]
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
    s_set = s.Schulze(ballots, candidates, voters)
    print(s_set)
    print(len(s_set))
