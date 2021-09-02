"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        n=self.head
        while n.next!=None:
            n=n.next
        n.next=new_element
     
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        counter=1
        n=self.head
        if position<1:
            return None
     
        while n and counter <= position:
            if counter==position:
                return n
            n=n.next
            counter = counter+1
        return None
        
  
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
      
        counter=1
        n=self.head
        if position>1:
            while n and counter<position:
                if counter == position - 1:
                    new_element.next = n.next
                    n.next = new_element
                n = n.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        n = self.head
        previous = None
        while n.value != value and n.next:
            previous = n
            n = n.next
        if n.value == value:
            if previous:
                previous.next = n.next
            else:
                self.head = n.next
