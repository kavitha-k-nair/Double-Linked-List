class Node:
    def __init__(self,prev,data,next):
        self.prev = prev
        self.data = data
        self.next = next

class Operation:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beg(self,ele):
        self.ele = ele
        if self.head == None:
            node = Node(None,self.ele,None)
            self.head = node
            self.tail = node
            return

        node = Node(None,self.ele,self.head)
        self.head.prev = node
        self.head = node

    def insert_pos(self,ele,pos):
        self.ele = ele
        self.pos = pos
        if self.pos>1 and self.head==None:
            print("Invalid Position")
            return
        
        if self.pos == 1:
            self.insert_beg(self.ele)
            return

        count = 1
        temp = self.head
        while count != self.pos-1:
            if temp.next:
                temp = temp.next
                count += 1
            else:
                print("Invalid Position")
                return

        if temp.next:
            next_node = temp.next
            node = Node(temp,self.ele,next_node)
            next_node.prev = node
            temp.next = node
        else:
            self.insert_end(self.ele)

    def insert_end(self,ele):
        self.ele = ele
        if self.head ==None:
            self.insert_beg(self.ele)
            return

        node = Node(self.tail,self.ele,None)
        self.tail.next = node
        self.tail = node
            
    def delete_beg(self):
        if self.head == None:
            print("Empty")
            return

        if self.head.next == None:
            self.head = None
            self.next = None
            self.tail = None
            return
        
        next_node = self.head.next
        next_node.prev = None
        self.head.next = None
        self.head = next_node

    def delete_pos(self,pos):
        self.pos = pos
        if self.head==None:
            print("Empty")
            return

        if self.pos == 1:
            self.delete_beg()
            return

        count = 1
        temp = self.head
        while count != self.pos-1:
            if temp:
                temp = temp.next
                count += 1
            else:
                print("Invalid Position")
                return

        if temp.next == None:
            print("Invalid Position")
            return

        if temp.next.next==None:
            self.delete_end()
            return

        next_node = temp.next.next
        temp.next = next_node
        next_node.prev = temp

    def delete_end(self):
        if self.head==None:
            print("Empty")
            return

        if self.tail.prev == None:
            self.head = None
            self.next = None
            self.tail = None
            return
        
        temp = self.tail.prev
        temp.next = None
        self.tail = temp

    def search(self,ele):
        self.ele = ele
        temp = self.head
        while temp:
            if temp.data == self.ele:
                return True
            temp = temp.next
        return False
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end ='<-->')
            temp = temp.next
        print()

print('''1.Insert at beginning  2.Insert at position  3.Insert at end
4.Delete at beginning  5.Delete at position  6.Delete at end
7.Search               8.Display             9.Exit''')

DL = Operation()

while True:
    choice = int(input("\nChoice: "))

    if choice==1:
        ele = input("Element: ")
        DL.insert_beg(ele)

    elif choice==2:
        ele = input("Element: ")
        pos = int(input("Position: "))
        DL.insert_pos(ele,pos)

    elif choice==3:
        ele = input("Element: ")
        DL.insert_end(ele)

    elif choice==4:
        DL.delete_beg()

    elif choice==5:
        pos = int(input("Position: "))
        DL.delete_pos(pos)

    elif choice==6:
        DL.delete_end()

    elif choice==7:
        ele = input("Element: ")
        print(DL.search(ele))

    elif choice==8:
        DL.display()

    else:
        exit()

