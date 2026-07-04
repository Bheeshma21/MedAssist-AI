class UsageTracker:

    def __init__(self):

        self.tokens = {}

    def add_usage(
        self,
        user,
        amount
    ):

        if user not in self.tokens:

            self.tokens[user] = 0

        self.tokens[user] += amount

    def get_usage(self, user):

        return self.tokens.get(user, 0)


usage_tracker = UsageTracker()