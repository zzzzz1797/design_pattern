"""
    原型模式：
        1、创建对象的克隆。
        2、用于创建对象的完全副本。
"""
import copy
from collections import OrderedDict
from typing import List


class Book:
    def __init__(self, name: str, authors: List[str], price: float, **kwargs):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(kwargs)

    def __str__(self):
        my_list = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for k, v in ordered.items():
            my_list.append(f"{k}: {v}")
            if k == "pirce":
                my_list.append("¥")
            my_list.append("\n")
        return "".join(my_list)


class ProtoType:
    def __init__(self):
        self.obj_dict = dict()

    def register(self, identifier: str, obj: object):
        self.obj_dict[identifier] = obj

    def unregister(self, identifier):
        if identifier in self.obj_dict:
            del self.obj_dict[identifier]

    def clone(self, identifier, **kwargs) -> object:
        obj = self.obj_dict.get(identifier)
        if obj is None:
            raise ValueError

        new_obj = copy.deepcopy(obj)
        new_obj.__dict__.update(kwargs)
        return new_obj


if __name__ == '__main__':
    book1 = Book("我的野蛮女友", ["z", "h"], 112.33, publisher="猫子的小黑屋", tags=["言情", "生活"])

    prototype = ProtoType()
    prototype.register("123", book1)

    # 克隆5本书
    for i in range(5):
        new_book = prototype.clone("123", publisher=f"哈哈{i}", authors=["123"])
        print(new_book)
