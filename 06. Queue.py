# coding:utf-8

class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        self.__list.append(item)
        # 或者----self.__list.insert(0,item)

    def dequeue(self):
        """从队列中删除一个元素"""
        return self.__list.pop(0)
        # 或者----return self.pop()

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []


    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())
    print(q.size())
