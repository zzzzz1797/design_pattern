"""
    抽象工厂：抽象方法的一种泛化。概括来说，一个抽象工厂是(逻辑上的)一组工厂方法，其中的每个工厂方法负责产生不同种类的对象。
    抽象工厂设计模式的实现是同属于单个类的许多个工厂方法用于创建一系列种类的相关对象。
"""

from ast import literal_eval
from typing import Callable, Any


class Frog:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obj: Callable) -> None:
        print(f"[Frog] {self} encounters {obj} and {obj.action()}")


class Bug:
    def __str__(self):
        return "Bug"

    def action(self) -> str:
        return "eats it "


class FrogWorld:
    def __init__(self, name: str):
        self.player_name = name

    def make_character(self) -> Frog:
        return Frog(self.player_name)

    def make_obstacle(self) -> Bug:
        return Bug()


class Lion:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obj: Any) -> None:
        print(f"[Lion] {self} encounters {obj} and {obj.action()}")


class Antelope:
    def __str__(self):
        return "Antelope"

    def action(self) -> str:
        return "kills it"


class LineWorld:
    def __init__(self, name: str):
        self.player_name = name

    def make_character(self) -> Lion:
        return Lion(self.player_name)

    def make_obstacle(self) -> Antelope:
        return Antelope()


class GameWorld:
    def __init__(self, factory: Any):
        self.boss = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.boss.interact_with(self.obstacle)


if __name__ == '__main__':
    # 根据年龄选择玩哪个角色
    age = literal_eval(input("请输入你的年龄："))

    GameWorld(LineWorld("胖虎") if age > 18 else FrogWorld("小明")).play()
