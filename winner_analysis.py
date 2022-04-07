import numpy as np
from collections import Counter


def load_files():
    files = [f"{i}_ranks_similar_1.csv" for i in range(235, 247)]
    ballots = []
    for file in files:
        ballot = np.genfromtxt(file, delimiter=",")[:,:-1]
        ballots.append(ballot)
    ballots = np.vstack(ballots)
    return ballots

if __name__ == "__main__":
    ballots = load_files()
    print(ballots.shape)
    for i in range(8):
        print(Counter(ballots[i,:]))
    # print(Counter(ballots[152,:]), sum(ballots[152,:]))
    # print(Counter(ballots[119,:]))
    # print(Counter(ballots[121,:]))
    # print(Counter(ballots[122,:]))
    # for i in [1528, 1540, 1545, 1546, 1622, 1623, 1626, 1627, 1632, 1633, 1634, 1635]:
    #     print(Counter(ballots[i,:]))
    # [print(Counter(ballots[i,:])) for i in range(0,250)]
    # print(Counter(ballots[94,:]))
    # print(Counter(ballots[221,:]))
    # print(Counter(ballots[339,:]))