class Movement:
    def __init__(self, delta_x: int = 0, delta_y: int = 0):
        self.delta_x = delta_x
        self.delta_y = delta_y
    
    def get_delta_x(self):
        return self.delta_x
    
    def get_delta_y(self):
        return self.delta_y
    
    def get_delta(self):
        return self.delta_x, self.delta_y

    def __str__(self) -> str:
        return f"({self.delta_x}, {self.delta_y})"