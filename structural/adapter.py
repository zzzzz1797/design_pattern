"""
    适配器模式(Adapter pattern)是一种结构型设计模式，帮助我们实现两个不兼容接口之间 的兼容。
    详细：
        如果我们希望把一个老组件用于一个新系统中， 或者把一个新组件用于一个老系统中，不对代码进行任何修改两者就能够通信的情况很少见。
        但又并非总是能修改代码，或因为我们无法访问这些代码(例如，组件以外部库的方式提供)，或因为修改代码本身就不切实际。
        在这些情况下，我们可以编写一个额外的代码层，该代码层包含 让两个接口之间能够通信需要进行的所有修改。这个代码层就叫适配器。
"""
from typing import Dict


class Computer:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def execute(self):
        return "execute a program"


class Human:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def speak(self):
        return "Hello"


class Bird:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def fly(self):
        return "fly"


class Adapter:
    def __init__(self, obj: object, adapter_methods: Dict):
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __str__(self):
        return str(self.obj)


if __name__ == '__main__':
    objects = [Computer("联想")]

    bird = Bird("乌鸦")
    objects.append(Adapter(bird, dict(execute=bird.fly)))

    human = Human("小明")
    objects.append(Adapter(human, dict(execute=human.speak)))

    for o in objects:
        print(str(o), o.execute())
