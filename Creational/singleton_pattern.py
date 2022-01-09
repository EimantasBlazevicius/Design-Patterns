class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=SingletonType):
    pass


x = SingletonClass()
y = SingletonClass()
print(x==y)


class NotSingletonClass:
    pass


x1 = NotSingletonClass()
y1 = NotSingletonClass()
print(x1==y1)
