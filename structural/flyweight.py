"""
享元模式
    一个享元(Flyweight)就是一个包含状态独立的不可变(又称固有的)数据的共享对象。
    依赖状态的可变(又称非固有的)数据不应是享元的一部分，因为每个对象的这种信息都不同，无法共享。
"""
import random
from enum import Enum

TreeType = Enum("TreeType", "apple pear peach")


class Tree:
    pool = {}

    def __new__(cls, tree_type: TreeType):
        obj = cls.pool.get(tree_type)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age: int, x: int, y: int):
        print(id(self))
        print(f"Render a tree of type {self.tree_type} and age({age}) at({x}, {y})")


if __name__ == '__main__':

    min_age, max_age = 1, 30
    min_point, max_point = 0, 100
    tree_counter = 0

    for i in range(10):
        t1 = Tree(TreeType.apple)
        t1.render(
            random.randint(min_age, max_age),
            random.randint(min_point, max_point),
            random.randint(min_point, max_point)
        )

    for i in range(5):
        t1 = Tree(TreeType.pear)
        t1.render(
            random.randint(min_age, max_age),
            random.randint(min_point, max_point),
            random.randint(min_point, max_point)
        )
    for i in range(3):
        t1 = Tree(TreeType.peach)
        t1.render(
            random.randint(min_age, max_age),
            random.randint(min_point, max_point),
            random.randint(min_point, max_point)
        )

