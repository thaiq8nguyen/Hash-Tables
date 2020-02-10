# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)

        if self.storage[hashed_key] is not None:
            # set a node containing the first node of the linked list
            node = self.storage[hashed_key]
            while node:  # while there is a node, meaning node is not None
                if node.key == key:  # if a key is already existed in the linked list, replace the value
                    node.value = value
                    break  # break the while loop after a value is entered
                elif node.next:  # go to the next node if it existed
                    node = node.next
                else:  # create a LinkedPair at the node
                    node.next = LinkedPair(key, value)
                    break
        else:
            # there is no node existed at the index, create one
            self.storage[hashed_key] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)

        if self.storage[hashed_key] is None:
            print("Warning! Key not found")
            return

        # set the first node of the linked list
        node = self.storage[hashed_key]
        prev_node = None
        while node:
            if node.key == key:  # matches the current node key with the key argument, note that the key has not been hashed
                if prev_node:
                    if node.next:
                        prev_node = node.next
                    else:
                        prev_node.next = None
                else:
                    if node.next:
                        self.storage[hashed_key] = node.next
                    else:
                        self.storage[hashed_key] = None
                return node.value
            else:
                prev_node = node
                node = node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_mod(key)

        # if self.storage[hashed_key]:
        #     node = self.storage[hashed_key]
        #     while node:
        #         if node.key == key:
        #             return node.value
        #         node = node.next

        # return None

        node = self.storage[hashed_key]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_list = []
        for i in self.storage:
            node = i
            while node:
                new_list.append([node.key, node.value])
                node = node.next

        self.capacity = 2 * self.capacity
        self.storage = [None] * self.capacity

        for j in new_list:
            self.insert(j[0], j[1])


# ht = HashTable(2)
# print(ht._hash("Thai"))


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
