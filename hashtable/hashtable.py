class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # capacity set to default MIN capacity variable
        # make a list of None depending on capacity
        self.capacity = capacity
        self.slots = [None] * capacity
        self.counter = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.slots)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.counter / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        hash function 1
        """
        fnv_prime = 1099511628211
        offset_basis = 14695981039346656037

        hash = offset_basis

        for char in key:
            hash = hash * fnv_prime
            hash = hash ^ ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        hash function 2
        """
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.

        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # done in hash index with djb2 or fnv1
        index = self.hash_index(key)
        hst = HashTableEntry(key, value)
        slot = self.slots[index]

        if slot != None:
            self.slots[index] = hst
            self.slots[index].next = slot
        else:
            self.slots[index] = hst
            self.counter += 1
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
        # elif self.get_load_factor() < 0.2:
        #     self.resize(self.capacity == 8) #I don't have this part correct

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if key is key:
            self.put(key, None)
            self.counter -= 1
        else:
            print('This key was not found.')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        starter = self.hash_index(key)  # where we start
        n = self.slots[starter]
        # if not empty
        if n != None:
            while n:
                if n.key == key:
                    return n.value
                n = n.next
            return n

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # make a new hash table with the new capacity
        newTable = HashTable(new_capacity)
        # for each value in the table slots
        for spot in self.slots:
            if spot:  # checking to see if the value is there
                # if there -> update the new table using self.put(key, value)
                newTable.put(spot.key, spot.value)
                if spot.next:  # if there is a next (spot.next)
                    current = spot  # make current variable and set to spot
                    while current.next:  # while there is a current.next
                        current = current.next  # the new current id the current.next
                        # change the newTable using put method and passing the current key and value
                        newTable.put(current.key, current.value)
        # self.slots = the new hash.value
        self.slots = newTable.slots  # slots are set to new hash table slots
        # self.capacity is now the new hash.capacity
        self.capacity = newTable.capacity


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
