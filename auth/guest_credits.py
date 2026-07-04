class GuestCredits:

    MAX_CREDITS = 10

    def __init__(self):

        self.remaining = self.MAX_CREDITS

    def use(self, amount=1):

        if self.remaining < amount:
            return False

        self.remaining -= amount

        return True

    def get_remaining(self):

        return self.remaining

    def reset(self):

        self.remaining = self.MAX_CREDITS


guest_credits = GuestCredits()