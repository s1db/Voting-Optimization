from turtle import shape
import numpy as np

ballot_1 = [
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3,], # A
    [3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4,], # B
    [4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1,], # C
    [1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2,], # D
    [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 1, 1, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5,], # E
]
ballot_1 = np.array(ballot_1)
candidates_1 = ballot_1.shape[0]
voters_1 = ballot_1.shape[1]



ballot_2 = [
    [2,2,2,2,2,2,2, 1,1,1,1, 2,2,2, 1,1,1,1,1], # B
    [4,4,4,4,4,4,4, 3,3,3,3, 1,1,1, 3,3,3,3,3], # M
    [3,3,3,3,3,3,3, 2,2,2,2, 4,4,4, 2,2,2,2,2], # S
    [1,1,1,1,1,1,1, 4,4,4,4, 3,3,3, 4,4,4,4,4], # T
]

ballot_2 = np.array(ballot_2)
candidates_2 = ballot_2.shape[0]
voters_2 = ballot_2.shape[1]


ballot_3 = [
    [4,4,4, 3,3, 1,1, 1,1], # A
    [3,3,3, 2,2, 3,3, 3,3], # B
    [2,2,2, 1,1, 2,2, 4,4], # C
    [1,1,1, 4,4, 4,4, 2,2], # D
]
ballot_3 = np.array(ballot_3)
candidates_3 = ballot_3.shape[0]
voters_3 = ballot_3.shape[1]



def Schulze(ballot, candidates, voters):
    R,C = np.tril_indices(candidates,-1)
    entries = R.shape[0]
    pairwise_score = np.zeros((candidates, candidates))
    p = np.zeros((candidates, candidates))

    for r in range(entries):
        i = R[r]
        j = C[r]
        score = sum(ballot[i, :] > ballot[j, :])
        pairwise_score[i,j] = score
        pairwise_score[j,i] = voters - score

    # print(pairwise_score)

    for r in range(entries):
        i = R[r]
        j = C[r]
        if pairwise_score[i,j] > pairwise_score[j,i]:
            p[i,j] = pairwise_score[i,j]
        else:
            p[j,i] = pairwise_score[j,i]

    for i in range(candidates):
        for j in range(candidates):
            if i != j:
                for k in range(candidates):
                    if i != k and j != k:
                        p[j,k] = max (p[j,k], min (p[j,i], p[i,k]))
    # print(p)
    scores = schulze_scores(p, candidates)
    print("----------------")
    print(scores)
    print(schulze_set(scores))

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