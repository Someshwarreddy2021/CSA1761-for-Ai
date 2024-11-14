class VacuumCleaner:
    def __init__(self, initial_state):
        self.state = initial_state

    def is_goal(self):
        return self.state['A'] == 'Clean' and self.state['B'] == 'Clean'

    def clean(self):
        if self.state[self.state['position']] == 'Dirty':
            self.state[self.state['position']] = 'Clean'
            return f"Cleaned {self.state['position']}"

    def move(self):
        if self.state['position'] == 'A':
            self.state['position'] = 'B'
        else:
            self.state['position'] = 'A'
        return f"Moved to {self.state['position']}"

    def run(self):
        steps = []
        while not self.is_goal():
            if self.state[self.state['position']] == 'Dirty':
                steps.append(self.clean())
            else:
                steps.append(self.move())
        return steps

initial_state = {'A': 'Dirty', 'B': 'Dirty', 'position': 'A'}
vacuum = VacuumCleaner(initial_state)
steps = vacuum.run()
for step in steps:
    print(step)
