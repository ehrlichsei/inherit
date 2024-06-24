class Parent:
    def show(self):
        print("这是父类的方法")

class Child(Parent):
    def show(self):
        print("这是子类的方法")

# 创建一个子类的实例
child = Child()

# 调用 show 方法
child.show()
