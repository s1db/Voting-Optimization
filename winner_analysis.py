import numpy as np
import voting_methods.schulze as s
from collections import Counter


def load_files():
    files = ["450_ranks_wo_56.csv", "451_ranks_wo_56.csv", "452_ranks_wo_56.csv", "453_ranks_wo_56.csv", "454_ranks_wo_56.csv", "455_ranks_wo_56.csv", "456_ranks_wo_56.csv", "457_ranks_wo_56.csv", "458_ranks_wo_56.csv", "459_ranks_wo_56.csv", "460_ranks_wo_56.csv"]
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
    # for i in [1528, 1540, 1545, 1546, 1622, 1623, 1626, 1627, 1632, 1633, 1634, 1635]:
    #     print(Counter(ballots[i,:]))
    # [print(Counter(ballots[i,:])) for i in range(0,250)]
    print(Counter(ballots[155,:]))
    print(Counter(ballots[221,:]))
    print(Counter(ballots[339,:]))