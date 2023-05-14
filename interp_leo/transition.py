import re
import subprocess
from dataclasses import dataclass

from interp_leo.leo_uitls import convert_to_leo_type

@dataclass
class Transition:
    path_project_aleo: str
    name: str
    input_arguments: dict[str: str]
    return_type: str

    def __call__(self, *args, **kwargs):
        if len(args) != len(self.input_arguments):
            raise ValueError('Error input arguments. Available arguments:', self.input_arguments)

        arguments = []
        type_arguments = list(self.input_arguments.values())
        for i in range(0, len(type_arguments)):
            arg_in = args[i]
            aleo_value = convert_to_leo_type(arg_in, type_arguments[i])
            arguments.append(f'"{aleo_value}"')

        full_command = f"./leo run --path {self.path_project_aleo} -- {self.name} -- {' '.join(arguments)}"
        process = subprocess.Popen(
            full_command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        stdout, stderr = process.communicate()

        if process.returncode != 0:
            raise Exception(stderr.decode('utf-8'))

        text = stdout.decode('utf-8')
        result = re.findall('Output\n\n • (.*?)\n', text)
        return result[0]
