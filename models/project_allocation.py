import numpy as np

projects_without_index = [4708, 4709, 4710, 4711, 4712, 4465, 4484, 4486, 4487, 4671, 4675, 4607, 4604, 4597, 4549, 4554, 4543, 4544, 4685, 4458, 4459, 4698, 4699, 4700, 4701, 4702, 4438, 4413, 4527, 4528, 4566, 4617, 4618, 4601, 4434, 4435, 4436, 4437, 4449, 4450, 4687, 4688, 4689, 4690, 4703, 4704, 4705, 4706, 4431, 4426, 4427, 4428, 4394, 4395, 4396, 4397, 4398, 4399, 4672, 4673, 4674, 4676, 4722, 4588, 4589, 4662, 4643, 4644, 4646, 4647, 4648, 4653, 4654, 4655, 4659, 4660, 4661, 4550, 4545, 4546, 4547, 4548, 4511, 4430, 4507, 4508, 4632, 4634, 4670, 4696, 4697, 4656, 4649, 4650, 4651, 4652, 4667, 4668, 4669, 4608, 4609, 4610, 4605, 4606, 4720, 4663, 4664, 4414, 4415, 4416, 4445, 4539, 4623, 4587, 4590, 4592, 4593, 4645, 4635, 4625, 4626, 4627, 4628, 4629, 4571, 4572, 4573, 4600, 4683, 4515, 4516, 4517, 4518, 4410, 4509, 4510, 4461, 4567, 4613, 4429, 4540, 4541, 4542, 4538, 4658, 4665, 4666, 4611, 4612, 4512, 4513, 4514, 4526, 4520, 4521, 4522, 4574, 4575, 4594, 4595, 4684, 4680, 4682, 4565, 4523, 4524, 4525, 4439, 4440, 4441, 4442, 4443, 4568, 4569, 4624, 4619, 4620, 4621, 4622, 4468, 4585, 4586, 4657, 4631, 4633, 4707, 4723, 4532, 4533, 4534, 4535, 4536, 4537, 4467]
project_supervisors_map = ["Alice Miller", "Alice Miller", "Alice Miller", "Alice Miller", "Alice Miller", "Alvis Fong", "Christos Anagnostopoulos", "Christos Anagnostopoulos", "Christos Anagnostopoulos", "Baharak Rastegari", "Catherine Higham", "Craig Macdonald", "Craig Macdonald", "Colin Perkins", "Colin Perkins", "Colin Perkins", "Colin Perkins", "Colin Perkins", "Colin Perkins", "David F Manlove", "David F Manlove", "Dimitrios Pezaros", "Dimitrios Pezaros", "Dimitrios Pezaros", "Dimitrios Pezaros", "Dimitrios Pezaros", "Gethin Norman", "Gethin Norman", "Gethin Norman", "Gethin Norman", "Gethin Norman", "Gethin Norman", "Gethin Norman", "Helen C Purchase", "Helen C Purchase", "Helen C Purchase", "Helen C Purchase", "Helen C Purchase", "Inah Omoronyia", "Inah Omoronyia", "Inah Omoronyia", "Inah Omoronyia", "Inah Omoronyia", "Inah Omoronyia", "Joemon Jose", "Joemon Jose", "Joemon Jose", "Joemon Jose", "Joemon Jose", "Joemon Jose", "Joemon Jose", "Joemon Jose", "Chris Johnson", "Chris Johnson", "Chris Johnson", "Chris Johnson", "Chris Johnson", "Chris Johnson", "Joe Maguire", "Joe Maguire", "Joe Maguire", "Joe Maguire", "Joe Maguire", "John Rooksby", "John Rooksby", "Jeremy Singer", "John T O'Donnell", "John T O'Donnell", "John T O'Donnell", "John T O'Donnell", "John T O'Donnell", "John T O'Donnell", "Julie Williamson", "Julie Williamson", "Julie Williamson", "Julie Williamson", "Julie Williamson", "Leif Azzopardi", "Leif Azzopardi", "Leif Azzopardi", "Leif Azzopardi", "Leif Azzopardi", "Lewis M Mackenzie", "Lewis M Mackenzie", "Lewis M Mackenzie", "Lewis M Mackenzie", "Mary Ellen Foster", "Mary Ellen Foster", "Alistair Morrison", "Natalia Chechina", "Natalia Chechina", "Nikos Ntarmos", "Nikos Ntarmos", "Nikos Ntarmos", "Nikos Ntarmos", "Nikos Ntarmos", "Nikos Ntarmos", "Nikos Ntarmos", "Nikos Ntarmos", "Iadh Ounis", "Iadh Ounis", "Iadh Ounis", "Iadh Ounis", "Iadh Ounis", "Iadh Ounis", "Parvin Asadzadeh Birjandi", "Parvin Asadzadeh Birjandi", "Patrick Prosser", "Patrick Prosser", "Patrick Prosser", "Patrick Prosser", "Patrick Prosser", "Peter Triantafillou", "Peter Triantafillou", "Peter Triantafillou", "Peter Triantafillou", "Peter Triantafillou", "Patrick Maier", "Patrick Maier", "Quintin I Cutts", "Quintin I Cutts", "Quintin I Cutts", "Quintin I Cutts", "Quintin I Cutts", "Roderick Murray-Smith", "Roderick Murray-Smith", "Roderick Murray-Smith", "Roderick Murray-Smith", "Roderick Murray-Smith", "Ron Poet", "Ron Poet", "Ron Poet", "Ron Poet", "Rosanne English", "Rosanne English", "Rosanne English", "Rosanne English", "Rosanne English", "Mattias Rost", "Mattias Rost", "Simon J Gay", "Simon J Gay", "Simon J Gay", "Simon J Gay", "Simon J Gay", "Simon J Gay", "Simon J Gay", "Simon Rogers", "Simon Rogers", "Simon Rogers", "Simon Rogers", "Simon Rogers", "Stephen Brewster", "Stephen Brewster", "Stephen Brewster", "Stephen Brewster", "Stephen Brewster", "Stephen Brewster", "Stephen Brewster", "Stephen Brewster", "Stephen Brewster", "Stephen Brewster", "Stephen Brewster", "Phil Trinder", "Phil Trinder", "Phil Trinder", "Phil Trinder", "Tim Storer", "Tim Storer", "Tim Storer", "Tim Storer", "Tim Storer", "Tim Storer", "Tim Storer", "Alessandro Vinciarelli", "Alessandro Vinciarelli", "Alessandro Vinciarelli", "Alessandro Vinciarelli", "Alessandro Vinciarelli", "Zhengkui Wang", "David White", "David White", "David White", "Wim Vanderbauwhede", "Wim Vanderbauwhede", "Wim Vanderbauwhede", "Wim Vanderbauwhede", "W Paul Cockshott", "W Paul Cockshott", "W Paul Cockshott", "W Paul Cockshott", "W Paul Cockshott", "W Paul Cockshott", "Jianxin Zheng"]
assert len(projects_without_index) == len(project_supervisors_map)
project_supervisor_zip = zip(projects_without_index, project_supervisors_map)

