class Node :
    def __init__ ( self , data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
    
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
        
    def add ( self , data ) :
        if self.head != None :
            last = self.head
            end = self.head
            while ( end ) : 
                last = end
                end = end.next
            last.next = Node ( data )
        else : self.head = Node ( data )
    
    def toInt ( self ) :
        ans = 0
        temp = self.head
        while ( temp ) :
            ans *= 10
            ans += temp.data
            temp = temp.next
        return ans
        
        
num1 = LinkedList()
num1.add ( 1 )
num1.add ( 2 )
num1.add ( 3 )

num2 = LinkedList()
num2.add ( 3 )
num2.add ( 2 )
num2.add ( 1 )

print ( num1.toInt() + num2.toInt() )