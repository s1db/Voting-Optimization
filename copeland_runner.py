import numpy as np
import voting_methods.copeland as c

def load_files():
    files = [f"{i}_utilities_similar_1.csv" for i in range(235,248)]
    ballots = []
    for file in files:
        # ballot = np.genfromtxt("data/"+file, delimiter=",")[:,:-1]
        ballot = np.genfromtxt(file, delimiter=",")[:,:-1]
        ballots.append(ballot)
    ballots = np.vstack(ballots)
    print(ballots.shape)
    return ballots

if __name__ == "__main__":
    ballots = load_files()
    print(ballots.shape)
    candidates = ballots.shape[0]
    voters = ballots.shape[1]
    s_set = c.Copeland(ballots, candidates, voters)
    print(s_set)
    print(len(s_set))
