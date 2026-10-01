# import tkinter as tk
# from tkinter import simpledialog, messagebox
# import time

# def Read_file_function():
#     with open("text_skill.txt", "r") as Read_data_name_list:
#         data = Read_data_name_list.read()
#         return data


# user_input = input("เพิ่มชื่อใครก็ได้: ") + "\n"

# with open("text_skill.txt", "a") as add_name:
#     add_name.writelines(user_input)
#     print("เพิ่มเสร็จแล้ว")

# name_list = open("text_skill.txt", "r")
# for lines in name_list:
#     print(lines)

# # สร้างหน้าต่างหลัก (ซ่อนไว้ไม่ต้องแสดงก็ได้)
# # root = tk.Tk()
# # root.withdraw()

# # import tkinter as tk
# # from tkinter import messagebox

# # # สร้างหน้าต่างหลัก (ซ่อนไว้ไม่ต้องแสดงก็ได้)
# # root = tk.Tk()
# # root.withdraw() 

# # # 1. กล่องข้อความแจ้งเตือนทั่วไป (Info)
# # messagebox.showinfo("แจ้งเตือน", "บันทึกข้อมูลเรียบร้อยแล้ว!")

# # # 2. กล่องข้อความแจ้งเตือนแบบเตือนภัย/ระวัง (Warning)
# # messagebox.showwarning("คำเตือน", "พื้นที่จัดเก็บใกล้เต็ม!")

# # # 3. กล่องข้อความแจ้งเตือนแบบ Error (Error)
# # messagebox.showerror("101", "เกิดข้อผิดพลาดในการเชื่อมต่อ")

# # # 4. กล่องข้อความถามยืนยัน (Yes/No)
# # result = messagebox.askquestion("ยืนยัน", "คุณต้องการลบข้อมูลนี้หรือไม่?")
# # if result == 'yes':
# #     print("ผู้ใช้เลือก Yes")
# # else:
# #     print("ผู้ใช้เลือก No")

# # สร้างหน้าต่างหลักและซ่อนไว้
# # root = tk.Tk()
# # root.withdraw()

# # # 1. กล่องรับข้อความทั่วไป (String)
# # name_of_user = simpledialog.askstring("กรอกข้อมูล", "กรุณาใส่ชื่อของคุณ:")

# # # ตรวจสอบว่าผู้ใช้พิมพ์อะไรกลับมาหรือไม่
# # if name_of_user:
# #     with open("text_skill.txt", "a") as user_input_name:
# #         user_input_name.writelines(name_of_user)
# #         print(messagebox.showinfo("เสร็จ", "เราได้เพิ่มชื่อของคุณแล้ว!"))
# #     print("เพิ่มชื่อของ Userแล้ว")
# # else:
# #     messagebox.showwarning("คำเตือน", "คุณไม่ได้กรอกชื่อ หรือกด Cancel")



# print(Read_file_function())
