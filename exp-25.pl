% Initial locations
monkey_location(start).
banana_location(high).
box_location(start).

% Actions
move_box :-
    box_location(start),
    retract(box_location(start)),
    asserta(box_location(banana)),
    writeln('Monkey moved the box under the banana.').

climb_box :-
    box_location(banana),
    writeln('Monkey climbed onto the box.').

reach_banana :-
    box_location(banana),
    writeln('Monkey reached for the banana.').
% Declare predicates as dynamic to allow modification
:- dynamic box_location/1.
:- dynamic monkey_location/1.

% Initial locations
monkey_location(start).
banana_location(high).
box_location(start).

% Actions
move_box :-
    box_location(start),
    retract(box_location(start)),
    asserta(box_location(banana)),
    writeln('Monkey moved the box under the banana.').

climb_box :-
    box_location(banana),
    writeln('Monkey climbed onto the box.').

reach_banana :-
    box_location(banana),
    writeln('Monkey reached for the banana.').

grab_banana :-
    reach_banana,
    writeln('Monkey grabbed the banana.').

eat_banana :-
    grab_banana,
    writeln('Monkey ate the banana.').

% Goal sequence to solve the problem
solve :-
    writeln('Monkey wants to eat the banana.'),
    move_box,
    climb_box,
    reach_banana,
    grab_banana,
    eat_banana.

grab_banana :-
    reach_banana,
    writeln('Monkey grabbed the banana.').

eat_banana :-
    grab_banana,
    writeln('Monkey ate the banana.').

% Goal sequence to solve the problem
solve :-
    writeln('Monkey wants to eat the banana.'),
    move_box,
    climb_box,
    reach_banana,
    grab_banana,
    eat_banana.

