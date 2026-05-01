1import threading 
2
3class ZeroEvenOdd:
4    def __init__(self, n):
5        self.n = n
6
7        self.zero_thread = threading.Semaphore(1)
8        self.even_thread = threading.Semaphore(0)
9        self.odd_thread = threading.Semaphore(0)
10            
11	# printNumber(x) outputs "x", where x is an integer.
12    def zero(self, printNumber: 'Callable[[int], None]') -> None:
13        for i in range(1, self.n + 1):
14            self.zero_thread.acquire()
15            printNumber(0)
16            if i%2==0:
17                self.even_thread.release()
18            else:
19                self.odd_thread.release()
20
21        
22    def even(self, printNumber: 'Callable[[int], None]') -> None:
23        for i in range(2, self.n + 1, 2):
24            self.even_thread.acquire()
25            printNumber(i)
26            self.zero_thread.release()
27        
28        
29        
30    def odd(self, printNumber: 'Callable[[int], None]') -> None:
31        for i in range(1, self.n + 1, 2):
32            self.odd_thread.acquire()
33            printNumber(i)
34            self.zero_thread.release()
35        
36        