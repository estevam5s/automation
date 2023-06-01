from abc import ABC, abstractmethod
from gitProject.commands.add_command import AddCommand
from gitProject.commands.push_command import PushCommand


class CommitStrategy(ABC):
    @abstractmethod
    def commit(self, days):
        pass


class SingleCommitStrategy(CommitStrategy):
    def __init__(self, command_executor):
        self.command_executor = command_executor

    def commit(self, days):
        if days < 1:
            push_command = PushCommand()
            push_command.execute()
        else:
            dates = f"{days} days ago"
            add_command = AddCommand("data/data.txt")
            add_command.execute()
            self.command_executor.execute(
                f'git commit --date="{dates}" -m "First commit for the day!"')


# from abc import ABC, abstractmethod


# class CommitStrategy(ABC):
#     @abstractmethod
#     def commit(self, days):
#         pass


# class SingleCommitStrategy(CommitStrategy):
#     def __init__(self, command_executor, commit_command):
#         self.command_executor = command_executor
#         self.commit_command = commit_command

#     def commit(self, days):
#         if days < 1:
#             return

#         dates = f"{days} days ago"
#         message = f'{dates} <- this was the commit for the day!!'
#         self.commit_command.add_commit(message)
#         self.command_executor.execute(
#             f'git commit --date="{dates}" -am "{message}"')
