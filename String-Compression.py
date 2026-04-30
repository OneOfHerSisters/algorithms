1class Solution:
2    def compress(self, chars: List[str]) -> int:
3        l = 0 
4        r = 0
5        window_size = 0
6        write = 0
7        while r<len(chars):
8            while r<len(chars) and chars[l] == chars[r]:
9                r += 1
10                window_size += 1
11            
12            char = chars[l]
13            
14            chars[write] = char
15            write += 1
16
17            if window_size > 1:
18                for digit in str(window_size):
19                    chars[write] = digit
20                    write += 1
21                
22            window_size = 0
23            l = r
24            
25        del chars[write:]
26
27        return len(chars)
28
29        
30        