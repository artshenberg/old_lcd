#!/usr/bin/env python
# coding: utf-8

# In[18]:

nums = list(map(lambda x: int(x), ''.join(input().split())))

width = int(input()) # changeable dimensions inputs by user
height = 2 * width + 3

# basic strings for digits
tbl = ' ' + '-' * width + ' ' # top/center/bottom of digit
cel = ' ' + ' ' * width + ' ' # center of digit
lel = '|' + ' ' * width + ' ' # left side of digit
rel = ' ' + ' ' * width + '|' # right side of digit
bol = '|' + ' ' * width + '|' # both sides of digit

# dictionary of basic print for digits
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

# changing dimensions of digits
def sized(width, digits):
    if width > 1:
        for digit in digits:
            for _ in range(width-1):
                digits[digit].insert(-1, digits[digit][-2])
            for _ in range(width-1):
                digits[digit].insert(1, digits[digit][1])
    return digits

# prints top and bottom borders
def print_top_bottom(width, l = len(nums)):
    print('x', end = '')
    print('-' * l * (width + 3), end = '')
    print('x')

# prints digits and left&right borders
def print_digits(height, nums, digits):
    for i in range(height):
        left_border = True
        for digit in nums:
            if left_border:
                print ('|', end = '')
            print(digits[digit][i], end = ' ')
            left_border = False
        print('|')

# calls functions
sized(width, digits)
print_top_bottom(width)
print_digits(height, nums, digits)
print_top_bottom(width)
