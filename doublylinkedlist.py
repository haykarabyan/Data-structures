class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None # The secret sauce for a doubly linked list!

    def __repr__(self):

        return 'Node({!r})'.format(self.data)
        
 def insert_at(self, index, item):
    if not (0 <= index <= self.size):
        print('impossible')
        return 0
    if index == 0:
        return self.prepend(item)
    elif index == self.size:
        return self.append(item)


    new_node = Node(item)
    prev_node = None
    current_node = self.head
    counter = 0

    while counter != index:
        current_node = current_node.next
        counter += 1

    new_node.prev = current_node.prev
    new_node.next = current_node 
    current_node.prev.next = new_node
    current_node.prev = new_node
    self.size += 1
    
    def append(self, item):

      new_node = Node(item)
      # Check if this linked list is empty
      if self.is_empty():
          # Assign head to new node
          self.head = new_node
      else:
          # Otherwise insert new node after tail
          self.tail.next = new_node
          new_node.prev = self.tail
      # Update tail to new node regardless
      self.tail = new_node
      self.size += 1
    
    def prepend(self, item):

      # Create a new node to hold the given item
      new_node = Node(item)
      # Check if this linked list is empty
      if self.is_empty():
          # Assign tail to new node
          self.tail = new_node
      else:
          # Otherwise insert new node before head
          new_node.next = self.head
          self.head.prev = new_node
      # Update head to new node regardless
      self.head = new_node
      self.size += 1
