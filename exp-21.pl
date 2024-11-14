hanoi(0,_,_,_):-
    !.
hanoi(N,Source,Target,Auxiliary):-
    N>0,
    N1 is N-1,
    hanoi(N1,Source,Auxiliary,Target),
    write('Move disk '+N+' from '+Source+' to '+Target), nl,
    hanoi(N1,Auxiliary,Target,Source).
