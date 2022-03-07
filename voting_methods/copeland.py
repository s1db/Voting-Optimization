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
                elif pairwise_scores[i,j] < pairwise_scores[j,i]:
                    scores[j] += 1
                else:
                    scores[i] += 0.5
                    scores[j] += 0.5
    return scores