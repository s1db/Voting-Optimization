from itertools import permutations
import voting_methods.copeland as copeland
num_roommates = 4
num_rooms = num_roommates//2

roommates_set = [i for i in range(num_roommates)]
preferences = [
    [3,1,2],
    [2,0,3],
    [1,0,3],
    [0,1,2]
]
valid_pairings = list(permutations(roommates_set))
# [print(pair) for pair in valid_pairings]

pairs = []
utility_of_pairing = []

for i in valid_pairings:
    a = i[:num_rooms]
    b = i[num_rooms:]
    pairs.append([a,b])
    utility = [0]*num_roommates
    for j in range(num_rooms):
        utility[a[j]] += (num_roommates - 1) - preferences[a[j]].index(b[j])
        utility[b[j]] += (num_roommates - 1) - preferences[b[j]].index(a[j])
    utility_of_pairing.append(utility)

max_sum_val = 0
max_sum_pos = 0
winners = []

# borda
for i,x in enumerate(utility_of_pairing):
    a = sum(x)
    if a == max_sum_val:
        winners.append(i)
    if a > max_sum_val:
        max_sum_val = a
        max_sum_pos = i
        winners = []
        winners.append(i)
print("borda:")
print("    ",max_sum_val)
print("    ",winners)
print("    ",utility_of_pairing[winners[0]])
print("    ",pairs[max_sum_pos])


print("-----🌟-----")
print(utility_of_pairing)
copeland_score = copeland.copeland_method(utility_of_pairing)
for i,x in enumerate(copeland_score):
    print("    ",i,x)
print("-----🌟-----")
