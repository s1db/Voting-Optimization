include "globals.mzn";

int: n; set of int: STUDENT = 1..n; % number of students (which take the role of agents here)
int: p; set of int: PROJECT = 1..p; % number of projects
int: l; set of int: LECTURER = 1..l; % number of lecturers
array[PROJECT] of LECTURER: projectToLecturer;
array[STUDENT, PROJECT] of PROJECT: studentProjectRanks;

array[STUDENT] of var PROJECT: studentToProject; % assign students to topics
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

int: minPerLecturer; 
array[LECTURER] of int: maxPerLecturer; % Maximum allocations a lectuerer can take on.

int: minPerProject; 
int: maxPerProject;

set of int: COUNT_NUMBERS = 1..10;
array[COUNT_NUMBERS] of var 0..n: counts;
constraint forall(i in COUNT_NUMBERS)(counts[i] = count(studentRanksProjectAt, i));

minPerLecturer = 0; 

% A project can have 0 or 1 students allocated to it.
minPerProject = 0; maxPerProject= 1;

constraint global_cardinality_low_up ( studentToLecturer, [l_ | l_ in LECTURER], [minPerLecturer | l_ in LECTURER], maxPerLecturer); 
constraint global_cardinality_low_up ( studentToProject, [p_ | p_ in PROJECT], [minPerProject | p_ in PROJECT], [maxPerProject | p_ in PROJECT]);

var int: sumed = sum(util_per_agent);
var int: allocation_sum = sum(studentRanksProjectAt);

% constraint forall(i in studentRanksProjectAt )(i != 8);


% solve minimize allocation_sum;
solve satisfy;

output [" student to project: ",show(studentToProject), "\n student ranks project at: ", show(studentRanksProjectAt), "\n utility sum:", show(sumed),"\n allocation sum:", show(allocation_sum), "\n count: ", show(counts), ];
