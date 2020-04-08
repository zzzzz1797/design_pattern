"""
    外观模式：
        有助于隐藏系统的内部复杂性，并通过一个简化的接口向客户端暴露必要的部分。
        外观(Facade)是在已有复杂系统之上实现的一个抽象层。
        客户端代码想要使用一个复杂系统但又不关心系 统复杂性之时，这种模式是为复杂系统提供一个简单接口的理想方式。
"""
import abc
from enum import Enum

State = Enum('State', 'new running sleeping restart zombie')


class User:
    pass


class Process:
    pass


class File:
    pass


class Server(metaclass=abc.ABCMeta):

    def __init__(self):
        self.name = self.__class__.__name__

    def __str__(self):
        return self.name

    @abc.abstractmethod
    def kill(self, restart=True):
        pass

    @abc.abstractmethod
    def boot(self):
        pass


class FileServer(Server):
    def __init__(self):
        super().__init__()
        self.state = State.new

    def boot(self):
        print(f"booting the {self}")
        self.state = State.running

    def kill(self, restart=True):
        print(f"Killing {self}")
        self.state = State.restart if restart else State.zombie

    def create_file(self, user: str, name: str, permission: str):
        print(f"trying to create the file {name} for user {user} with permission{permission}")


class ProcessServer(Server):
    def __init__(self):
        super().__init__()
        self.state = State.new

    def boot(self):
        print(f"Booting the {self}")
        self.state = State.running

    def kill(self, restart=True):
        print(f"Killing {self}")
        self.state = State.restart if restart else State.zombie

    def create_process(self, user: str, name: str):
        print(f"trying to create the process {name} for user {user}")


class Operator:
    def __init__(self):
        self.fp = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fp, self.ps)]

    def create_file(self, user, name, permission):
        self.fp.create_file(user, name, permission)

    def create_process(self, user, name):
        self.ps.create_process(user, name)


if __name__ == '__main__':
    op = Operator()
    op.start()
    op.create_file("zz", "q.jpg", "-rw-r-r")
    op.create_process("asd", "ls -alt")
