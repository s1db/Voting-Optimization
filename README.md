# Voting-Optimization

## Introduction
We attempt to solve multi-objective optimization problems, specifically Student Project Allocation, by extending the literature of social choice theory.
This repository constains all the code for the dissertation.

## Setup

To use the code in this directory you first need to install the required packages using requirements.txt.
If you wish to simply reproduce our results then you can choose to stop here and move onto the directory structure.


Please note to use the accumulation script(`project_allocation_accumulator.py`) you will need to install MiniZinc and Gurobi seperately on your machine.

You can use the following installation guides:
https://www.gurobi.com/documentation/9.5/quickstart_mac/software_installation_guid.html
https://www.minizinc.org/doc-2.2.3/en/installation.html

For the networkflow approach for solving the problem you may refer to the jar executable in the directory. Please note that you will need to have java installed for this and I'm not the author of this software.


## Directory Structure
```
Instances - i.e 2015, 2020, 2021, random_1, similar_1, these are the 5 instances we use in the dissertation
    data - this directory constrains all the solutions gathered from the accumulation script
    instance_name_jar.txt - this file is the input file for the jar file that constains all the implementations of the network flow algorithms
    instance_name.dzn - this in the MiniZinc datafile for the instance
    project_allocation_instance_name.py - this is the python file that generates the MiniZinc datafile.
borda_runner.py - this is the main file that runs the borda count algorithm, you just run it like a normal python file and it will ask you for an instance name, you can provide it with any of the 5 mentioned above. i.e 2015, 2020, 2021, random_1, similar_1. It returns the ids of the winning solution

copeland_runner.py - works the same way as borda runner.
schulze_runner.py - works the same way as borda runner.
winner_analysis.py - you run the python file, it will ask for an instance name, you can provide it with any of the 5 mentioned above. It then asks for an ID of the solution, you can use any that you get from the voting algorithms. It prints out the profile and cost of each solution.
```
