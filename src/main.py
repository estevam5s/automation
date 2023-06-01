from gitProject.commands.commit_command import CommitCommand
from gitProject.core.committer import Committer
from gitProject.core.commit_strategy import SingleCommitStrategy
from gitProject.infrastructure.git_command_executor import GitCommandExecutor
from utils.file_utils import create_file

command_executor = GitCommandExecutor()
commit_strategy = SingleCommitStrategy(command_executor)
committer = Committer(commit_strategy)

create_file("src/data/data.txt")
commit_command = CommitCommand("src/data/data.txt", commit_strategy)

committer.commit_iterations(1500, commit_command)
