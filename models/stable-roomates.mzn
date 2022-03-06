include "globals.mzn";

int: num_roommates;
int: num_rooms = num_roommates/2;
set of int: ROOMATES = 0..num_roommates;
set of int: ROOMS = 0..num_rooms;

array[1..num_roommates
1..num_roommates] of var 1..num_men: rankRoomates;

array[1..2
ROOMATES]:assignment;

