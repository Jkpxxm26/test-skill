# แผนอัพเดตระบบในอนาคต 
# (1) ระบบนาที
# (2) ระบบถ้าจ่ายเงินจำนวนเงินน้อยกว่าราคาอาหารรวม ให้สามารถจ่ายเงินเพิ่มได้ จนกว่าจะครบ
# (3) ระบบ Vat 7%
import time

class Defualt_Rt:
    def __init__(self):
        self.num_plate = input("เลขทะเบียนรถ: ")
        self.excu_plate = "sss-111" #------------(1)e
        self.menu = ["สปาเก็ตตี้", "ข้าวผัดมันเนื้อ", "เนื้อริบอาย"]
        self.A_drink = ["Red vine", "Champagne", "Vine"]
        self.soft_drink = ["Cola", "Est", "Fanta"]
        self.nm_drink = ["Water", "Mineral"]
        self.all_drink = self.A_drink + self.soft_drink + self.nm_drink
        self.all_menu = self.menu + self.A_drink + self.all_drink

#------ รับข้อมูล อาหาร / จำนวน
        while True:
            self.user_input = input("อาหารที่ต้องการสั่ง: ")
            if self.user_input not in self.all_menu:
                print("Sorry, My rest not have this.")
                time.sleep(1)
                print("Please choise again!")
                time.sleep(1)
                continue
            try:
                self.amount = int(input("จำนวนที่ต้องการสั่ง: "))
            except ValueError:
                print("ใส่ตัวเลขเท่านั้น")
                print("Please try again!")
                continue
            
            if self.amount <= 0:
                print("ขั้นต่ำ 1ชิ้น")
                time.sleep(1)
                print("Please choise again!")
                time.sleep(1)
                continue
            else:
                break

#----- คำนวณราคา จากผู้ใช้
    def cal_menu(self, hours, minute):
        if self.user_input in self.menu:
            if self.user_input == "เนื้อริบอาย":
                price = 120
            else:
                price = 50

        elif self.user_input in self.A_drink:
            if self.user_input == "Champagne":
                price = 250
            else:
                price = 200

        elif self.user_input in self.soft_drink:
            price = 20 

        elif self.user_input in self.nm_drink:
            if self.user_input == "Mineral":
                price = 20
            else:
                price = 10

#------- ราคาจอดรถรายชม. 
        # if minute == 60:
        #     hours = hours + 1
        #     minute =  ------[รออัพเดต]
               
        if hours >= 1 or minute == 60:
            price_hours = 20
            
        elif hours == 0 and 0 < minute < 60:
            price_hours = 0

#------- (1)คำนวณราคาอาหาร / (2)ราคารายการอาหาร + ราคาจอดรถรายชม.      
        self.result_price = (self.amount * price)
        self.result_time = (hours * price_hours)
        self.result = self.result_price + self.result_time

#------- ส่วนลดสำหรับทะเบียนรถพิเศษ        
        if self.num_plate == self.excu_plate:
            bonus = 50
            self.result = self.result * (100 - bonus) // 100
            bonus_text = "ยินดีด้วย คุณได้ส่วนลด 50%!"

#------- User เลือกอาหาร ใช้หน่วย(text)=จาน / เลือกอันอื่น(เครื่องดื่ม)=ขวด
        if self.user_input in self.menu:
            text = "จาน"
        else:
            text = "ขวด"
        
        if minute == 0:
            text_box = f"คุณได้สั่ง {self.user_input} จำนวน {self.amount}{text} จอดรถ {hours}ชั่วโมง"

        else:
            text_box = f"คุณได้สั่ง {self.user_input} จำนวน {self.amount}{text} จอดรถ {hours}ชั่วโมง {minute}นาที"

        print(text_box)
        if self.num_plate == self.excu_plate:
            print(bonus_text)
        time.sleep(0.5)

#------- บอกเวลาจอดรถและราคาอาหาร
        print(f"|ราคารวม {self.result}บาท|")
        time.sleep(1.5)

        while True:
            try:
                user_cart = int(input("ใส่เลขบัตรเดรดิต: "))
                user_insert_money = int(input("ใส่จำนวนเงิน: "))            
            except ValueError:
                print("ใส่แต่ตัวเลขเท่านั้น!")
                continue

            if user_insert_money <= 0 or user_insert_money < self.result:
                print("จำนวนเงินไม่พอ!")
                continue 
            else:
                break
            
        new_result = user_insert_money - self.result
        time.sleep(1)
        
        return f"|กำลังทอน {new_result}บาท|"
        time.sleep(3)

# user1 = Defualt_Rt()
# print(user1.cal_menu(2, 0))

class rest_systhem(Defualt_Rt):
    def __init__(self):
        super().__init__()
        self.owner = "Prem"
        
        
            
            
            
        