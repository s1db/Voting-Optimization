import numpy as np
import voting_methods.schulze as s
from borda_runner import load_files

if __name__ == "__main__":
    a, ballots = load_files()
    print("number of solutions and number of students: ", ballots.shape)
    candidates = ballots.shape[0]
    voters = ballots.shape[1]
    s_set = s.Schulze(a, ballots, candidates, voters)
    print("winning solution ids: ", s_set)