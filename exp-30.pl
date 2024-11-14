rainy(day1).
cloudy(day2).
sunny(day3).
precipitation(day1).
heavy_rain(day1).

% Rules
wet(X) :- rainy(X).
wet(X) :- cloudy(X), precipitation(X).
flood(X) :- wet(X), heavy_rain(X).

% Backward chaining queries
is_wet(Day) :- wet(Day), writeln(Day + ' is wet.'), fail.
is_wet(Day) :- \+ wet(Day), writeln(Day + ' is not wet.'), fail.

is_flood(Day) :- flood(Day), writeln(Day + ' has flood.'), fail.
is_flood(Day) :- \+ flood(Day), writeln(Day + ' has no flood.'), fail.

has_precipitation(Day) :- precipitation(Day), writeln(Day + ' has precipitation.'), fail.
has_precipitation(Day) :- \+ precipitation(Day), writeln(Day + ' has no precipitation.'), fail.