supervisors = ["Christos Anagnostopoulos","Parvin Asadzadeh Birjandi","Leif Azzopardi","Stephen Brewster","Natalia Chechina","W Paul Cockshott","Quintin I Cutts","Rosanne English","Alvis Fong","Mary Ellen Foster","Simon J Gay","Catherine Higham","Chris Johnson","Joemon Jose","Craig Macdonald","Lewis M Mackenzie","Joe Maguire","Patrick Maier","David F Manlove","Alice Miller","Alistair Morrison","Roderick Murray-Smith","Gethin Norman","Nikos Ntarmos","John T O'Donnell","Inah Omoronyia","Iadh Ounis","Colin Perkins","Dimitrios Pezaros","Ron Poet","Patrick Prosser","Helen C Purchase","Baharak Rastegari","Simon Rogers","John Rooksby","Mattias Rost","Jeremy Singer","Tim Storer","Peter Triantafillou","Phil Trinder","Wim Vanderbauwhede","Alessandro Vinciarelli","Zhengkui Wang","David White","Julie Williamson","Jianxin Zheng"]
lecturerMax = [2, 3, 4, 4, 2, 4, 4, 2, 9, 2, 2, 2, 4, 0, 3, 3, 3, 2, 2, 4, 4, 3, 4, 4, 4, 3, 4, 3, 4, 4, 4, 4, 3, 2, 3, 1, 4, 1, 4, 2, 4, 4, 3, 3, 3, 3]
assert len(supervisors) == len(lecturerMax)
supervisor_max_zip = zip(supervisors, lecturerMax)

