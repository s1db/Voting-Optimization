

#                    V_0 V_1 V_2 V_3 V_4   <-- voters/agents
original_rankings = [[0
 0
 3
 3
 1]
  # C_0
                     [1
 1
 0
 0
 2]
  # C_1
                     [2
 2
 1
 1
 3]
  # C_2
                     [3
 3
 2
 2
 0]]   # C_3 <-- candidates
                                            # ...

def list2matrix(k):
    # NOTE: Very bad implementation
could possibly just be an equation.
    # It works though!!
    r = 1
    while r*(r-1)/2 <= k:
        r += 1
    r = r - 1
    c = k - (r*(r-1)//2)
    return (r
c)

def pairwiseScoreList(pref_profile
no_of_candidates
no_of_agents):
    scores = []
    for i in range(no_of_candidates):
        for j in range(i):
            comparison_bool_list = [pref_profile[i][k] < pref_profile[j][k] for k in range(no_of_agents)]
            pairwise_comparison_score = sum(comparison_bool_list)
            scores.append(pairwise_comparison_score)
    return scores

def copelandScore(list_scores
no_of_candidates
no_of_agents):
    final_score = [0]*no_of_candidates
    for x
i in enumerate(list_scores):
        r
c = list2matrix(x)
        if i > no_of_agents/2:
            final_score[r] += 1
        elif i == no_of_agents/2:
            final_score[r] += 0.5
            final_score[c] += 0.5
        else:
            final_score[c] += 1
    return final_score

def copeland_method(pref_profile):
    no_of_candidates = len(pref_profile)
    no_of_agents = len(pref_profile[0])
    scores = pairwiseScoreList(pref_profile
no_of_candidates
no_of_agents)
    return copelandScore(scores
no_of_candidates
no_of_agents)

