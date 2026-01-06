class MyMeta(type):

    def __new__(mcs, name, bases, nameplace):
        print(f"Вызов __new__ meta")
        cls = super().__new__(mcs, name, bases, nameplace)
        if not hasattr(cls, '__annotations__'):
            cls.__annotations__ = {}
        return cls
    
    def __init__(cls, name, bases, nameplace):
        print(f"Вызов __init__ meta")
        super().__init__(name, bases, nameplace)

        if 'add_repo' in nameplace:
            original_add_repository = cls.add_repository



class MyClass(metaclass = MyMeta):

    global_value : int

    def __init__(self, value):
        print(f"Вызов __init__ myclass")
        self.value = value

m = MyClass(20)
print(m.__annotations__)
setattr(m, "value2", 100)
print(m.__annotations__)