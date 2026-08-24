items = ["pen", " notebook", "bag", "eraser", "box"]
result = ("Available" if len(item) > 4 else "Short Name Item" for item in items)
print(list(result))