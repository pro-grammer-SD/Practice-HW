class Reverse:
    def __init__(self, s=""):
        self.s = input("Enter a string: ") if not s else s

    def get_reversed(self):
        return self.s[::-1]

r = Reverse()
print(r.get_reversed())
