class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    """单项循环链表"""
    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = node


    def is_empty(self):
        """链表是否为空"""
        return self._head == None


    def length(self):
        if self.is_empty:
            return 0
        cur = self._head
        count = 1
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count


    def travel(self):
        if self.is_empty:
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.elem, end=" ")
            cur = cur.next
        #退出循环，cur指向尾节点，但尾节点的元素未打印
        print(cur.elem)


    def add(self, item):
        """头插法"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
        #退出循环，cur指向尾节点
        node.next = self._head
        self._head = node
        #cur.next = node
        cur.next = self._head


    def append(self, item):
        """尾插法"""
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            #node.next = cur.next
            node.next = self._head
            cur.next = node


    def insert(self, pos, item):
        """指定位置添加元素，不涉及到头尾节点的位置，所以和单链表处理方法一致"""
        if pos <= 0:
            self.add(item)
        elif pos >= (self.length()-1):
            self.append(item)
        else:
            pre = self._head
            count = 0
            while count <(pos-1):
                count += 1
                pre = pre.next
            #当循环退出时，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node


    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while cur.next != self._head:
            if cur.elem == item:
                #先判断此节点是否为头结点
                if cur == self._head:
                    #头结点的情况
                    #找尾节点
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                else:
                    #中间节点
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
        #退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self._head:
                # 链表只有一个节点
                self._head = None
            else:
                pre.next = cur.next


    def search(self, item):
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        #退出循环，cur指向尾节点
        if cur.elem == item:
            return True
        return False

