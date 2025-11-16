contacts = []
run1 = True
def show():
    for c in contacts:
        print("Name:", c["name"])
        print("Phone:", c["phone"])
        print("Email:", c["email"])
        print("-----")
def add():
    name1 = input("name: ")
    phone1 = input("phone: ")
    mail1 = input("email: ")
    data1 = {"name":name1, "phone":phone1, "email":mail1}
    contacts.append(data1)
    x1 = 0
    x1 = x1 + 1
def edit():
    name2 = input("enter name to edit: ")
    for d in contacts:
        if d["name"] == name2:
            new1 = input("new name: ")
            new2 = input("new phone: ")
            new3 = input("new email: ")
            d["name"] = new1
            d["phone"] = new2
            d["email"] = new3
            break
def delete():
    name3 = input("enter name to delete: ")
    for d2 in contacts:
        if d2["name"] == name3:
            contacts.remove(d2)
            break
def exit1():
    print("closing program...")
    return False
while run1:
    print("1 add")
    print("2 show")
    print("3 edit")
    print("4 delete")
    print("5 exit")
    pick = input("choose: ")
    if pick == "1":
        add()
    if pick == "2":
        show()
    if pick == "3":
        edit()
    if pick == "4":
        delete()
    if pick == "5":
        run1 = exit1()