studentProjectRanks = [
    [4594, 4566, 4660, 4654, 4510, 4569], 
    [4592, 4513, 4618, 4539, 4566, 4631], 
    [4664, 4435, 4507, 4660, 4520, 4676], 
    [4670, 4508, 4507, 4606, 4573, 4520], 
    [4663, 4606, 4612, 4704, 4626, 4550], 
    [4626, 4625, 4654, 4660, 4435, 4574], 
    [4571, 4706, 4604, 4548, 4550, 4601], 
    [4722, 4672, 4520, 4594, 4625, 4627], 
    [4662, 4459, 4589, 4670, 4520, 4685], 
    [4670, 4672, 4532, 4435, 4567, 4629], 
    [4632, 4622, 4434, 4437, 4684, 4624], 
    [4680, 4547, 4521, 4573, 4661, 4572], 
    [4626, 4628, 4550, 4508, 4612, 4663], 
    [4660, 4622, 4619, 4673, 4676, 4435], 
    [4612, 4663, 4458, 4610, 4605, 4395], 
    [4550, 4568, 4690, 4569, 4607, 4605], 
    [4589, 4573, 4511, 4610, 4664, 4526], 
    [4610, 4589, 4625, 4586, 4664, 4609], 
    [4515, 4434, 4626, 4661, 4522, 4548], 
    [4625, 4706, 4606, 4573, 4704, 4629], 
    [4396, 4618, 4684, 4436, 4595, 4704], 
    [4510, 4670, 4608, 4508, 4664, 4606], 
    [4607, 4662, 4700, 4589, 4646, 4595], 
    [4607, 4610, 4664, 4656, 4624, 4541], 
    [4521, 4435, 4394, 4703, 4594, 4722], 
    [4670, 4664, 4571, 4543, 4685, 4566], 
    [4680, 4513, 4514, 4595, 4604, 4609], 
    [4547, 4487, 4589, 4571, 4609, 4511], 
    [4535, 4513, 4698, 4532, 4605, 4515], 
    [4626, 4574, 4518, 4672, 4670, 4705], 
    [4518, 4513, 4631, 4532, 4395, 4663], 
    [4507, 4574, 4585, 4508, 4684, 4610], 
    [4670, 4664, 4526, 4517, 4415, 4610], 
    [4703, 4606, 4573, 4604, 4550, 4610], 
    [4548, 4521, 4703, 4508, 4704, 4594], 
    [4510, 4435, 4670, 4703, 4588, 4654], 
    [4625, 4612, 4670, 4507, 4589, 4689], 
    [4670, 4508, 4549, 4699, 4522, 4484], 
    [4622, 4627, 4612, 4688, 4514, 4619], 
    [4652, 4722, 4565, 4571, 4661, 4631], 
    [4524, 4654, 4517, 4662, 4682, 4722], 
    [4609, 4607, 4487, 4589, 4703, 4547], 
    [4539, 4646, 4538, 4644, 4571, 4666], 
    [4526, 4511, 4572, 4397, 4437, 4685], 
    [4518, 4670, 4508, 4514, 4625, 4511], 
    [4508, 4507, 4664, 4594, 4670, 4588], 
    [4589, 4699, 4712, 4445, 4631, 4619], 
    [4612, 4521, 4573, 4664, 4663, 4566], 
    [4508, 4507, 4595, 4520, 4625, 4612], 
    [4660, 4437, 4621, 4722, 4674, 4435], 
    [4450, 4690, 4568, 4410, 4517, 4543], 
    [4521, 4670, 4545, 4573, 4567, 4395], 
    [4606, 4443, 4547, 4604, 4513, 4607], 
    [4670, 4526, 4672, 4594, 4654, 4517], 
    [4589, 4547, 4683, 4618, 4522, 4703], 
    [4487, 4589, 4700, 4554, 4398, 4606], 
    [4395, 4589, 4569, 4573, 4410, 4545], 
    [4535, 4675, 4589, 4573, 4534, 4622], 
    [4398, 4515, 4662, 4690, 4701, 4534], 
    [4508, 4680, 4606, 4609, 4706, 4589], 
    [4703, 4594, 4526, 4670, 4511, 4612], 
    [4672, 4567, 4670, 4511, 4416, 4435], 
    [4672, 4605, 4625, 4549, 4520, 4722], 
    [4397, 4606, 4610, 4607, 4526, 4652], 
    [4707, 4397, 4522, 4631, 4712, 4701], 
    [4513, 4623, 4514, 4547, 4682, 4571], 
    [4690, 4450, 4394, 4397, 4515, 4706], 
    [4632, 4586, 4459, 4526, 4625, 4414], 
    [4513, 4709, 4619, 4514, 4708, 4631], 
    [4589, 4539, 4416, 4538, 4664, 4567], 
    [4680, 4521, 4660, 4507, 4511, 4664], 
    [4619, 4620, 4569, 4625, 4632, 4644], 
    [4646, 4688, 4567, 4410, 4517, 4436], 
    [4606, 4609, 4586, 4664, 4508, 4670], 
    [4670, 4618, 4622, 4660, 4663, 4521], 
    [4571, 4535, 4708, 4513, 4438, 4662],
]

for proj in projects_without_index:
    inRanked = False
    for student in studentProjectRanks:
        if proj in student:
            inRanked = True
            break
    if inRanked == False:
        project_supervisor_zip = [(i,j) for i,j in project_supervisor_zip if i != proj]

projects, project2supervisor = zip(*project_supervisor_zip)
projects = list(projects)
project2supervisor = list(project2supervisor)

key_projects = {k:v for v, k in enumerate(projects)}

supervisor_key = [project2supervisor.count(v) for v in set(project2supervisor)]


num_projects = len(projects)
student_project_rank = []
for student in studentProjectRanks:
    all_proj = [num_projects]*num_projects
    for rank, proj in enumerate(student):
        key = key_projects[proj]
        all_proj[key] = rank+1
    student_project_rank.append(all_proj)
a = np.array(student_project_rank)

np.savetxt('test.txt', a, fmt="%s", delimiter=", ")

supervisors_list = []
for i, x in enumerate(supervisor_key):
    supervisors_list.extend([i+1]*x)
print(len(supervisor_key))
print(supervisors_list)

supervisor_max_zip = [(i,j) for i,j in zip(supervisors, lecturerMax) if i in set(project2supervisor)]
new_sup_max = [j for i,j in supervisor_max_zip]
print(new_sup_max)
print(len(new_sup_max))
# print(lecturerMax)




'''





'''