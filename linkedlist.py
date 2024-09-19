class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class Linkedlist:
    def __init__(self):
        self.head=None
        
    def insteratbigining(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def print(self):
        if self.head==None:
            print("emplty ll")
            return
        itr=self.head
        str1=''
        while itr:
            str1+=str(itr.data)+'--->'
            itr=itr.next
        print(str1)
        
    def insertatend(self,data):
        if self.head==None:
            self.head=Node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
            
        itr.next=Node(data,None)
    
    def insertvalues(self,datalist):
        self.head=None
        for data in datalist:
            self.insertatend(data)
            
    def getlength(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
        
    def removeat(self,index):
        if index<0 or index>=self.getlength():
            raise Exception("invalid index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr = self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
            
    def updateat(self,index,data):
        if index<0 or index>=self.getlength():
            raise Exceptiom("invalid index")
        if index==0:
            self.insteratbigining(data)
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
     
    def insertat(self,index,data):
        if index<0 or index>=self.getlength():
            raise Exception("invalid index")
        if index==0:
            self.insteratbigining(data)
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1       
            
    def insertaftervalue(self,dataafter,datatoinsert):
        itr= self.head
        while itr:
            if itr.data==dataafter:
                node=Node(datatoinsert,itr.next)
                itr.next=node
                break
            itr=itr.next
            
    def removebyvalue(self,data):
        if self.head is None:  # If the list is empty
            print("The list is empty.")
            return

    # Special case for head
        if self.head.data == data:
            self.head = self.head.next  # Remove the head node by updating the head
            return
    
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                return
            itr=itr.next
            
            
        
            
if __name__=='__main__':
    ll=Linkedlist()
    ll.insertvalues([1,2,3,4,5])
    ll.print()
    ll.updateat(3,9)
    ll.print()
    ll.insertat(2,23)
    ll.print()
    #ll.removeat(1)
    ll.insertaftervalue(23,6)
    print(ll.getlength())
    ll.print()
    ll.removebyvalue(23)
    ll.print()
    
    
        
        
        