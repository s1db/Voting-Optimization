from minizinc import Instance, Model, Solver
import asyncio

import numpy as np

or_tools = Solver.lookup("or-tools")
project_allocation = Model("./models/project_assignment_core.mzn")
instance = Instance(or_tools, project_allocation)
instance.add_file("./models/datafiles/socs_2015.dzn")

def all_sol(model, data, utility_sum_constraint):
    utilities = []
    allocations = []
    ranks = []
    instance = Instance(or_tools, project_allocation)
    instance.add_string(f"constraint allocation_sum={utility_sum_constraint};")
    instance.add_string("constraint forall(i in studentRanksProjectAt )(i !=5 /\ i !=6);")
    instance.add_file(data)
    result = True
    while result != None:
        with instance.branch() as opt:
            result = opt.solve()
            try:
                # print(result, "\n -----------------")
                allocation = result["studentToProject"]
                allocations.append(allocation)
                rank = result["studentRanksProjectAt"]
                ranks.append(rank)
                utils = result["util_per_agent"]
                utilities.append(utils)
            except:
                break
        
        instance.add_string(f"constraint studentToProject!={allocation};\n")
        # print(sum(allocation))
    return allocations, utilities, ranks
# allocations, utilities = all_sol(project_allocation, "./models/datafiles/socs_2015.dzn", 148)
# [print(allocation) for allocation in allocations]
# [print(utility) for utility in utilities]

final_allocations = []
final_utilities = []
final_ranks = []
contrained_utilities = range(148, 155)
for i in contrained_utilities:
    allocations, utilities, ranks = all_sol(project_allocation, "./models/datafiles/socs_2015.dzn", i)
    final_allocations.append(allocations)
    final_utilities.append(utilities)
    final_ranks.append(ranks)
    print(i, len(allocations), len(utilities), len(ranks), len(allocations[0]), len(utilities[0]), len(ranks[0]))
print(len(final_utilities))
print(len(final_allocations))

final_allocations = np.asarray(final_allocations)
np.savetxt("final_allocations_wo_56.csv", final_allocations, delimiter=",")
final_utilities = np.asarray(final_utilities)
np.savetxt("final_utilities_wo_56.csv", final_utilities, delimiter=",")
final_ranks = np.asarray(final_ranks)
np.savetxt("final_ranks_wo_56.csv", final_ranks, delimiter=",")