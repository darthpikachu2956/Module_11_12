import inspect


class Dog:
    def __init__(self, color, voice, speed):
        self.color = color
        self.voice = voice
        self.speed = speed

    def barking(self):
        self.voice = True
        print(f'Is the dog barking? {self.voice}')

    def running(self):
        self.speed = True
        print(f'Is the dog running? {self.speed}')


def get_methods(obj):
    return [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]


def introspection_info(obj):
    dog_dict = {}
    dog_dict.update({"Object type": obj.__class__.__name__})
    dog_dict.update({"Object attributes": list(vars(obj))})
    dog_dict.update({"Object methods": list(get_methods(Bethowen))})
    module_name = inspect.getmodule(obj)
    dog_dict.update({"Object Module": module_name.__name__})
    dog_dict.update({"Is the object related to the class Dog": isinstance(Bethowen, Dog)})
    return dog_dict


Bethowen = Dog('White&black', False, False)
intro = introspection_info(Bethowen)
print(intro)
