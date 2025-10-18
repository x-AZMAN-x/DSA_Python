class ArithmeticSolver:
    operation_type = "Algebric"
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve_expression(self):
        return (self.a + self.b) ** 2 - self.c
    
    @classmethod
    def set_operation_type(cls, new_type):
        cls.operation_type = new_type

    @staticmethod
    def display_expression():
        print("Expression: (a + b) ^ 2 - c")

if __name__ == '__main__':
    solver = ArithmeticSolver(3, 4, 5)

    print(f"Operation Type: {ArithmeticSolver.operation_type}")

    result = solver.solve_expression
    print(f"Result: {result}")

    ArithmeticSolver.set_operation_type("Polynomial")
    print(f"Updated Operation Type: {ArithmeticSolver.operation_type}")
    print(f"Operation Type: {ArithmeticSolver.operation_type}")

    ArithmeticSolver.display_expression()