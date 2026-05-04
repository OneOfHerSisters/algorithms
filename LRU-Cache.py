1class Node:
2    def __init__(self, key=None, value=None, prev=None, next=None):
3        self.prev = prev
4        self.next = next
5        self.key = key
6        self.value = value
7        
8
9class DLList:
10    def __init__(self):
11        self.head = Node()
12        self.tail = Node()
13        self.head.next = self.tail
14        self.tail.prev = self.head
15
16    def remove(self, node):
17        node.prev.next = node.next
18        node.next.prev = node.prev
19    
20    def append(self, node):
21        node.prev = self.tail.prev
22        self.tail.prev.next = node
23        self.tail.prev = node
24        node.next = self.tail
25
26class LRUCache:
27    def __init__(self, capacity: int):
28        self.capacity = capacity
29        self.hash_map = dict()
30        self.cache = DLList()
31
32    def get(self, key: int) -> int:
33        if key in self.hash_map:
34            node = self.hash_map[key]
35            self.cache.remove(node)
36            self.cache.append(node)
37            return node.value
38        else:
39            return -1
40
41    def put(self, key: int, value: int) -> None:
42        if key in self.hash_map:
43            node = self.hash_map[key]
44            node.value = value
45            self.cache.remove(node)
46            self.cache.append(self.hash_map[key])
47        else:
48            if len(self.hash_map) == self.capacity:
49                lru = self.cache.head.next
50                self.cache.remove(lru)
51                del self.hash_map[lru.key]
52
53            self.hash_map[key] = Node(key,value)
54            self.cache.append(self.hash_map[key])    
55
56# Your LRUCache object will be instantiated and called as such:
57# obj = LRUCache(capacity)
58# param_1 = obj.get(key)
59# obj.put(key,value)