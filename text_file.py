import time

def check_member():
    
    with open("listname.txt", "r", encoding="utf-8") as read_file:
        read_data = read_file.read()

    user_input = input("ใส่ชื่อเพื่อน: ").strip().capitalize()

    if user_input in read_data:
        print(f"เจอข้อมูล: {user_input} เป็นสมาชิกในบริษัท")
    else:
        print(f"ไม่เจอข้อมูล: {user_input} ไม่ได้เป็นสมาชิก")

def show_list_member():
    with open("listname.txt", "r") as show_list:
        read_data = show_list.readlines()
        amount_member = len(read_data)
        print(f"\nมีพนักงานอยู่ {amount_member}คน")
        print("คือ...")
        time.sleep(1.5)
        print(read_data)


check_member()
time.sleep(1)
time.sleep(1)
show_list_member()