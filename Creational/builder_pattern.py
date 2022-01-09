class Builder:
    def build_part(self, element):
        pass

    def get_result(self):
        pass


class HexBuilder(Builder):
    def __init__(self):
        self._result_hex_string = ''

    def build_part(self, element):
        self._result_hex_string += f"0x{ord(element):02x} "

    def get_result(self):
        return self._result_hex_string


class UpperBuilder(Builder):
    def __init__(self):
        self._result_upper_string = ''

    def build_part(self, element):
        self._result_upper_string += element.upper()

    def get_result(self):
        return self._result_upper_string


class LowerBuilder(Builder):
    def __init__(self):
        self._result_lower_string = ''

    def build_part(self, element):
        self._result_lower_string += element.lower()

    def get_result(self):
        return self._result_lower_string


class CounterBuilder(Builder):
    def __init__(self):
        self._result_counter = 0

    def build_part(self, element):
        self._result_counter += 1

    def get_result(self):
        return self._result_counter


class Director:
    def __init__(self, file_name):
        self._file_name = file_name
        self._builder = None

    def construct(self):
        with open(self._file_name) as file:
            for line in file:
                for char in line:
                    self._builder.build_part(char)

    def set_builder(self, builder):
        self._builder = builder

    def get_result(self):
        return self._builder.get_result()


def main():
    director = Director('test.txt')

    hex_builder = HexBuilder()
    upper_builder = UpperBuilder()
    lower_builder = LowerBuilder()
    counter_builder = CounterBuilder()

    director.set_builder(hex_builder)
    director.construct()
    print(director.get_result())

    director.set_builder(upper_builder)
    director.construct()
    print(director.get_result())

    director.set_builder(lower_builder)
    director.construct()
    print(director.get_result())

    director.set_builder(counter_builder)
    director.construct()
    print(director.get_result())


if __name__ == '__main__':
    main()