"""
    工厂方法模式
        在工厂方法模式中，我们执行单个函数，传入一个参数(提供信息表明我们想要什么)，
        但并不要求知道任何关于对象如何实现以及对象来自哪里的细节。
"""


class Car:

    def go(self) -> None:
        print("Drive a car")


class AirPlane:

    def go(self) -> None:
        print("By plane")


def factory(way: str):
    detail = None
    if way == "car":
        detail = Car()
    elif way == "airplane":
        detail = AirPlane()

    if detail:
        return detail
    raise NotImplementedError(way)


if __name__ == '__main__':
    factory("car").go()
    factory("airplane").go()
    factory("train").go()
