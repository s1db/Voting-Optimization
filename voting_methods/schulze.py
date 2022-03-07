from turtle import shape
import numpy as np

ballot_1 = [
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3,], # A
    [3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4,], # B
    [4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1,], # C
    [1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2,], # D
    [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5,], # E
]
# Winner: E
ballot_1 = np.array(ballot_1)
candidates_1 = ballot_1.shape[0]
voters_1 = ballot_1.shape[1]



ballot_2 = [
    [2,2,2,2,2,2,2, 1,1,1,1, 2,2,2, 1,1,1,1,1], # B
    [4,4,4,4,4,4,4, 3,3,3,3, 1,1,1, 3,3,3,3,3], # M
    [3,3,3,3,3,3,3, 2,2,2,2, 4,4,4, 2,2,2,2,2], # S
    [1,1,1,1,1,1,1, 4,4,4,4, 3,3,3, 4,4,4,4,4], # T
]
# Winner: T
ballot_2 = np.array(ballot_2)
candidates_2 = ballot_2.shape[0]
voters_2 = ballot_2.shape[1]


ballot_3 = [
    [4,4,4, 3,3, 1,1, 1,1], # A
    [3,3,3, 2,2, 3,3, 3,3], # B
    [2,2,2, 1,1, 2,2, 4,4], # C
    [1,1,1, 4,4, 4,4, 2,2], # D
]
# Winner: B, D
ballot_3 = np.array(ballot_3)
candidates_3 = ballot_3.shape[0]
voters_3 = ballot_3.shape[1]



def Schulze(ballot, candidates, voters):
    d = pairwise_scores(ballot, candidates)
    p = widest_path(d, candidates)

    scores = schulze_scores(p, candidates)
    winners_index = schulze_set(scores)
    print(scores)
    print(winners_index)
    print(scores[winners_index[0]])
    print("--------------------------------")
    return winners_index

def widest_path(d, candidates):
    p = np.zeros((candidates, candidates))
    for i in range(candidates):
        for j in range(candidates):
            if i != j:
                if d[i,j] > d[j,i]:
                    p[i,j] = d[i,j]
                else:
                    p[i,j] = 0
    for i in range(candidates):
        for j in range(candidates):
            if i != j:
                for k in range(candidates):
                    if i != k and j != k:
                        p[j,k] = max(p[j,k], min(p[j,i], p[i,k]))
    return p

def pairwise_scores(ballot, candidates):
    pairwise_scores = np.zeros((candidates, candidates))
    for i in range(candidates):
        for j in range(candidates):
            if i != j:
                pairwise_scores[i,j] = sum(ballot[i, :] > ballot[j, :])
    return pairwise_scores

def schulze_scores(p, candidates):
    scores = np.zeros(candidates)
    for i in range(candidates):
        for j in range(candidates):
            if i != j:
                if p[i,j] >= p[j,i]:
                    scores[i] += 1
    return scores

def schulze_set(scores):
    max_score = max(scores)
    max_indices = [i for i, x in enumerate(scores) if x == max_score]
    return max_indices

# Schulze(ballot_3, candidates_3, voters_3)

def main():
    Schulze(ballot_1, candidates_1, voters_1)
    Schulze(ballot_2, candidates_2, voters_2)
    Schulze(ballot_3, candidates_3, voters_3)

if __name__ == "__main__":
    main()