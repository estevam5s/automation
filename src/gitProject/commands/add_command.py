from gitProject.commands.command import Command
from gitProject.infrastructure.git_command_executor import GitCommandExecutor


class AddCommand(Command):
    def __init__(self, file_path):
        self.file_path = file_path
        self.command_executor = GitCommandExecutor()

    def execute(self):
        self.command_executor.execute(f'git add {self.file_path}')
