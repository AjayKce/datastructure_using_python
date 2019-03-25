class Node:
    def __init__(self,value):
        self.info=value
        self.link=None

class SingleLinkedList:
    def __init__(self):
        self.start=None
        
    def display_list(self):
        if self.start is None:
            print("List is Empty")
            return
        else:
            p=self.start
            while p is not None:
                print(p.info," ",end='')
                p=p.link
            print()
    
    def count_node(self):
        p=self.start
        n=0
        while p is not None:
            n=n+1
            p=p.link
        print("count of Nodes: ",n)
    
    def search(self,x):
        pos=1
        p=self.start
        if self.start is None:
            print("List is Empty")
            return False
        while p is not None:
            if p.info==x:
                print(x," fount at position :",pos)
                return True
            pos=pos+1
            p=p.link
        else:
            print(x," Not found")
            return False
    
    def insert_in_beginning(self,data):
        temp = Node(data)
        if self.start is None:
            self.start=temp
            return
        temp.link=self.start
        self.start=temp
    
    def insert_at_end(self,data):
        
        temp = Node(data)
        if self.start is None:
            self.start=temp
            return
        p=self.start
        while p.link is not None:
            p=p.link
        p.link=temp

    def create_list(self):
        for _ in range(int(input("Enter no of nodes : "))):
            data = int(input("enter ele to insert : "))
            self.insert_at_end(data)
    
    def insert_after(self,data,x):
        p=self.start
        while p is not None:
            if p.info==x:
                break
            p=p.link
        if p is None:
            print(x," not found in list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link=temp
    
    def insert_before(self,data,x):
        if self.start is None:
            print("empty list")
            return
        
        if x==self.start.info:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        
        p = self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
        if p.link is None:
            print(x," not found in list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
        
    
    def insert_at_position(self,data,k):
        if k==1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        p=self.start
        i=1
        while i < k-1 and p is not None:
            p=p.link
            i+=1
        if p is None:
            print("You can insert only upto position : ",i)
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
    
    def delete_node(self,x):
        if self.start is None:
            print("empty list")
            return
        if self.start.info==x:
            self.start=self.start.link
            return
        p=self.start
        while p.link is not None:
            if p.link.info==x:
                break
            p=p.link
        if p.link is None:
            print(x," Not in list")
        else:
            p.link = p.link.link
    
    def delete_first_node(self):
        if self.start is None:
            print("empty list")
            return
        self.start = self.start.link
    
    def delete_last_node(self):
        if self.start is None:
            print("empty list")
            return
        if self.start.link is None:
            self.start=None
            return
        p = self.start
        while p.link.link is not None:
            p= p.link
        p.link=None

    def reverse_list(self):
        if self.start is None:
            print('List is Empty')
            return
        if self.start.link is None:
            print("list reversed")
            return
        prev = None
        p=self.start
        while p is not None:
            nextNode = p.link
            p.link=prev
            prev=p
            p=nextNode
        self.start = prev
        print("list reversed")
    
    def bubble_sort_exdata(self):
        p = self.start
        while p is not None:
            q=p.link
            while q is not None:
                if p.info>q.info:
                    temp=p.info
                    p.info = q.info
                    q.info=temp
                q=q.link
            p=p.link
        
    
    def bubble_sort_exlinks(self):
        p = self.start
        r = self.start
        while p is not None:
            q=p.link
            while q is not None:
                if p.info>q.info:
                    p.link=q.link
                    q.link=p
                    if p!=self.start:
                        r.link = q
                    else:
                        self.start=q
                    p,q=q,p
                q=q.link
            r=p
            p=p.link

    def merge_sorted(self,li2):
        p1 = self.start
        p2= li2.start
        if p1.info <= p2.info:
            startM=p1
            p1=p1.link
        else:
            startM=p2
            p2=p2.link
        pm = startM
        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pm.link = p1
                pm = pm.link
                p1=p1.link
            else:
                pm.link = p2
                pm = pm.link
                p2=p2.link

        if p1 is None:
            pm.link=p2
        else:
            pm.link=p1
        return startM

    def mergesort(self,list_start):
        if list_start is None or list_start.link is None:
            return list_start

        start1 = list_start
        start2 = self.divide_list(list_start)

        start1 = self.mergesort(start1)
        start2 = self.mergesort(start2)
        startm = self.mergelist(start1,start2)

        return startm

    def mergelist(self,p1,p2):
        if p1.info<=p2.info:
            startm=p1
            p1=p1.link
        else:
            startm=p2
            p2=p2.link
        pm = startm
        while p1 is not None and p2 is not None:
            if p1.info <=p2.info:
                pm.link = p1
                pm=pm.link
                p1=p1.link
            else:
                pm.link = p2
                pm=pm.link
                p2=p2.link
        if p1 is None:
            pm.link = p2
        else:
            pm.link = p1

        return startm

    def divide_list(self,p):
        q=p.link.link
        while q is not None and q.link is not None:
            p=p.link
            q=q.link.link
        start2 = p.link
        p.link = None
        return start2

    def insert_cycle(self,key):
        if self.start is None or self.start.link is None:
            print("Not able to insert cycle")
            return
        p=self.start
        flag=0
        while p.link is not None:
            if p.info == key:
                flag=1
                inter = p
            p=p.link
        if flag==1:
            p.link = inter
        else:
            print("Element Not Detected")

    def has_cycle(self):
        p=self.start
        q=self.start
        while p is not None and q is not None:
            p=p.link
            q=q.link.link
            if p==q:
                r=self.start
                while r is not p:
                    r=r.link
                    p=p.link
                    print("cycle detected at ele ",p.info)
                return
        print("No cycle Found")
        

li=SingleLinkedList()
li.create_list()

while True:
    print("\n1.Display List")
    print("2.Count Nodes")
    print("3.Search Element")
    print("4.Insert in empty list/Insert in begining of the list")
    print("5.Insert Node at end")
    print("6.Insert Node after specified")
    print("7.Insert Node before specified")
    print("8.Insert Node at given position")
    print("9.delete first node")
    print("10.delete last node")
    print("11.delete node")
    print("12.Reverse a List")
    print("13.bubble sort by exchanging data")
    print("14 bubble sort by exchanging links")
    print("15 merge two sorted list")
    print("16 merge sort")
    print("17 insert cycle")
    print("18 detect cycle")
    
    option = int(input('enter your option : '))
    if option == 1:
        li.display_list()
    elif option == 2:
        li.count_node()
    elif option == 3:
        ele = int(input('enter the ele to search :'))
        li.search(ele)
    elif option == 4:
        ele = int(input('enter the ele to insert :'))
        li.insert_in_beginning(ele)
    elif option == 5:
        ele = int(input('enter the ele to insert :'))
        li.insert_at_end(ele)
    elif option == 6:
        ele,x = list(map(int,input('enter the ele to insert and x :').split()))
        li.insert_after(ele,x)
    elif option == 7:
        ele,x = list(map(int,input('enter the ele to insert and x :').split()))
        li.insert_before(ele,x)
    elif option == 8:
        ele,k = list(map(int,input('enter the ele to insert and position :').split()))
        li.insert_at_position(ele,k)
    elif option == 9:
        li.delete_first_node()
    elif option == 10:
        li.delete_last_node()
    elif option == 11:
        ele = int(input('enter the ele to delete :'))
        li.delete_node(ele)
    elif option == 12:
        li.reverse_list()
    elif option == 13:
        li.bubble_sort_exdata()
        print("list sorted")
    elif option == 14:
        li.bubble_sort_exdata()
        print("list sorted")
    elif option == 15:
        li1=SingleLinkedList()
        li2=SingleLinkedList()
        resultList = SingleLinkedList() 
        print("Enter list 1")
        li1.create_list()
        li1.bubble_sort_exdata()
        print("Enter list 2")
        li2.create_list()
        li2.bubble_sort_exdata()
        li1.start=li1.merge_sorted(li2)
        li=li1
    elif option == 16:
        li.start = li.mergesort(li.start)
        print("list sorted")
    elif option == 17:
        ele  = int(input('enter ele : '))
        li.insert_cycle(ele)
    elif option == 18:
        li.has_cycle()
    else:
        break
