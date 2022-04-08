import numpy as np
from os import walk
import voting_methods.borda as b

def load_files():
    a = input("Enter the name of instance: ")
    # files = [f"{i}_utilities_random_1.csv" for i in range(162, 170)]
    files = []
    mypath = a + "/data/"
    for (dirpath, dirnames, filenames) in walk(mypath):
        for filename in filenames:
            if "utilities" in filename:
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
    a, ballots = load_files()
    print("number of solutions and number of students: ", ballots.shape)
    candidates = ballots.shape[0]
    voters = ballots.shape[1]
    b_set = b.Borda(ballots, candidates, voters)
    print("winning solution ids: ", b_set)
