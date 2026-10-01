# แผนอัพเดตระบบในอนาคต 
# (1) เพิ่มข้อมูลData ที่ลูกค้าสั่งเข้าไฟล์ txt เขียนได้ อ่านได้
# (2) ระบบนาที
# (3) ระบบถ้าจ่ายเงินจำนวนเงินน้อยกว่าราคาอาหารรวม ให้สามารถจ่ายเงินเพิ่มได้ จนกว่าจะครบ --- เสร็จ
# (4) ระบบ Vat 7%
import time

class Defualt_Rt:
    def __init__(self):
        self.num_plate = input("เลขทะเบียนรถ: ")
        self.excu_plate = "sss-111" #------------(1)
        self.menu = ["สปาเก็ตตี้", "ข้าวผัดมันเนื้อ", "เนื้อริบอาย"]
        self.A_drink = ["Red vine", "Champagne", "Vine"]
        self.soft_drink = ["Cola", "Est", "Fanta"]
        self.nm_drink = ["Water", "Mineral"]
        self.all_drink = self.A_drink + self.soft_drink + self.nm_drink
        self.all_menu = self.menu + self.all_drink

#----- คำนวณราคา จากผู้ใช้
    def cal_menu(self, hours, minute):
        #------ รับข้อมูล อาหาร / จำนวน
        def Input_Menu():
            while True:
                self.user_input = input("อาหารที่ต้องการสั่ง: ").strip().capitalize()
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
                
            if hours >= 1 or minute == 60:  #----- ปรับแบบเหมาจ่าย นึกถึงความเป็นจริง
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
            print(f"|ราคารวม {self.result}บาท|\n")
            time.sleep(1.5)

        Input_Menu()

#------- จ่ายเงิน (Cash/Card)
        print("ต้องการจ่ายเงินรูปแบบไหน")
        time.sleep(0.5)
        self.Cash_card = input("Cash / Card? : ").strip().capitalize()
        # Card
        if self.Cash_card == "Card":
            while True:
                try:
                    self.user_cart = int(input("ใส่เลขบัตรเดรดิต: "))
                    self.user_insert_money = int(input("ใส่จำนวนเงิน: "))            
                except ValueError:
                    print("ใส่แต่ตัวเลขเท่านั้น!")
                    continue

                if self.user_insert_money <= 0 or self.user_insert_money < self.result:
                    print("ยอดเงินไม่เพียงพอ!\n")
                    time.sleep(1)
                    print("คุณต้องการทำรายการต่อไหม?")
                    print("ทำต่อ: Yes / ทำรายการใหม่: No")
                    yes_no = input("Anwser: ").strip().capitalize()
                    if yes_no == "Yes":
                        continue
                    elif yes_no == "No":
                        Input_Menu()
                    else:
                        break    
                
            new_result = self.user_insert_money - self.result
            time.sleep(1)
            
            return f"|กำลังทอน {new_result}บาท|"
        # Cash
        elif self.Cash_card == "Cash":
            self.cash_user = 0
            print(f"|ราคารวม {self.result}บาท|\n")
            while True:
                self.pay_cash = int(input("ใส่เงิน: "))
                self.cash_user = self.cash_user + self.pay_cash

                if self.cash_user < self.result:
                    self.money = self.result - self.cash_user
                    print(f"ขาดเงินอีก {self.money}บาท")
                    continue
                elif self.cash_user == self.result:
                    break

            return "ทำรายการสำเร็จ ขอบคุณครับ/ค่ะ"


            


user1 = Defualt_Rt()
print(user1.cal_menu(2, 0))

class rest_systhem(Defualt_Rt):
    def __init__(self):
        super().__init__()
        self.owner = "Prem"
        
        
            
            
            
        