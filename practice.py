fruits=["apple","orange","mango","kivi"]
f_new=[]
for fruit in fruits:
    if 'o' or 'i' in fruit:
        f_new.append(fruit)
        print(fruit.upper())

# comprehension method
fruits2 = ["apple","orange","mango","kivi"]
f_new2=[fruit.upper() for fruit in fruits2 if 'o' in fruit or 'i'  in fruit]
print(f_new2)

