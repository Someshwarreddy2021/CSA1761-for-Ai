% Facts about animal characteristics
fact(has_feathers).
fact(has_wings).
fact(lays_eggs).

% Rules to deduce animal types based on characteristics
if(bird) :- fact(has_feathers), fact(has_wings), fact(lays_eggs).
if(mammal) :- fact(has_fur), fact(gives_birth).
if(reptile) :- fact(lays_eggs), fact(has_scales).

% Forward chaining rule to infer a type based on facts
forward_chaining(Conclusion) :-
    if(Conclusion),         % Find a rule that leads to Conclusion
    \+ fact(Conclusion),    % Check if Conclusion is not already a known fact
    assertz(fact(Conclusion)).  % Assert the new fact

% Querying until no new facts can be derived
infer :-
    forward_chaining(Conclusion),
    write('Derived: '), writeln(Conclusion),
    infer.  % Recur to derive more facts

infer :-  % Base case: stop when no more new facts are derived
    writeln('No more facts can be derived.').

% Starting point to reset facts and start inference
start_inference :-
    retractall(fact(_)),       % Remove any previously derived facts
    % Set initial known facts for this example
    assertz(fact(has_feathers)),
    assertz(fact(has_wings)),
    assertz(fact(lays_eggs)),
    infer.
rainy(day1).
cloudy(day2).
sunny(day3).

% Rules
wet(X) :- rainy(X).
wet(X) :- cloudy(X), precipitation(X).
flood(X) :- wet(X), heavy_rain(X).
precipitation(X) :- rainy(X).
heavy_rain(X) :- rainy(X).

% Query to demonstrate forward chaining
forward_chaining(Day) :-
    writeln('Day: ' + Day),
    (rainy(Day) -> writeln('It is raining.');
     cloudy(Day) -> writeln('It is cloudy.');
     sunny(Day) -> writeln('It is sunny.')),
    (wet(Day) -> writeln('It is wet.');
     writeln('It is not wet.')),
    (flood(Day) -> writeln('There is a flood.');
     writeln('There is no flood.')),
    (precipitation(Day) -> writeln('There is precipitation.');
     writeln('There is no precipitation.')),
    (heavy_rain(Day) -> writeln('There is heavy rain.');
     writeln('There is no heavy rain.')).
