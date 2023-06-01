from gitProject.commands.command import Command
from gitProject.infrastructure.git_command_executor import GitCommandExecutor


class PushCommand(Command):
    def __init__(self):
        self.command_executor = GitCommandExecutor()

    def execute(self):
        self.command_executor.execute('git push')
