import numpy as np
import voting_methods.schulze as s
from collections import Counter


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
    # print(Counter(ballots[0,:]))
    # print(Counter(ballots[1,:]))
    # print(Counter(ballots[119,:]))
    # print(Counter(ballots[121,:]))
    # print(Counter(ballots[122,:]))
    for i in [1528, 1540, 1545, 1546, 1622, 1623, 1626, 1627, 1632, 1633, 1634, 1635]:
        print(Counter(ballots[i,:]))