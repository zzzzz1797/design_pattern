"""
    建造者设计模式：一个复杂对象的构造过程与其表现分离，这样，同一个构造 过程可用于创建多个不同的表现。

    建造者模式和工厂模式的区别：
        1、工厂模式以单个步 骤创建对象，而建造者模式以多个步骤创建对象。
        2、工厂模式下，会立即返回一个创建好的对象;而在建造者模式下，仅在需要时客户端代码才显式地请求指挥者返回最终的对象。
"""
import time
from types import MethodType


class Noodles:
    def __init__(self, name: str):
        self.name = name
        self.action = None
        self.flag = None

    def __str__(self):
        if self.flag:
            return f"美味的 {self.name}, 赶紧吃吧。"

        if self.action is None:
            return f"Noodles {self.name} is not started to do"
        if self.action != "ending":
            return f"Noodles {self.name} is in {self.action}"
        else:
            self.flag = True
            return f"Noodles is ok"


class DragonBearNoodleBuilder:
    steps = ["prepare", "cook", "put_to_bowl", "flavor"]

    def __init__(self):
        self.noodle = Noodles("龙须面")

    def prepare(self):
        """准备面条"""
        self.noodle.action = "prepare"
        time.sleep(3)

    def cook(self):
        """煮一下"""
        self.noodle.action = "cook"
        time.sleep(4)

    def put_to_bowl(self):
        """放入碗中"""
        self.noodle.action = "put_to_bowl"
        time.sleep(1)

    def flavor(self):
        """调味"""
        self.noodle.action = "flavor"
        time.sleep(2)
        self.noodle.action = "ending"


class OilSplashNoodleBuilder:
    steps = ["prepare", "cook", "put_to_bowl", "flavor", "oil_splash"]

    def __init__(self):
        self.noodle = Noodles("油泼面")

    def prepare(self):
        """准备面条"""
        self.noodle.action = "prepare"
        time.sleep(3)

    def cook(self):
        """煮一下"""
        self.noodle.action = "cook"
        time.sleep(5)

    def put_to_bowl(self):
        """放入碗中"""
        self.noodle.action = "put_to_bowl"
        time.sleep(2)

    def flavor(self):
        """调味"""
        self.noodle.action = "flavor"
        time.sleep(4)

    def oil_splash(self):
        """油泼下"""
        self.noodle.action = "oil_splash"
        time.sleep(2)
        self.noodle.action = "ending"


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_noodle(self, builder):
        self.builder = builder()
        for step in [step for step in self.builder.steps if isinstance(getattr(self.builder, step, ''), MethodType)]:
            getattr(self.builder, step, '')()
            print(self.builder.noodle)

    @property
    def noodle(self):
        return self.builder.noodle


if __name__ == '__main__':
    try:
        noodle_dict = {"1": OilSplashNoodleBuilder, "2": DragonBearNoodleBuilder}
        noodle = input("吃啥面？[1]油泼面  [2]龙须面")
        waiter = Waiter()
        waiter.construct_noodle(noodle_dict[noodle])
        print(waiter.noodle)
    except KeyError:
        print("要啥自行车呀，别吓选～～～～～")
