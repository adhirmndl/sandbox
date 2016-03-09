class Node():
    value  = None
    nxt    = None
    prev   = None
    def __init__(self, value):
        self.value = value
class LList():
    head = None
    def insert(self, val):
        newNode = Node(val)
        if self.head is not None:
            newNode.nxt = self.head
            self.head.prev = newNode
        self.head = newNode
        return self

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def chop_top(self):
        if self.head is None:
            return None
        self.head = self.head.nxt
        return self

    def __str__(self):
        tmpHead = self.head
        strList = '['
        while (tmpHead):
           strList += str(tmpHead.value) + ', '
           tmpHead = tmpHead.nxt
        return strList[:-2] + ']'

    def search(self, k):
        tmpHead = self.head
        found = False
        while tmpHead:
            if tmpHead.value == k:
                found = True
                break
            tmpHead = tmpHead.nxt
        return found

    def delete(self, k):
        if not self.search(k):
            return False
        x = self.head
        while x:
            if x.value == k:
                if x.prev is None:
                    self.head = x.nxt
                else:
                    x.prev.nxt = x.nxt
                if x.nxt is not None:
                    x.nxt.prev = x.prev
                break
            x = x.nxt
        return True

    def reverseRec(self):
        self = self.rev_helper(LList(), self)
        return str(self)

    def reverse(self):
        nxtNode  = None
        current  = self.head
        prevNode = None
        while(current):
            nxtNode = current.nxt
            current.nxt = prevNode
            prevNode = current
            current = nxtNode
        self.head = prevNode
        return self

    def rev_helper(self, acc, llist):
        if llist is None:
            return acc
        else:
            return self.rev_helper(acc.insert(llist.top()), llist.chop_top())


def createDummyList():
    dummyList = LList()
    dummyList.insert(50)
    dummyList.insert(40)
    dummyList.insert(30)
    dummyList.insert(20)
    dummyList.insert(10)
    return dummyList

if __name__ == '__main__':
    llist = createDummyList()
    print llist
    print llist.search(30)
    print llist.search(90)
    print llist.delete(90)
    print llist.delete(10)
    print llist
    print llist.reverse()
