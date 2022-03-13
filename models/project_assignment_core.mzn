% A student-project matching
include "globals.mzn";

int: n; % number of students (which take the role of agents here)
set of int: STUDENT = 1..n;


int: p; % number of topics
set of int: PROJECT = 1..p;

int: l; % number of lecturers
set of int: LECTURER = 1..l;
array[PROJECT] of LECTURER: projectToLecturer;

% assign students to topics
array[STUDENT] of var PROJECT: studentToProject;

%-----------------------------------------------------------------------------
% preferences for the students
array[STUDENT, PROJECT] of PROJECT: studentProjectRanks; 

array[STUDENT] of var PROJECT: studentRanksProjectAt;
constraint forall(s in STUDENT) (
   studentRanksProjectAt[s] = studentProjectRanks[s, studentToProject[s]]
);

% convert this to utils -> e.g. rank 1 out of 5 gives Utility 4, rank 5 out of 5 gives Utility 0
array[STUDENT] of var PROJECT: util_per_agent;
constraint forall(s in STUDENT) (
   util_per_agent[s] = p - studentRanksProjectAt[s] 
);


array[STUDENT] of var LECTURER: studentToLecturer;

constraint forall(s in STUDENT) (studentToLecturer[s] = projectToLecturer[studentToProject[s]] );


%-----------------------------------------------------------------------------
% a global cardinality constraint % minimum 1 per project, maximal 3?, same for lecturers

int: minPerLecturer; 
% int: maxPerLecturer;
array[LECTURER] of int: maxPerLecturer; % Maximum allocations a lectuerer can take on.

int: minPerProject; 
int: maxPerProject;


% some default values for now
minPerLecturer = 0; 

% A project can have 0 or 1 students allocated to it.
minPerProject = 0; maxPerProject= 1;

constraint global_cardinality_low_up ( studentToLecturer, [l_ | l_ in LECTURER], [minPerLecturer | l_ in LECTURER], maxPerLecturer); 
constraint global_cardinality_low_up ( studentToProject, [p_ | p_ in PROJECT], [minPerProject | p_ in PROJECT], [maxPerProject | p_ in PROJECT]);

ann: random_dec_vars = int_search(studentToProject, input_order, indomain_random, complete);
var int: sumed = sum(util_per_agent);
var int: allocation_sum = sum(studentRanksProjectAt);

% constraint forall(i in studentRanksProjectAt )(i !=5 /\ i !=6);
var int: highest_rank = max(studentRanksProjectAt);
% constraint allocation_sum > 140;
% constraint allocation_sum < 155;
% var int: num_4_occourances = count(studentRanksProjectAt, 4);
% constraint count(studentRanksProjectAt, 3) = 1;

solve 
% minimize num_4_occourances;
maximize sumed;
% minimize highest_rank;
% satisfy;

output [" student to project: ",show(studentToProject), "\n student ranks project at: ", show(studentRanksProjectAt), "\n utility sum:", show(sumed),"\n allocation sum:", show(allocation_sum), "\n count of 1: ", show(count(studentRanksProjectAt, 1)),"\n count of 2: ", show(count(studentRanksProjectAt, 2)),"\n count of 3: ", show(count(studentRanksProjectAt, 3)), "\n count of 4: ", show(count(studentRanksProjectAt, 4)), "\n count of 5: ", show(count(studentRanksProjectAt, 5)), "\n count of 6: ", show(count(studentRanksProjectAt, 6)),];