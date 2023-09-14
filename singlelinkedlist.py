# 定义结点
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    # 创建单链表
    def __init__(self):
        self.head = None

    # 判断是否空表
    def isEmpty(self):
        return self.head == None

    # 获取链表长度
    def getLength(self):
        # 创建游标指向头结点
        cur = self.head
        count = 0
        # 遍历链表
        while cur != None:
            count += 1
            cur = cur.next
        return count

    # 展示单链表
    def display(self):
        # 创建游标指向头结点
        cur = self.head
        while cur != None:
            print(cur.data, end=",")
            cur = cur.next
        print()

    # 头插法
    def add(self, data):
        # 创建存储data的结点
        newNode = Node(data)
        # 将新结点的next指向头结点
        newNode.next = self.head
        # 头结点指向新结点
        self.head = newNode

    # 尾插法
    def append(self, data):
        # 创建存储data的结点
        newNode = Node(data)
        # 判断是否空表,若为空，头结点指向新结点
        if self.isEmpty():
            self.head = newNode
        # 否则，游标指向头结点，当游标的next不为空时，游标指向游标的next，将游标的next指向新结点
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode

    # 按位置插入
    def insert(self, index, data):
        # 若指定位置index为第一个元素之前，则执行头插法
        if index <= 0:
            self.add(data)
        # 若指定位置超过链表尾部，则执行尾插法
        elif index > self.getLength() - 1:
            self.append(data)
        else:
            newNode = Node(data)
            count = 0
            # 初始化为头结点
            preNode = self.head
            #pre用来指向指定位置index的前一个位置index-1，初始从头节点开始移动到指定位置
            while count < (index - 1):
                count += 1
                #插入位置结点指向插入节点的next
                preNode = preNode.next
            # 将新节点的next指向插入位置的节点的next
            newNode.next = preNode.next
            # 将插入位置的前一个节点的next指向新节点
            preNode.next = newNode

    #删除结点
    def delete(self, data):
        cur = self.head
        preNode = Node
        while cur != None:
            # 找到指定位置
            if cur.data == data:
                #如果第一个是删除的结点
                if not preNode:
                    #将头指针指向游标的next
                    self.head = cur.next
                else:
                    #删除的节点的next指向删除位置的next
                    preNode.next = cur.next
                break
            else:
                #继续按链表移动结点
                preNode = cur
                cur = cur.next

    #合并操作
    def merge(self, listB):
        #定义结点A为头结点的next
        nodeA = self.head.next
        #定义结点B为表B头结点的next
        nodeB = listB.head.next
        #初始化表C
        listC = LinkedList()
        #使表C的头结点指向头结点
        listC.head = self.head
        #表尾指向表C头结点
        tailC = listC.head
        while nodeA != None and nodeB != None:
            #结点B的数据大于结点A的数据
            if nodeA.data <= nodeB.data:
                #表尾的next指向结点A
                tailC.next = nodeA
                #表尾指向结点A
                tailC = nodeA
                #结点A指向结点A的next
                nodeA = nodeA.next
            else:
                #表尾的next指向结点B
                tailC.next = nodeB
                #表尾指向结点B
                tailC = nodeB
                #结点B指向结点B的next
                nodeB = nodeB.next
        #若结点A不为空，表尾的next指向结点A
        if nodeA != None:
            tailC.next = nodeA
        ##若结点A不为空，表尾的next指向结点A
        if nodeB != None:
            tailC.next = nodeB
        return listC



if __name__ == "__main__":
    list = LinkedList()
    list.display()

    for i in range(10):
        list.add(chr(ord("A") + i))
    print("头插法：", end="")
    list.display()

    length = list.getLength()
    print("当前表长为：%d" % length)

    list = LinkedList()
    for i in range(10):
        list.append(chr(ord("A") + i))
    print("尾插法:", end="")
    list.display()

    list.insert(3, "S")
    list.display()

    list.delete("S")
    list.display()