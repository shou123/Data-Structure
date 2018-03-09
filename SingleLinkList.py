class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self._head = node


    def is_empty(self):    #链表是否为空
        return self._head == None


    def length(self):    #链表长度
        cur = self._head   #设置游标指向头结点
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count


    def travel(self):    #遍历整个链表
        cur = self._head
        while cur != None:
            print(cur.elem, end = " ")   #python3中按行显示出来用end
            cur = cur.next


    def add(self, item):    #链表头部添加元素
        node = Node(item)
        node.next = self._head
        self._head = node


    def append(self, item):    #链表尾部添加元素
        node = Node(item)
        if self.is_empty():   #重点，调用同一类的其他方法时，前加self
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def insert(self, pos, item):    #指定位置添加元素
        if pos <= 0:
            self.add(item)   #如果pos小于0，直接忽略为头插法
        elif pos >= (self.length()-1):
            self.append()   #如果pos的位置比链表的长度还大，在尾节点添加
        else:
            pre = self._head
            count = 0
            while count < (pos-1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node


    def remove(self, item):     #删除节点
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:   #先判断此节点是否是头结点
                if cur == self._head:   #头结点
                    self._head = cur.next   #cur.next指向None
                else:
                    pre.next = cur.next   #其他任意位置删除item所指的节点
                break
            else:
                pre = cur
                cur = cur.next


    def search(self, item):    #查看节点是否存在
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False



if __name__ == "__main__":
    ll = SingLinkList()
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