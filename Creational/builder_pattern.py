class Result:
    def __init__(self, number):
        self.number = number


class Calculator:
    def __init__(self):
        self.result = Result(0)

    def add(self, x: int):
        self.result.number += x
        return self

    def subtract(self, x: int):
        self.result.number -= x
        return self

    def multiply(self, x: int):
        self.result.number *= x
        return self

    def divide(self, x: int):
        self.result.number /= x
        return self

    def do(self) -> Result:
        return self.result

    def to_number(self):
        return self.result.number


print(Calculator()
      .add(3)
      .subtract(4)
      .add(10)
      .multiply(2)
      .divide(5)
      .to_number()
      )
