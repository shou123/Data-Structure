# coding :utf-8

class Stock(object):
    def __init__(self):
        self.__list = []


    def push(self, item):
        """添加一个元素item到栈顶"""
        self.__list.append(item)


    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()


    def peek(self):
        """返回栈顶元素"""
        return self.__list[-1]


    def is_empty(self):
        """判断站是否为空"""
        return self.__list == []


    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)



if __name__ == "__main__":
    s = Stock()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())