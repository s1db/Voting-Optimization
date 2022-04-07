from minizinc import Instance, Model, Solver

import numpy as np

or_tools = Solver.lookup("gurobi")
project_allocation = Model("./models/count_constraints_spa.mzn")


def all_sol(model, data_file, utility_sum_constraint):
    utilities = []
    allocations = []
    ranks = []
    counts = []
    instance = Instance(or_tools, model)
    instance.add_string(f"constraint allocation_sum={utility_sum_constraint};")
    instance.add_file(data_file)
    result = True
    count = 0
    while result != None and count <= 100:
        with instance.branch() as opt:
            result = opt.solve()
            # print(result)
            try:
                allocation = result["studentToProject"]
                counts = result["counts"]
                print(count, counts)
                rank = result["studentRanksProjectAt"]
                utils = result["util_per_agent"]
            except:
                break
        with open(str(utility_sum_constraint)+"_allocations_similar_1.csv", "ab") as f:
            np.savetxt(f, allocation,fmt="%d", delimiter=",", newline=",")
            f.write(b"\n")
        with open(str(utility_sum_constraint)+"_ranks_similar_1.csv", "ab") as f:
            np.savetxt(f, rank,fmt="%d", delimiter=",", newline=",")
            f.write(b"\n")
        with open(str(utility_sum_constraint)+"_utilities_similar_1.csv", "ab") as f:
            np.savetxt(f, utils,fmt="%d", delimiter=",", newline=",")
            f.write(b"\n")
        instance.add_string(f"constraint studentToProject!={allocation};\n")
        instance.add_string(f"constraint counts!={counts};\n")
        count +=1
    return allocations, utilities, ranks




contrained_utilities = range(235,237)
for i in contrained_utilities:
    print("Currently on: ", i)
    allocations, utilities, ranks = all_sol(project_allocation, "./data/similar_1/similar_1.dzn", i)