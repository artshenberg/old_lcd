#!/usr/bin/env python
# coding: utf-8

# In[18]:


import matplotlib.pyplot as plt

def collatz(number):
    yield number
    while number != 1:
        if number % 2 == 0:
            number //= 2
            yield number
        else:
            number = number * 3 + 1
            yield number
            
            
def collatz_count(number):
    collatz_max, counter = 0, 0
    for i in collatz(number):
        collatz_max += i
        counter += 1
    return collatz_max / counter, counter
            
number = int(input())

print(*collatz_count(number))

for i in range(1, number + 1):
    print(*list(collatz(i)))

'''    
table = [(0, 0)]
for i in range(1, 100):
    table.append(collatz_count(i))
    
max_table = [i[0] for i in table]
count_table = [i[1] for i in table]
fig = plt.figure()
graph1 = plt.plot(max_table, 'y')
graph2 = plt.plot(count_table, 'b')
'''


# In[146]:


nums = list(map(lambda x: int(x), ''.join(input().split())))

width = int(input())
height = 2 * width + 3

tbl = ' ' + '-' * width + ' ' # top/center/bottom of digit
cel = ' ' + ' ' * width + ' ' # center of digit
lel = '|' + ' ' * width + ' ' # left side of digit
rel = ' ' + ' ' * width + '|' # right side of digit
bol = '|' + ' ' * width + '|' # both sides of digit

digits = {
          0:[tbl, bol, cel, bol, tbl],
          1:[cel, rel, cel, rel, cel],
          2:[tbl, rel, tbl, lel, tbl],
          3:[tbl, rel, tbl, rel, tbl],
          4:[cel, bol, tbl, rel, cel],
          5:[tbl, lel, tbl, rel, tbl],
          6:[tbl, lel, tbl, bol, tbl],
          7:[tbl, rel, cel, rel, cel],
          8:[tbl, bol, tbl, bol, tbl],
          9:[tbl, bol, tbl, rel, tbl]
         }

def sized(width, digits):
    if width > 1:
        for digit in digits:
            for _ in range(width-1):
                digits[digit].insert(-1, digits[digit][-2])
            for _ in range(width-1):
                digits[digit].insert(1, digits[digit][1])
    return digits

def print_top_bottom(width, l = len(nums)):
    print('x', end = '')
    print('-' * l * (width + 3), end = '')
    print('x')
    
def print_digits(height, nums, digits):
    for i in range(height):
        left_border = True
        for digit in nums:
            if left_border:
                print ('|', end = '')
            print(digits[digit][i], end = ' ')
            left_border = False
        print('|')

sized(width, digits)
print_top_bottom(width)
print_digits(height, nums, digits)
print_top_bottom(width)


# In[ ]:




