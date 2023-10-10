# 베스트셀러

import sys

input = sys.stdin.readline
books = {}

for _ in range(int(input())):
    book = input()
    books[book] = books.get(book, 0) + 1

max_book = max(books.values())
max_keys = [key for key, value in books.items() if value == max_book]
print(min(max_keys))