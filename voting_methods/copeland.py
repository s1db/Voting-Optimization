import numpy as np

def Copeland(utility_profile, candidates, voters):
    scores = pairwise_scores(utility_profile, candidates)
    final_score = copeland_score(scores, candidates)
    index_positions = copeland_set(final_score)
    print(final_score)
    print(index_positions)
    print(final_score[index_positions[0]])
    return index_positions

def copeland_set(scores):
    max_score = max(scores)
    max_indices = [i for i, x in enumerate(scores) if x == max_score]
    return max_indices


def pairwise_scores(ballot, candidates):
    pairwise_scores = np.zeros((candidates, candidates))
    for i in range(candidates):
        for j in range(candidates):
            if i != j:
                pairwise_scores[i,j] = sum(ballot[i, :] > ballot[j, :])
    return pairwise_scores

def copeland_score(pairwise_scores, candidates):
    scores = np.zeros(candidates)
    for i in range(candidates):
        for j in range(candidates):
            if i != j:
                if pairwise_scores[i,j] > pairwise_scores[j,i]:
                    scores[i] += 1
                elif pairwise_scores[i,j] == pairwise_scores[j,i]:
                    scores[i] += 0.5
    return scores

def copeland_score2(pairwise_scores, candidates):
    scores = np.zeros((candidates,candidates))
    for i in range(candidates):
        for j in range(candidates):
            if i != j:
                if pairwise_scores[i,j] > pairwise_scores[j,i]:
                    scores[i,j] += 1
                elif pairwise_scores[i,j] == pairwise_scores[j,i]:
                    scores[i,j] += 0.5
    return scores


ballot_2 = [
    [2,2,2,2,2,2,2, 1,1,1,1, 2,2,2, 1,1,1,1,1], # B
    [4,4,4,4,4,4,4, 3,3,3,3, 1,1,1, 3,3,3,3,3], # M
    [3,3,3,3,3,3,3, 2,2,2,2, 4,4,4, 2,2,2,2,2], # S
    [1,1,1,1,1,1,1, 4,4,4,4, 3,3,3, 4,4,4,4,4], # T
]
# Winner: T with Schulze
# ballot_2 = np.array(ballot_2)
# candidates_2 = int(ballot_2.shape[0])
# voters_2 = ballot_2.shape[1]
# print(pairwise_scores(ballot_2, candidates_2))
# print(copeland_score(pairwise_scores(ballot_2, candidates_2), candidates_2))