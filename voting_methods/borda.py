import numpy as np

def Borda(preference_profiles, candidates, voters):
    scores = preference_profiles.sum(axis=1)
    winning_index = borda_set(scores)
    return winning_index

def borda_set(scores):
    max_score = max(scores)
    max_indices = [i for i, x in enumerate(scores) if x == max_score]
    return max_indices
