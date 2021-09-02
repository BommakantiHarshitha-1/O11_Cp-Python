"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""
#hash table do not store null values
class HashTable(object):
    #table
    def __init__(self):
        self.table = [None]*10000
    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        H=(ord(string[0])*100)+ ord(string[1])
        return H
    
        
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        x=self.calculate_hash_value(string)
        if(self.table[x]==None or self.table[x]!=string):
            return -1
        else:
            return x
        
        
    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        # Your code goes here
        x=self.calculate_hash_value(string)
        self.table.insert(x,string)
        return -1
       
    


