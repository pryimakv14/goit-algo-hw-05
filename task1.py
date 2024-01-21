class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True

        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True

        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for index in range(len(self.table[key_hash])):
                if self.table[key_hash][index][0] == key and self.table[key_hash][index]:
                    del self.table[key_hash][index]
                    return True
        return False


if __name__ == '__main__':
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)
    H.insert("onion", 110)
    H.insert("gentos", 210)
    H.insert("Hinata", 310)
    H.insert("Zenitcu", 210)
    H.insert("Naruto", 220)
    H.insert("Ferir", 230)
    H.insert("apple", 1000)
    print(H.table)
    print(H.delete("apple"))
    print(H.delete("orange"))
    print(H.delete("banana"))
    print(H.delete("007"))
    print(H.table)
