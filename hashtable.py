class HashTable(object):
    def __init__(self, length=4):
        self.array = [None] * length
    
    def hash(self, key):
        length = len(self.array)
        return hash(key) % length
        
    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                # If key is found, then update
                # its current value to the new value.
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:

                self.array[index].append([key, value])
        else:

            self.array[index] = []
            self.array[index].append([key, value])
    
    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through all key-value-pairs
            # and find if our key exist. If it does 
            # then return its value.
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            
            # If no return was done during loop,
            # it means key didn't exist.
            raise KeyError()
