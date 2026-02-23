#----------------------------------------------------
# Lab 4: Fruit Sorter
# 
# Author: CMPUT 175 Team
#----------------------------------------------------
class Stack:
    """
    A class representing a stack Abstract Data Type (ADT).
    Modify it slightly to fit the Stack Game requirements.
    Hint:
    It needs to have a maximum capacity and can be marked as 
    completed when all items are the same and the stack is full.
    """

    def __init__(self, capacity):
        # Initializes an empty stack.
        self.items = []
        self.capacity = capacity
        
    
    def is_completed(self):
        # Checks if the stack is completed (full and all items are the same).
        if self.size() == self.capacity and len(set(self.items)) == 1:
            return True
        return False

    def push(self, item): 
        # Adds an item to the top of the stack.
        if self.is_completed():
            raise Exception("Cannot push to a completed stack.")

        if self.size() >= self.capacity:
            raise Exception("Cannot push to a full stack.")
        else:
            self.items.append(item)
        # Check if the stack is now completed
        if self.size() == self.capacity:
            self.is_completed() == True
        pass
    

    def pop(self): 
        # Removes and returns the top item from the stack.
        if self.is_completed() == True:
            raise Exception("Cannot pop from a completed stack.")
        
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack.")
        return self.items.pop()

    
    def peek(self):  
        # Returns the top item of the stack without removing it.
        if self.is_empty():
            raise Exception("Cannot peek from an empty stack.")
        return self.items[-1]
         
    
    def is_empty(self):
        # Checks if the stack is empty.
        return self.items == []
        
    
    def size(self):
        # Returns the number of items in the stack.
        return len(self.items)
    
    def show(self):
        # Prints the items in the stack.
        print(self.items)
    
    def __str__(self):
        # Returns a string representation of the stack.
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        # Clears all items from the stack, does nothing if the stack is already empty.
        self.items = []
        pass  



def main():
    # ----- Stack tests (formatted) -----
    print("\n=== Stack tests ===")

    # Basic usage
    print("\n-- Basic operations --")
    s = Stack(4)
    print("Initially empty:", s.is_empty())

    s.push('A')
    s.push('B')
    s.push('C')
    print("After pushing A, B, C ->")
    print("  Stack contents:", end=" ")
    s.show()
    print(f"  Size: {s.size()}")
    print(f"  Peek (top): {s.peek()}")
    popped = s.pop()
    print(f"  Popped item: {popped}")
    print("  Stack now:", end=" ")
    s.show()
    print("  Is empty?:", s.is_empty())
    print("  String repr:", str(s))

    # Additional behavioural tests
    print("\n-- Additional tests (capacity & errors) --")
    # Test completed flag when pushing identical items up to capacity
    s2 = Stack(3)
    s2.push('X')
    s2.push('X')
    s2.push('X')
    print("s2 contents:", s2.items)
    print("s2 size:", s2.size())
    print("s2 completed?:", s2.is_completed())

    # Attempting to pop from a completed stack should raise
    try:
        s2.pop()
    except Exception as e:
        print("Expected error (pop completed):", e)

    # Attempting to push to a full/completed stack should raise
    try:
        s2.push('X')
    except Exception as e:
        print("Expected error (push completed/full):", e)

    # Test pop/peek on empty stack raise
    s3 = Stack(2)
    try:
        s3.pop()
    except Exception as e:
        print("Expected error (pop empty):", e)

    try:
        s3.peek()
    except Exception as e:
        print("Expected error (peek empty):", e)

    # Test transitions: push then pop to empty
    s4 = Stack(2)
    print("s4 is_empty initially:", s4.is_empty())
    s4.push('A')
    print("s4 size after one push:", s4.size())
    popped = s4.pop()
    print("s4 popped value:", popped)
    print("s4 is_empty after pop:", s4.is_empty())

    # Test __str__ formatting for multiple items
    s5 = Stack(4)
    s5.push('p')
    s5.push('q')
    print("s5 string repr:", str(s5))

if __name__ == "__main__":
    main()