class Operation:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def sum(self):
        return self.a + self.b
    def diff(self):
        return self.a - self.b
    def product(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
        