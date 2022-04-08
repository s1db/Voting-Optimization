import numpy as np
from collections import Counter
from os import walk
from borda_runner import load_files

def load_files():
    a = input("Enter the name of instance: ")
    # files = [f"{i}_utilities_random_1.csv" for i in range(162, 170)]
    files = []
    mypath = a + "/data/"
    for (dirpath, dirnames, filenames) in walk(mypath):
        for filename in filenames:
            if "ranks" in filename:
                files.append(filename)
        break
    files = sorted(files)
    print("file names: ", files)
    ballots = []
    for file in files:
        ballot = np.genfromtxt(mypath + file, delimiter=",")[:,:-1]
        ballots.append(ballot)
    ballots = np.vstack(ballots)
    return a, ballots

if __name__ == "__main__":

    dir, ballots = load_files()
    i = input("Enter the solution ID: ")
    i = int(i)
    print(Counter(ballots[i,:]), ballots[i,:].sum())
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