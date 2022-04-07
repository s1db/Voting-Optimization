import numpy as np
import voting_methods.schulze as s

def load_files():
    files = [f"{i}_utilities_2020.csv" for i in range(372, 385)]
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
