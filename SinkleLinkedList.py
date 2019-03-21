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
        for _ in range(int(input("Enter no of nodes"))):
            data = int(input("enter ele to insert"))
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
        pass
    
    def delete_first_node(self):
        pass
    
    def delete_last_node(self):
        pass
    
    def bubble_sort_exdata(self):
        pass
    
    def bubble_sort_exlinks(self):
        pass
    
    def has_cycle(self):
        pass
    
    def remove_cycle(self):
        pass
    
    def insert_cycle(self,x):
        pass
    
    def merge2(self,list2):
        pass
    
    def _merge2(self,p1,p2):
        pass
    
    def merge_sort(self):
        pass
    
    def _merge_sort_rec(self,listStart):
        pass
    
    def _divide_list(self,listStart):
        pass
        

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
    option = int(input('enter your option :'))
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
    else:
        break
