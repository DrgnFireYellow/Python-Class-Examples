mylist = ["item 1", "item 2", "item 3"]
print(len(mylist))
print(mylist[1])
print(mylist)
mylist.append("item 4")
print(mylist)
mylist.pop(0)
print(mylist)
mylist[1] = "totally item 6"
print(mylist)
del mylist[1]
print(mylist)

mytuple = ("item 1", "item 2", "item 3")
print(mytuple)
print(mytuple[2])


colorsdictionary = {"apple": "red", "banana": "yellow"}
print(colorsdictionary)
print(colorsdictionary["apple"])
colorsdictionary["orange"] = "orange"
print(colorsdictionary)
colorsdictionary["pear"] = "green"
print(colorsdictionary)
colorsdictionary.pop("orange")
print(colorsdictionary)

for i in mylist:
    print(i)