# coding: utf-8
list = ["aaa", "bbb", "abc", "abcd"]
for s in list:
  if "abc" in s:
    list[list.index(s)] = "zzz"
    break

print(list)

