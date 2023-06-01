class Committer:
    def __init__(self, commit_strategy):
        self.commit_strategy = commit_strategy

    def commit_iterations(self, max_iterations, commit_command):
        for i in range(max_iterations):
            days = max_iterations - i
            self.commit_strategy.commit(days)
            commit_command.execute()
