% Define edges in the graph (Node1, Node2, Cost).
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 1).
edge(c, d, 1).
edge(c, e, 5).
edge(d, goal, 2).
edge(e, goal, 1).

% Define heuristic values for each node (heuristic is 0 for the goal node).
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 3).
heuristic(d, 2).
heuristic(e, 4).
heuristic(goal, 0).

% Best First Search implementation
best_first_search(Start, Goal, Path, Cost) :-
    % Initialize the open list with the starting node
    heuristic(Start, H),
    best_first([[Start, 0, H]], [], Goal, Path, Cost).

% best_first(OpenList, ClosedList, Goal, Path, Cost)
best_first([[Node, Cost, _]|_], _, Node, [Node], Cost) :-
    % If the first node in OpenList is the Goal node, we're done
    write('Goal reached: '), writeln(Node).

best_first([[Node, G, _]|RestOpen], Closed, Goal, [Node|Path], Cost) :-
    % Expand the current node
    findall([Next, NewG, F],
            (edge(Node, Next, StepCost),          % Find adjacent nodes
             \+ member(Next, Closed),             % Exclude nodes already in Closed
             \+ member([Next, _, _], RestOpen),   % Exclude nodes already in Open
             % Define edges in the graph (Node1, Node2, Cost).
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 1).
edge(c, d, 1).
edge(c, e, 5).
edge(d, goal, 2).
edge(e, goal, 1).

% Define heuristic values for each node (heuristic is 0 for the goal node).
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 3).
heuristic(d, 2).
heuristic(e, 4).
heuristic(goal, 0).

% Best First Search implementation
best_first_search(Start, Goal, Path, Cost) :-
    % Initialize the open list with the starting node
    heuristic(Start, H),
    best_first([[Start, 0, H]], [], Goal, Path, Cost).

% best_first(OpenList, ClosedList, Goal, Path, Cost)
best_first([[Node, Cost, _]|_], _, Node, [Node], Cost) :-
    % If the first node in OpenList is the Goal node, we're done
    write('Goal reached: '), writeln(Node).

best_first([[Node, G, _]|RestOpen], Closed, Goal, [Node|Path], Cost) :-
    % Expand the current node
    findall([Next, NewG, F],
            (edge(Node, Next, StepCost),          % Find adjacent nodes
             \+ member(Next, Closed),             % Exclude nodes already in Closed
             \+ member([Next, _, _], RestOpen),   % Exclude nodes already in Open
             NewG is G + StepCost,                % Calculate new path cost
             heuristic(Next, H),                  % Retrieve heuristic
             F is NewG + H),                      % Calculate f = g + h
            Children),

    % Append new children nodes to Open list, then sort by F value
    append(RestOpen, Children, NewOpen),

    % Sort Open list by the third element (F value)
    include(has_three_elements, NewOpen, FilteredNewOpen), % Ensure all lists have three elements
    sort(2, @=<, FilteredNewOpen, SortedOpen),             % Sort by the F value (second element)

    % Recursive call with updated Open and Closed lists
    best_first(SortedOpen, [Node|Closed], Goal, Path, Cost).

% Helper predicate to check list structure
has_three_elements([_, _, _]).
NewG is G + StepCost,                % Calculate new path cost
             heuristic(Next, H),                  % Retrieve heuristic
             F is NewG + H),                      % Calculate f = g + h
            Children),

    % Add current node to Closed, sort Open by heuristic F
    append(RestOpen, Children, NewOpen),
    sort(3, @=<, NewOpen, SortedOpen),

    % Recursive call with updated Open and Closed lists
    best_first(SortedOpen, [Node|Closed], Goal, Path, Cost).
