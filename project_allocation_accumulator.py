from minizinc import Instance, Model, Solver
import asyncio

import numpy as np

or_tools = Solver.lookup("or-tools")
project_allocation = Model("./models/project_assignment.mzn")
instance = Instance(or_tools, project_allocation)
instance.add_file("./models/datafiles/socs_2015_new.dzn")

def all_sol(model, data, utility_sum_constraint):
    utilities = []
    allocations = []
    ranks = []
    instance = Instance(or_tools, model)
    instance.add_string(f"constraint allocation_sum={utility_sum_constraint};")
    instance.add_string("constraint forall(i in studentRanksProjectAt)(i !=5 /\ i !=6);")
    instance.add_file(data)
    result = True
    count = 0
    while result != None and count <=250:
        with instance.branch() as opt:
            result = opt.solve()
            # print(result)
            try:
                print(count)
                allocation = result["studentToProject"]
                # allocations.append(allocation)
                rank = result["studentRanksProjectAt"]
                # ranks.append(rank)
                utils = result["util_per_agent"]
                # utilities.append(utils)
            except:
                break
        with open(str(utility_sum_constraint)+"_allocations_wo_56.csv", "ab") as f:
            np.savetxt(f, allocation,fmt="%d", delimiter=",", newline=",")
            f.write(b"\n")
        with open(str(utility_sum_constraint)+"_ranks_wo_56.csv", "ab") as f:
            np.savetxt(f, rank,fmt="%d", delimiter=",", newline=",")
            f.write(b"\n")
        with open(str(utility_sum_constraint)+"_utilities_wo_56.csv", "ab") as f:
            np.savetxt(f, utils,fmt="%d", delimiter=",", newline=",")
            f.write(b"\n")
        instance.add_string(f"constraint studentToProject!={allocation};\n")
        count +=1
        # print(sum(allocation))
    return allocations, utilities, ranks
# allocations, utilities = all_sol(project_allocation, "./models/datafiles/socs_2015.dzn", 148)
# [print(allocation) for allocation in allocations]
# [print(utility) for utility in utilities]

# final_allocations = []
# final_utilities = []
# final_ranks = []
contrained_utilities = [139,140,141,142]
for i in contrained_utilities:
    allocations, utilities, ranks = all_sol(project_allocation, "./models/datafiles/socs_2015_new.dzn", i)
    # # final_allocations.append(allocations)
    # # final_utilities.append(utilities)
    # # final_ranks.append(ranks)
    # print(i, len(allocations), len(utilities), len(ranks))
    # final_allocations = np.asarray(allocations)
    # np.savetxt(str(i)+"_allocations_wo_56.csv", allocations,fmt="%s", delimiter=",")
    # final_utilities = np.asarray(utilities)
    # np.savetxt(str(i)+"_utilities_wo_56.csv", utilities,fmt="%s", delimiter=",")
    # final_ranks = np.asarray(ranks)
    # np.savetxt(str(i)+"_ranks_wo_56.csv", ranks,fmt="%s", delimiter=",")
# print(len(final_utilities))
# print(len(final_allocations))