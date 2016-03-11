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
        if self.head is None:
            return '[]'
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

    def has_loop(self):
        first  = self.head
        second = self.head.nxt
        while first and second:
            if first == second:
                return True
            if first:
                first  = first.nxt
            if second.nxt:
                second = second.nxt.nxt
            else:
                second = None
        return False

    #1
    def count(self, k):
        count = 0
        temp = self.head
        while(temp):
            if temp.value == k:
                count += 1
            temp = temp.nxt
        return count

    #2
    def getNth(self, n):
        count = n
        temp = self.head
        while(temp):
            if (temp.nxt is None) and count > 0:
                raise Exception("out of bounds")
            if count == 0:
                return temp.value
            count -=1
            temp = temp.nxt

    #3 deleteList

    #4
    def pop(self):
        if self.head is None:
            raise Exception("empty")
        temp = self.head.value
        self.head = self.head.nxt
        return temp

    #5
    def insertAtNth(self, n, value):
        if n == 0:
            self.insert(value)
            return
        current = self.head
        while n!=1 and current:
            current = current.nxt
            n -= 1
        if n == 1:
            temp = Node(value)
            temp.nxt = current.nxt
            current.nxt = temp
        else:
            raise Exception("out of bounds")

    #6
    def sortedInsert(self, value):
        current = self.head
        inPoint = None
        while current and current.value < value:
            inPoint = current
            current = current.nxt
        if self.head is None or inPoint is None:
            self.insert(value)
            return
        temp = Node(value)
        temp.nxt = inPoint.nxt
        inPoint.nxt = temp

    #7
    def insertSort(self):
        current = self.head
        self.head = None
        while current:
            self.sortedInsert(current.value)
            current = current.nxt

    #8
    def append(self, listB):
        if self.head is None:
            self.head = listB.head
        currA = self.head
        while currA.nxt:
            currA = currA.nxt
        currA.nxt = listB.head

    #9
    def frontBackSplit(self):
        back = LList()
        if not (self.head is None or self.head.nxt is None):
            slow = self.head
            fast = self.head.nxt
            while fast:
                fast = fast.nxt
                if fast:
                    slow = slow.nxt
                    fast = fast.nxt
            back.head = slow.nxt
            slow.nxt  = None
        print self
        print back

    #10
    def removeDuplicates(self):
        if self.head is None:
            return
        self.insertSort()
        print self
        current = self.head
        while current.nxt:
            if current.value == current.nxt.value:
                current.nxt = current.nxt.nxt
            else:
                current = current.nxt

def createSortedList():
    dummyList = LList()
    dummyList.insert(50)
    dummyList.insert(40)
    dummyList.insert(30)
    dummyList.insert(20)
    dummyList.insert(10)
    return dummyList

def createLoopyList():
    loopyList = LList()
    loopyList.insert(5)
    fiveNode = loopyList.head
    loopyList.insert(4)
    loopyList.insert(3)
    loopyList.insert(2)
    fiveNode.nxt = loopyList.head
    loopyList.insert(1)
    return loopyList

def test_simple():
    llist = createSortedList()
    print llist
    print llist.search(30)
    print llist.search(90)
    print llist.delete(90)
    print llist.delete(10)
    print llist
    print llist.reverse()
    print llist.has_loop()

def test_loopy():
    loopy = createLoopyList()
    print loopy.has_loop()

def test_count():
    llist = createSortedList()
    print llist.count(20)
    llist.insert(20)
    print llist.count(20)

def test_getNth():
    llist = createSortedList()
    print llist
    print llist.getNth(2)
    llist.insert(20)
    print llist
    print llist.getNth(5)

def test_pop():
    llist = createSortedList()
    print llist
    print llist.pop()
    print llist.pop()
    print llist.pop()
    print llist.pop()
    print llist.pop()
    print llist
    print llist.pop()

def test_insertAtNth():
    llist = createSortedList()
    print llist
    llist.insertAtNth(0, 78)
    print llist

def test_sortedInsert():
    llist = createSortedList()
    print llist
    llist.sortedInsert(25)
    llist.sortedInsert(60)
    llist.sortedInsert(5)
    llist.sortedInsert(15)
    print llist

def test_removeDuplicates():
    llist = createRandomList()
    llist.removeDuplicates()
    print llist

def createRandomList():
    llist = LList()
    llist.insert(43)
    llist.insert(2)
    llist.insert(2)
    llist.insert(2)
    llist.insert(2)
    llist.insert(32)
    llist.insert(32)
    llist.insert(32)
    llist.insert(32)
    llist.insert(25)
    llist.insert(20)
    llist.insert(20)
    llist.insert(21)
    llist.insert(95)
    llist.insert(95)
    llist.insert(95)
    return llist

def test_insertSort():
    llist = createRandomList()
    print llist
    llist.insertSort()
    print llist

def test_append():
    llist = createRandomList()
    print llist
    llist.insertSort()
    print llist
    listB = createSortedList()
    llist.append(listB)
    print llist

def test_frontBackSplit():
    #llist = createRandomList()
    llist = LList()
    llist.insert(3)
    print llist
    llist.frontBackSplit()

if __name__ == '__main__':
    #test_simple()
    #test_loopy()
    #test_count()
    #test_getNth()
    #test_pop()
    #test_insertAtNth()
    #test_sortedInsert()
    #test_insertSort()
    #test_append()
    #test_frontBackSplit()
    test_removeDuplicates()
