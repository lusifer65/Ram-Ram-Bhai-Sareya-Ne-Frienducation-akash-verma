class LL:
    def __init__(self):
        self.next=None
        self.val=0
        self.min=float('inf')

class MinStack:

    def __init__(self):
        self.head=None
    def push(self, val: int) -> None:
        temp=LL()
        temp.val=val
        if(self.head==None):
            self.head=temp
            self.head.min=val
        else:
            if(val<self.head.min):
                temp.min=val
            else:
                temp.min=self.head.min
            temp.next=self.head
            self.head=temp
        # print(self.head.val,self.head.min)

    def pop(self) -> None:
        self.head=self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min


