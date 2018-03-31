# coding:utf-8

class Node(object):
    """节点"""
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinkList(object):
    """双链表"""
    def __init__(self):
        self._head = None


    def is_empty(self):
        """链表是否为空"""
        return self._head == None


    def length(self):
        """链表的长度"""
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count


    def travel(self):
        """链表的遍历"""
        cur = self._head
        while cur != None:
            print(cur.elem, end = " ")
            cur = cur.next
        print("")


    def add(self,item):
        """头插法"""
        node = Node(itme)
        node.next = self._head
        self._head = node
        node.next.prev = node


    def append(self, item):
        """尾插法"""
        if self.is_empty():
            self._head = node
        else:
            node = Node(item)
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur


    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cur = self._head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            # 当循环退出时，cur指向pos的位置
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev = node
            cur.prev.next = node


    def search(self, item):
        """查询节点是否存在"""
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


    def remove(self, item):
        """删除节点"""
        cur = self._head
        while cur != None:
            if cur.elem == item:
                #先判断此节点是否是头结点
                #头结点
                if cur == self._head:
                    self._head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    ll = DoubleLinkList()

    print(ll.is_empty())
    print(ll.length())
    print("")

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    print(ll.is_empty())
    print(ll.length())
    print("")
    # 8 1 2 3 4 5 6
    ll.insert(-2,6)
    ll.travel()
    print("")
    ll.remove(6)
    ll.travel()
    print("")
    ll.remove(5)
    ll.travel()
