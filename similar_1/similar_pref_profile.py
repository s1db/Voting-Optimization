import random
SEED = 42
random.seed(SEED)
import numpy as np

students = 100
projects = 100
supervisors = 100
student_project_ranks = []
for i in range(0,20):
    for _ in range(5):
        pref = list(range(i*5+1,((i+1)*5)+1))
        p = i
        while p == i:
            p = random.randint(0,19) 
        other_project_class = list(range(p*5+1,((p+1)*5)+1)) 
        random_proj = random.sample(other_project_class, 3)
        for k in random_proj:
            if k not in pref:
                pref.insert(random.randint(0, len(pref)), k)
        student_project_ranks.append(pref)

max_capacity = [1]*supervisors
project_supervised_by = range(1,supervisors+1)

mzn_pref_array = []

for student in student_project_ranks:
    all_proj = [projects]*projects
    for rank, proj in enumerate(student):
        all_proj[proj-1] = rank+1
    mzn_pref_array.append(all_proj)
a = np.array(mzn_pref_array)
np.savetxt(f'similar_1_{SEED}.txt', a, fmt="%s", delimiter=", ")



file = open(f'similar_pref_profile_jar.txt',"w")
file.write(f"{students}\n")
file.write(f"{projects}\n")
file.write(f"{supervisors}\n")

for i in range(1, students+1):
    file.write(f"s{i:03} s{i:03}\n")
for line in student_project_ranks:
    file.write(" ".join(str(x) for x in line) + "\n")
for i in range(1, projects+1):
    file.write(f"{i}\n")
for i in range(1, projects+1):
    file.write(f"p{i:03} p{i:03}\n")
for i in range(1, projects+1):
    file.write(f"1\n")
for i in range(1, supervisors+1):
    file.write(f"l{i:03}\n")
for i in max_capacity:
    file.write(f"{i}\n")
for i in project_supervised_by:
    file.write(f"l{i:03}\n")