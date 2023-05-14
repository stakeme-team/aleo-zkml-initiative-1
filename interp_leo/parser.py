import re
from interp_leo.transition import Transition


class Parser:
    def __init__(self, path, content: str):
        self.path = path
        self.content = content

    def get_transitions(self):
        transitions_pattern = r"transition\s+(\w+)\s*\(([^)]*)\)\s*->\s*(\w+)"
        re_transitions = re.findall(transitions_pattern, self.content)

        transitions = []
        for re_trans in re_transitions:
            if len(re_trans) == 2:
                transitions.append(
                    Transition(self.path, re_trans[0], {}, re_trans[1])
                )
                continue
            arguments = {k: v for k, v in (pair.split(': ') for pair in re_trans[1].split(', '))}
            transitions.append(
                Transition(self.path, re_trans[0], arguments, re_trans[1])
            )
        return transitions
