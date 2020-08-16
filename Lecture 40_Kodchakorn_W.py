username = input("Username : ")
password = input("Password : ")
if username == "admin" and password == "0000":
    print("-------------------------------")
    print("--- Welcome to pparnzz'Shop ---")
    print("-------------------------------")
    print("1. Bag")
    print("2. Watch")
    select = int(input("สินค้า : "))
    ec = int(input("จำนวน : "))
    prodPrice1 = 300
    prodPrice2 = 1990
    if select == 1:
        print("Bag :",prodPrice1,"THB","x",ec,"ชิ้น")
        print("Total :",prodPrice1*ec,"THB")
    elif select == 2:
        print("Watch :",prodPrice2,"THB","x",ec,"ชิ้น")
        print("Total :",prodPrice2*ec,"THB")
else:
    print("Access denied!!")