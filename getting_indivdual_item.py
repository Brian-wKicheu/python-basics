mylist = ["Brian", "Vitalis", "Kevin", "Sammy", "Mercy", 23, 43.2]

for name in mylist[:-1]:

    if name == "Brian":
        print(name + " Kicheu")
    else:
        print(name)
print("Thank you for your response")
print(set(mylist), "Now this has been converted into a set")
print("This is the length of the list", len(mylist))
print("This is the string name of the list", str(mylist))
print("This is a converted list that executes a tuple", tuple(mylist))
mylist.append("Philip")
mylist.pop(2)
mylist.insert(4, "Edith")
mylist.reverse()
print(mylist)
