import numpy as np
import voting_methods.schulze as s
from collections import Counter


def load_files():
    files = ["148_utilities_wo_56.csv", "149_utilities_wo_56.csv", "150_utilities_wo_56.csv"]
    ballots = []
    for file in files:
        ballot = np.loadtxt("data/"+file, delimiter=',')
        ballots.append(ballot)
    ballots = np.vstack(ballots)
    return ballots

if __name__ == "__main__":
    ballots = load_files()
    print(Counter(141 - ballots[7,:]))
    print(Counter(141 - ballots[2597,:]))