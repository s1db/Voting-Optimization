import random
import numpy as np
from collections import Counter
# from scipy.stats import skewnorm
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

students = 100
projects = 250
supervisors = 50
student_project_ranks = []

for i in range(students):
    preference = random.sample(range(projects), 8)
    student_project_ranks.append(preference)

mzn_pref_array = []

for student in student_project_ranks:
    all_proj = [projects]*projects
    for rank, proj in enumerate(student):
        all_proj[proj] = rank+1
    mzn_pref_array.append(all_proj)
a = np.array(mzn_pref_array)
np.savetxt(f'random_instance_1_{SEED}.txt', a, fmt="%s", delimiter=", ")

print("n = ", students)
print("p = ", projects)
print("l = ", supervisors)
project_supervised_by = np.random.randint(1,supervisors+1,size=(projects,))
print("project_sup_by = ", list(project_supervised_by), ";")

max_capacity = [2,3]*(supervisors//2)
print("max_capacity = ", max_capacity, ";")

file = open(f'random_jar_{SEED}.txt',"w")
file.write(f"{students}\n")
file.write(f"{projects}\n")
file.write(f"{supervisors}\n")
for i in range(1, students+1):
    file.write(f"s{i:03} s{i:03}\n")
for line in student_project_ranks:
    file.write(" ".join(str(x+1) for x in line) + "\n")
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