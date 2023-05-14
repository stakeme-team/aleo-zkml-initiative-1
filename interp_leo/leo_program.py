from interp_leo.parser import Parser


class LeoProgram:
    def __init__(self, path):
        with open(path + '/src/main.leo', 'r') as f:
            content = f.read()
        parser = Parser(path=path, content=content)
        transitions = parser.get_transitions()
        for transition in transitions:
            setattr(self, transition.name, transition)
        self.path = path