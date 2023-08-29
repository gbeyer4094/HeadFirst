class CountFromBy:
    def __init__(self, v: int=0, i:int=1):
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self):
        return str(self.val)
