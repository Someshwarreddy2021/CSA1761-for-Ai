person('Alice', date(1991-12-14)).
person('Bob', date(1987-05-09)).
date_of_birth(Name,DOB):-
    person(Name, DOB).
