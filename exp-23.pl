male(john).
male(michael).
male(david).
female(mary).
female(emily).

parent(john, michael).
parent(mary, michael).
parent(michael, david).
parent(michael, emily).

% Rules: Family relationships
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
child(X, Y) :- parent(Y, X).

% Queries
family_info(X) :-
    writeln('Parents of ' + X + ':'), findall(P, parent(P, X), Parents), writeln(Parents),
    writeln('Children of ' + X + ':'), findall(C, child(X, C), Children), writeln(Children).
