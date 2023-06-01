from gitProject.commands.command import Command
from gitProject.infrastructure.git_command_executor import GitCommandExecutor


class CommitCommand(Command):
    def __init__(self, file_path, commit_strategy):
        self.file_path = file_path
        self.commit_strategy = commit_strategy
        self.command_executor = GitCommandExecutor()

    def execute(self):
        self.command_executor.execute(f'git add {self.file_path}')
        self.command_executor.execute(
            f'git commit -m "First commit for the day!"')
        self.command_executor.execute('git push')
